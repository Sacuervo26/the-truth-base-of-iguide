"""Generate markdown + images for the 7 new docs (ids 56-62) from PDFs
that were not in the original DB.

Writes:
  bookstack-export/truth-base-export/<shelf-slug>/<slug>.md
  img/<slug>/*.{png,jpeg}
  new-docs.json  (metadata manifest consumed by build-patch.js)
"""
import json, importlib.util, os, sys, io
from pathlib import Path
import fitz

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).parent
DOCS_DIR = Path(r"C:/Users/255356.SCuervo/Documents/Trainig/Draft/docs")

# Load extract-pdf-figures for image extraction
spec = importlib.util.spec_from_file_location("extractor", ROOT / "extract-pdf-figures.py")
extractor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(extractor)

NEW_DOCS = [
    {
        "id": 56, "slug": "alignment-orientation-scans",
        "pdf": "Alignment_and_Orientation_of_Scans.pdf",
        "shelf": "Draft Software & Basics", "book": "Scan Setup",
        "title": "Alignment and Orientation of Scans",
        "source": "Alignment_and_Orientation_of_Scans.pdf",
        "shelf_folder": "02-software-basics",
    },
    {
        "id": 57, "slug": "finishing-touches-inspect-area",
        "pdf": "Finishing_Touches-_Inspect_Area.pdf",
        "shelf": "Finishing Touches", "book": "Finishing Touches",
        "title": "Finishing Touches — Inspect Area",
        "source": "Finishing_Touches-_Inspect_Area.pdf",
        "shelf_folder": "15-finishing-touches",
    },
    {
        "id": 58, "slug": "finishing-touches-verify",
        "pdf": "Finishing_Touches_-_Verify.pdf",
        "shelf": "Finishing Touches", "book": "Finishing Touches",
        "title": "Finishing Touches — Verify",
        "source": "Finishing_Touches_-_Verify.pdf",
        "shelf_folder": "15-finishing-touches",
    },
    {
        "id": 59, "slug": "finishing-touches-exporting",
        "pdf": "Finishing_Touches-_Exporting.pdf",
        "shelf": "Finishing Touches", "book": "Finishing Touches",
        "title": "Finishing Touches — Exporting",
        "source": "Finishing_Touches-_Exporting.pdf",
        "shelf_folder": "15-finishing-touches",
    },
    {
        "id": 60, "slug": "void-spaces",
        "pdf": "Void_Spaces.pdf",
        "shelf": "Area Classification", "book": "Special Spaces",
        "title": "Void Spaces",
        "source": "Void_Spaces.pdf",
        "shelf_folder": "08-area-classification",
    },
    {
        "id": 61, "slug": "unnecessary-invalid-update-requests",
        "pdf": "Unnecessary or Invalid Update Requests.pdf",
        "shelf": "Updates & Corrections", "book": "Invalid Requests",
        "title": "Unnecessary or Invalid Update Requests",
        "source": "Unnecessary or Invalid Update Requests.pdf",
        "shelf_folder": "14-updates",
    },
    {
        "id": 62, "slug": "l3-missing-space-outside-boundary",
        "pdf": "ERC980_1.PDF",
        "shelf": "Errors — Level 3", "book": "Missing Spaces",
        "title": "L3: Missing Draftable Space Outside Boundary",
        "source": "ERC980_1.PDF",
        "shelf_folder": "13-errors-L3",
    },
]


def extract_pdf_text(pdf_path):
    """Plain text extraction with some cleanup (page-footers stripped)."""
    doc = fitz.open(pdf_path)
    parts = []
    for pg in doc:
        parts.append(pg.get_text())
    return "\n\n".join(parts).strip()


def main():
    manifest = []
    for d in NEW_DOCS:
        pdf_path = DOCS_DIR / d["pdf"]
        if not pdf_path.exists():
            print(f"[{d['id']}] MISSING PDF: {d['pdf']}")
            continue

        # 1. Markdown
        md_dir = ROOT / "bookstack-export" / "truth-base-export" / d["shelf_folder"]
        md_dir.mkdir(parents=True, exist_ok=True)
        md_path = md_dir / (d["slug"] + ".md")
        text = extract_pdf_text(pdf_path)
        md_path.write_text(text if text else f"{d['title']}\n\n(See original PDF for figures.)", encoding="utf-8")

        # 2. Images (use defaults; per-PDF tuning can be added later)
        img_dir = ROOT / "img" / d["slug"]
        if img_dir.exists():
            for f in img_dir.glob("*"):
                f.unlink()
        rows = extractor.extract(pdf_path, img_dir, min_bytes=2000)
        image_paths = []
        if img_dir.exists():
            for f in sorted(img_dir.iterdir()):
                if f.is_file():
                    image_paths.append(f"img/{d['slug']}/{f.name}")

        manifest.append({
            "id": d["id"],
            "slug": d["slug"],
            "shelf": d["shelf"],
            "book": d["book"],
            "title": d["title"],
            "source": d["source"],
            "md_path": str(md_path.relative_to(ROOT)).replace("\\", "/"),
            "images": image_paths,
            "figure_count": len(image_paths),
            "text_length": len(text),
        })
        print(f"[{d['id']}] {d['title']:<60}  text={len(text):>6}  figs={len(image_paths)}")

    (ROOT / "new-docs.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote new-docs.json with {len(manifest)} entries")


if __name__ == "__main__":
    main()
