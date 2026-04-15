# The Truth Base of iGUIDE

A portable, searchable knowledge base for iGUIDE drafting documentation.
Stop guessing — search, read, and verify.

**55 documents · 14 shelves · 246,000+ words of verified iGUIDE content.**

## Live site

Deployed via GitHub Pages — see the **Environments → github-pages** deployment
on the repo sidebar for the live URL.

## Stack

- **Zero backend.** Two static HTML files (`index.html` landing, `search.html`
  app) with the full 55-document database embedded inline.
- **`data-patch.js`** — supplements the embedded DB with full content for
  documents that were truncated during initial extraction.
- **`serve.py`** — tiny Python 3 static server with pretty routes
  (`/`, `/search`, `/doc/<id>`, `/shelf/<name>`, `/q/<term>`).

## Features

- Full-text search across every document with excerpt highlighting
- Shelf → Book → Page sidebar tree navigation (collapsible, mobile-friendly)
- URL routing — `#/doc/5`, `#/shelf/Stairs`, `#/q/fireplace` are shareable
- Keyboard shortcuts — `/` focus search, `↑`/`↓` navigate results, `Enter` open,
  `←`/`→` prev/next doc inside reader, `Esc` close
- Clean reader view with proper headings, lists, notes, figure captions, and
  inline images that match each caption by name
- Lightbox for full-size image viewing
- Light theme matching Metric Planitar (slate + blue) with Colombian flag
  gradient header

## Local development

Requires Python 3. No Node or build step needed for the app itself.

```bash
python serve.py 8080
# then open http://localhost:8080
```

Or on Windows, double-click `start.bat`.

### Regenerating the content patch

When you update source markdowns in `bookstack-export/truth-base-export/`:

```bash
node build-patch.js
```

This regenerates `data-patch.js` with the full content of the listed documents.

### Adding images to a document

1. Drop the files into `img/<folder>/` named exactly like the caption
   (e.g. `Figure 3 - Scan Options Context Menu.png`)
2. Add the paths to the appropriate `DOC_IMAGES[id]` array in `search.html`
3. Reload — the matcher pairs captions to images automatically

## Structure

```
├── index.html                    # Landing
├── search.html                   # Search app (embedded DB + formatter)
├── data-patch.js                 # Full content for docs truncated in the embedded DB
├── build-patch.js                # Regenerator for data-patch.js
├── serve.py                      # Zero-dep Python static server with pretty routes
├── start.bat                     # Windows launcher
├── img/                          # Figure images organized by doc
└── bookstack-export/             # Source markdowns (for patch regeneration)
```
