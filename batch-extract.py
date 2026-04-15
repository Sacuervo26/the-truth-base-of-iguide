"""Batch-extract figures from every mapped PDF into img/<slug>/

Running this once produces:
  - img/<slug>/*.{png,jpeg}   — extracted figures named by caption
  - batch-extract-report.txt  — summary per doc (# figures extracted)

After running, manually copy the paths into DOC_IMAGES in search.html.
"""
import sys, re, importlib.util
from pathlib import Path

ROOT = Path(__file__).parent
DOCS_DIR = Path(r"C:/Users/255356.SCuervo/Documents/Trainig/Draft/docs")
IMG_DIR = ROOT / "img"

# Load the extractor module so we don't shell out N times
spec = importlib.util.spec_from_file_location("extractor", ROOT / "extract-pdf-figures.py")
extractor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extractor)

# Map: PDF filename → (doc_id, folder slug)
MAPPING = [
    ("Drafting_Exterior_Walls.pdf",                           5,  "drafting-exterior-walls"),
    ("Drafting_Interior_Walls.pdf",                           6,  "drafting-interior-walls"),
    ("Room_Types-_Residential.pdf",                           7,  "room-types-residential"),
    ("Manual_Labels.pdf",                                     8,  "manual-labels"),
    ("Placement_of_Doors_with_Proper_Orientation.pdf",        9,  "placement-of-doors"),
    ("Windows.pdf",                                           10, "windows"),
    ("Drafting_Exterior_Areas.pdf",                           11, "drafting-exterior-areas"),
    ("Ordering_and_Separation_of_Floors__Backsplits.pdf",     12, "ordering-floors-backsplits"),
    ("AutoDraft_Training.docx.pdf",                           15, "autodraft-training"),
    ("Drafting_Straight_Stairs.pdf",                          16, "drafting-straight-stairs"),
    ("Drafting_Curved_Stairs.pdf",                            17, "drafting-curved-stairs"),
    ("Drafting_Spiral_Stairs.pdf",                            18, "drafting-spiral-stairs"),
    ("Drafting_Multi-Segment_Stairs.pdf",                     19, "drafting-multi-segment-stairs"),
    ("Stair_Gates.pdf",                                       20, "stair-gates"),
    ("Drafting_Curved_Walls.pdf",                             21, "drafting-curved-walls"),
    ("Fireplaces.pdf",                                        22, "fireplaces"),
    ("Drafting_Rooms_With_Sloped_Walls-Ceilings.pdf",         23, "drafting-rooms-sloped-walls"),
    ("Dimensioning_Rooms_With_Sloped_Walls.pdf",              24, "dimensioning-sloped-walls"),
    ("Unfinished_Spaces.pdf",                                 25, "unfinished-spaces"),
    ("Site Plans - Drafting & Detailing(1).pdf",              26, "site-plans-drafting-detailing"),
    ("Site Plans - Nearmap.pdf",                              27, "site-plans-nearmap"),
    ("Site Plans \u2013 Overview & Workflow 2.pdf",           28, "site-plans-overview-workflow"),
    ("Site Plans - Update (10-02-2026).pdf",                  29, "site-plans-update-feb2026"),
    ("Courtesy Update 2.pdf",                                 53, "courtesy-update"),
    ("Draft Error Correction 2.pdf",                          54, "draft-error-correction"),
    ("Draft Update_Document 1 1.pdf",                         55, "draft-update-pano-floor"),
]


def main():
    lines = ["Batch extraction report\n" + "=" * 60]
    snippet = [
        "// ─── Paste into DOC_IMAGES in search.html ──────────────────",
    ]
    total_figs = 0

    for pdf_name, doc_id, slug in MAPPING:
        pdf_path = DOCS_DIR / pdf_name
        if not pdf_path.exists():
            lines.append(f"[{doc_id}] {pdf_name}: PDF NOT FOUND")
            continue
        out_dir = IMG_DIR / slug
        # Clean any prior extraction
        if out_dir.exists():
            for f in out_dir.glob("*"):
                f.unlink()
        rows = extractor.extract(pdf_path, out_dir, min_bytes=2000)
        count = len(rows)
        total_figs += count
        lines.append(f"[{doc_id}] {pdf_name:<55} -> {count} figures in img/{slug}/")
        if count:
            files = sorted(out_dir.iterdir())
            snippet.append(f"  {doc_id}: [")
            for f in files:
                snippet.append(f"    'img/{slug}/{f.name}',")
            snippet.append("  ],")

    lines.append("\nTotal figures extracted: " + str(total_figs))
    report = "\n".join(lines) + "\n\n" + "\n".join(snippet) + "\n"
    (ROOT / "batch-extract-report.txt").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
