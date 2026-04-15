r"""Extract images from a PDF and name them after the nearest figure caption.

Usage:
    python extract-pdf-figures.py <path-to.pdf> <output-dir> [--min-bytes N]

Logic:
  - For each page, list every embedded image with its bounding box.
  - Scan the same page for caption lines matching /^Figure\s*[#]?\s*\d.*/ or
    /^Example\s*\d.*/ with their bounding boxes.
  - Pair each image with the caption whose vertical midpoint is nearest
    (preferring captions that appear JUST BELOW the image, the usual layout).
  - Save the image as "<caption>.<ext>" stripping characters Windows forbids.
  - Drop tiny decorative images (< min-bytes, default 8000) since iGUIDE
    templates repeat a small background asset on every page.
  - Print a summary table so you can sanity-check before committing.
"""
import sys, os, re
from pathlib import Path
import fitz  # PyMuPDF

CAPTION_RE = re.compile(r"^\s*(?:figure|fig\.?|example)\s*[#]?\s*\d+[^\n]*", re.I)
INVALID_FS_CHARS = re.compile(r'[\\/:*?"<>|]')


def sanitize(name: str) -> str:
    # Normalise weird characters PDFs inject (en/em dash decode failures, NBSP…)
    name = name.replace("\ufffd", "-")      # replacement char → hyphen
    name = name.replace("\u2013", "-")       # en-dash
    name = name.replace("\u2014", "-")       # em-dash
    name = name.replace("\u00a0", " ")       # NBSP
    name = INVALID_FS_CHARS.sub("", name).strip()
    name = re.sub(r"\s+", " ", name)
    name = name.rstrip(".,;: ")
    return name or "untitled"


def find_captions(page):
    """Return [(caption_text, bbox)...] for caption-like lines on the page."""
    out = []
    text_page = page.get_text("dict")
    for block in text_page.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue
            text = "".join(s.get("text", "") for s in spans).strip()
            if not text:
                continue
            if CAPTION_RE.match(text):
                out.append((text, line["bbox"]))
    return out


def nearest_caption(img_bbox, captions):
    """Pick the caption closest to the image. Strongly prefer captions BELOW
    the image (PDFs almost always caption below), falling back to nearest."""
    if not captions:
        return None
    ix0, iy0, ix1, iy1 = img_bbox
    img_bottom = iy1
    img_cx = (ix0 + ix1) / 2

    def score(item):
        text, (cx0, cy0, cx1, cy1) = item
        cap_cx = (cx0 + cx1) / 2
        cap_top = cy0
        vertical = cap_top - img_bottom  # positive if caption below the image
        horizontal = abs(cap_cx - img_cx)
        # Prefer below-and-nearby: penalise above-image captions heavily
        if vertical < -20:  # caption clearly above the image
            return 10_000 + abs(vertical) + horizontal
        return max(vertical, 0) + horizontal * 0.5

    return min(captions, key=score)


def extract(pdf_path: Path, out_dir: Path, min_bytes: int = 2000, keep_unnamed: bool = False):
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    rows = []
    skipped = 0
    used_names = {}
    seen_xrefs = set()        # dedup images referenced on multiple pages
    seen_hashes = set()        # also dedup by content (different xref, same bytes)

    for page_index in range(len(doc)):
        page = doc[page_index]
        captions = find_captions(page)
        for img_info in page.get_image_info(xrefs=True):
            xref = img_info.get("xref")
            bbox = img_info.get("bbox")
            if not xref or not bbox:
                continue
            data = doc.extract_image(xref)
            size = len(data["image"])
            if size < min_bytes:
                skipped += 1
                continue
            if xref in seen_xrefs:
                skipped += 1
                continue
            h = hash(data["image"])
            if h in seen_hashes:
                skipped += 1
                continue
            seen_xrefs.add(xref)
            seen_hashes.add(h)

            cap = nearest_caption(bbox, captions)
            if not cap and not keep_unnamed:
                skipped += 1
                continue
            caption_text = cap[0] if cap else f"page{page_index+1}_unnamed"

            base = sanitize(caption_text)
            n = used_names.get(base, 0) + 1
            used_names[base] = n
            fname_base = base if n == 1 else f"{base} ({n})"

            ext = data.get("ext", "png")
            out_path = out_dir / f"{fname_base}.{ext}"
            out_path.write_bytes(data["image"])
            rows.append((page_index + 1, fname_base, ext, size))

    # Summary
    print(f"\nExtracted {len(rows)} images to {out_dir}  (skipped {skipped} small/duplicate assets)\n")
    print(f"{'Page':<6} {'File':<72} {'Size':>10}")
    print("-" * 90)
    for p, name, ext, size in rows:
        print(f"{p:<6} {name+'.'+ext:<72} {size:>10}")
    return rows


if __name__ == "__main__":
    args = sys.argv[1:]
    min_bytes = 2000
    keep_unnamed = False
    if "--min-bytes" in args:
        i = args.index("--min-bytes")
        min_bytes = int(args[i + 1])
        args = args[:i] + args[i + 2:]
    if "--keep-unnamed" in args:
        keep_unnamed = True
        args.remove("--keep-unnamed")
    if len(args) != 2:
        print("Usage: python extract-pdf-figures.py <pdf> <output-dir> [--min-bytes N] [--keep-unnamed]")
        sys.exit(1)
    extract(Path(args[0]), Path(args[1]), min_bytes=min_bytes, keep_unnamed=keep_unnamed)
