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

DEFAULT_CAPTION_RE = re.compile(r"^\s*(?:figure|fig\.?|example)\s*[#]?\s*\d+[^\n]*", re.I)
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


def find_captions(page, caption_re):
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
            if caption_re.match(text):
                out.append((text, line["bbox"]))
    return out


def nearest_caption(img_bbox, captions, prefer="below"):
    """Pick the caption closest to the image. `prefer` is "below" (default —
    PDFs normally caption below), "above" (section headings precede figure),
    or "any" (pure distance)."""
    if not captions:
        return None
    ix0, iy0, ix1, iy1 = img_bbox
    img_cx = (ix0 + ix1) / 2

    def score(item):
        _, (cx0, cy0, cx1, cy1) = item
        cap_cx = (cx0 + cx1) / 2
        cap_cy = (cy0 + cy1) / 2
        horizontal = abs(cap_cx - img_cx)
        if prefer == "below":
            vertical = cy0 - iy1               # positive if below image
            if vertical < -20:
                return 10_000 + abs(vertical) + horizontal
            return max(vertical, 0) + horizontal * 0.5
        if prefer == "above":
            vertical = iy0 - cy1               # positive if above image
            if vertical < -20:
                return 10_000 + abs(vertical) + horizontal
            return max(vertical, 0) + horizontal * 0.5
        # "any" — pure distance
        return abs(cap_cy - (iy0 + iy1) / 2) + horizontal * 0.3

    return min(captions, key=score)


def extract(pdf_path: Path, out_dir: Path, min_bytes: int = 2000,
            keep_unnamed: bool = False, min_width: float = 0.0,
            caption_re=DEFAULT_CAPTION_RE, prefer="below"):
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    rows = []
    skipped = 0
    used_names = {}
    seen_xrefs = set()
    seen_hashes = set()

    for page_index in range(len(doc)):
        page = doc[page_index]
        captions = find_captions(page, caption_re)
        for img_info in page.get_image_info(xrefs=True):
            xref = img_info.get("xref")
            bbox = img_info.get("bbox")
            if not xref or not bbox:
                continue
            bx0, by0, bx1, by1 = bbox
            if (bx1 - bx0) < min_width:
                skipped += 1
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

            cap = nearest_caption(bbox, captions, prefer=prefer)
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
    min_width = 0.0
    caption_re = DEFAULT_CAPTION_RE
    keep_unnamed = False

    def take(flags, cast):
        for flag in flags:
            if flag in args:
                i = args.index(flag)
                v = cast(args[i + 1])
                del args[i:i+2]
                return v
        return None

    v = take(["--min-bytes"], int)
    if v is not None: min_bytes = v
    v = take(["--min-width"], float)
    if v is not None: min_width = v
    v = take(["--caption-regex"], str)
    if v is not None: caption_re = re.compile(v, re.I)
    prefer = "below"
    for p in ("--caption-above", "--caption-below", "--caption-any"):
        if p in args:
            prefer = p.split("-")[-1]
            args.remove(p)
    if "--keep-unnamed" in args:
        keep_unnamed = True
        args.remove("--keep-unnamed")

    if len(args) != 2:
        print("Usage: python extract-pdf-figures.py <pdf> <output-dir> "
              "[--min-bytes N] [--min-width W] [--caption-regex RE] "
              "[--caption-above|--caption-below|--caption-any] [--keep-unnamed]")
        sys.exit(1)
    extract(Path(args[0]), Path(args[1]),
            min_bytes=min_bytes, min_width=min_width,
            keep_unnamed=keep_unnamed, caption_re=caption_re, prefer=prefer)
