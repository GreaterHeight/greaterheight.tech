# GreaterHeight Technologies — Visual Reconstruction v4

This build establishes the first modern visual system on top of the recovered DNN content.

## Design decisions
- Faithful to the existing GreaterHeight blue/teal visual language, but cleaner and more contemporary.
- Sticky responsive header with simplified information architecture.
- Homepage hero rebuilt without dependency on the unavailable original DNN video URL.
- Common footer rebuilt as static HTML.
- Legacy theme CSS remains temporarily because captured content modules still use its layout classes; it is isolated behind `site-v4.css` and should be progressively retired in the next pass.
- All DNN/WebForms runtime behavior remains excluded from the new shell.

## QA targets for next pass
1. Screenshot comparison at 1440, 1024, 768 and 390px.
2. Remove unused legacy CSS after content templates are converted.
3. Consolidate duplicate URL/page variants.
4. Optimize images and fonts.
5. Complete SEO metadata and redirect map.
