# GreaterHeight Technologies — Static Website Rebuild

This package is a clean HTML/CSS/JS reconstruction of the captured GreaterHeight Technologies website. It removes the DNN/WebForms runtime from the production pages while preserving the recovered page inventory and local assets.

## Structure
- `*.html` — static pages, with legacy page filenames retained where practical
- `assets/css/site-v10.css` — shared presentation layer
- `assets/js/site-v10.js` — navigation, interactions and contact-form mailto fallback
- `assets/images/` — recovered and organized image assets
- `assets/fonts/` — local fonts
- `assets/documents/` — retained public documents
- `docs/URL-MIGRATION-MAP.csv` — page-by-page migration inventory
- `robots.txt`, `sitemap.xml`, `site.webmanifest` — deployment/SEO support
- `.htaccess` — Apache deployment rules
- `web.config` — IIS deployment rules
- `_headers` — static-host security headers (e.g. Netlify/Cloudflare Pages style hosts)

## Deployment
Upload the **contents of this directory** to the website document root. Do not upload the parent ZIP directory as an additional URL segment unless that is intentional.

Recommended smoke tests after deployment:
1. `/index.html` (or `/` if the server maps it to the index file)
2. `/Where-We-Are.html`
3. one nested page under `/What-We-Do/`
4. one nested page under `/How-We-Do-It/`
5. `/assets/css/site-v10.css`
6. `/assets/js/site-v10.js`

The contact form is intentionally a client-side **mailto draft** rather than a fake server submission. It opens an email draft addressed to `sales@greaterheight.tech` with the visitor's entered details.

## Important launch note
The archive contains multiple historical/duplicate-looking URLs. They have been retained to reduce the risk of breaking inbound links. Before a production cutover, use `docs/URL-MIGRATION-MAP.csv` to decide which historical URLs should remain, redirect, or receive a search-engine `noindex` directive.

## QA status
The latest structural audit found:
- 198 HTML pages
- 0 missing local page/resource targets
- 0 DNN/WebForms runtime markers in production HTML
- 0 pages with incorrect H1 counts

Browser-rendered visual QA could not be completed in the build environment because its browser execution was blocked by the environment. Visual review should therefore be performed on the deployed staging URL before cutover.
