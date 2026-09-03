# GreaterHeight Technologies — Static Migration v3

## Scope

This pass converts the HTTrack-derived DNN pages into a DNN-independent static site using HTML/CSS/JS.

## Result

- HTML pages: 240
- DNN/WebForms runtime scripts removed from page markup.
- DNN FeedbackForm modules removed because their server-side postback cannot operate on a static site.
- Local links and asset references normalized against the rebuilt file tree.
- Shared `assets/css/site.css` and `assets/js/site.js` provide the static migration layer.
- Responsive navigation and keyboard/back-to-top behavior are implemented in JavaScript.

## Known external content

Two brochure PDFs referenced by the captured Brochure page are not present in the archive's rebuilt file tree. They remain the only unresolved local document references.

## Design policy

The legacy Generic4 visual system remains underneath the migration layer for fidelity. The new layer provides cleanup, accessibility and responsive behavior without imposing a wholesale redesign.
