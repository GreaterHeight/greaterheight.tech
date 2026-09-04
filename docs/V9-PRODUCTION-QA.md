# GreaterHeight Technologies — v9 Production QA

Production-candidate hardening based on v8.

- 198 HTML pages retained.
- DNN/WebForms runtime references: 0.
- Local page/asset targets: audited.
- Corrected WHO WE ARE top-level navigation target.
- Added a visible contact enquiry form and current public contact details.
- Added deployment security-header templates (`_headers`, `.htaccess`, `web.config`).
- Added `site.webmanifest`.
- Normalized script boolean attributes and asset references.

## Contact form
The current static implementation uses a `mailto:` fallback. It does not silently claim server-side delivery. For reliable lead capture, replace the action with the approved serverless/API endpoint before launch.
