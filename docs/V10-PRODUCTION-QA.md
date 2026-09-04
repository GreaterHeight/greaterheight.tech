# GreaterHeight Technologies — v10 Production QA

## Purpose
v10 is a targeted production QA pass on v9. It does not replace the recovered content set.

## Corrections
- Converted same-domain absolute navigation/resource URLs to relative paths so the static package remains self-contained when deployed under another hostname or subpath.
- Kept canonical, Open Graph and social metadata URLs absolute.
- Rebuilt the static contact-form submit behavior so it opens a prefilled email draft to sales@greaterheight.tech instead of suppressing the submit with no action.
- Renamed the production stylesheet/script to site-v10.css and site-v10.js.

## Verification
- All local HTML/resource references resolve inside the package.
- No WebForms runtime fields detected.
- No DNN module/runtime references detected.
