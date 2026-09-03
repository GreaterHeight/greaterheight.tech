# GreaterHeight Technologies — Static Rebuild v5

## Architecture

- Static HTML pages, no DNN/WebForms runtime.
- Shared `assets/css/site-v5.css` presentation layer.
- Shared `assets/js/site-v5.js` navigation/accessibility layer.
- Original visual/content assets retained under `assets/images` and `assets/fonts`.
- Legacy DNN theme CSS/JS is no longer loaded by production pages.
- Homepage content was restored from the original HTTrack capture because an earlier migration pass had accidentally omitted the main homepage banner/content section.
- Common header, footer, page hero and CTA are generated consistently across pages.
- `robots.txt` and `sitemap.xml` included.

## QA

The accompanying `V5-MIGRATION-AUDIT.json` records the generated page count, legacy-runtime hits and local-reference audit.
