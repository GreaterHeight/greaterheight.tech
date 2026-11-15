# Image Generation Prompts — GreaterHeight Tech

This file documents AI image generation prompts for every image placeholder currently on the site.
When an image is generated and placed at the documented path, it will automatically display on the page — no code changes needed.

**Brand colours for reference:**
- Forest green: `#0D3D28`
- Teal: `#005A3C`
- Teal glow (accent): `#1EB496`
- Mint: `#97EFC9`
- Crimson: `#8C0D0C`

---

## Analytics & BI Page
**Page:** `/what-we-do/data/analytics-bi/`

### `/assets/images/analytics/unlock-insights.jpg`
**Purpose:** Mid-page CTA banner, right column — full-height atmospheric visual. Displays inside a dark forest-green band.

**Prompt:**
> A modern data operations centre at night — wide-angle photo. Multiple large curved monitors display vibrant teal and green data dashboards, bar charts, and real-time analytics graphs. Soft ambient lighting in deep green and teal tones reflects off a glass desk surface. No people visible. The scene should feel calm, powerful, and technologically sophisticated. The left side of the image should be slightly darker/more shadowed to blend into a dark forest-green background panel. Shot with cinematic depth of field. No text overlays. Colour palette: deep forest green, teal, mint green, with subtle gold accents.

**Dimensions:** 480 × 500 px minimum, 2:3 portrait ratio
**Placement:** `what-we-do/data/analytics-bi/index.html` — `.unlock-img` div, right of "Unlock Better Business Insights" CTA

---

### `/assets/images/analytics/data-strategy-expert.jpg`
**Purpose:** "Evaluate Your Data Strategy" CTA section, right column. Person/expert image.

**Prompt:**
> A professional African data analyst or consultant — mid-shot portrait, natural office setting. The subject is seated at a modern workstation with a large monitor showing colourful analytics dashboards behind them. They are dressed in smart-casual business attire (dark top or shirt), looking slightly off-camera with a confident, thoughtful expression. Warm natural lighting from the left, slight bokeh on the background monitors. Photo should feel approachable and credible — not overly staged. No heavy colour grading. The subject's right side of the frame should be slightly open/lighter to blend into the section's dark background. Colour palette: natural skin tones, teal and green monitor glow, dark background.

**Dimensions:** 400 × 400 px minimum, 1:1 to 2:3 ratio
**Placement:** `what-we-do/data/analytics-bi/index.html` — `.evaluate-img` div, right of "Evaluate Your Data Strategy" CTA

---

### `/assets/images/analytics/media-analytics.jpg`
**Purpose:** Industry card — Media & Entertainment. Used as a full-bleed background image inside an industry card with a dark overlay.

**Prompt:**
> An aerial view of a modern broadcast studio or streaming production control room — overhead or dramatic angle. Multiple screens show video feeds, waveform graphics, and content dashboards. Rich purple, blue, and teal ambient lighting. Cinematic and high-contrast. The image should work as a full-bleed background with a dark gradient overlay applied from top. No people required. Mood: creative industry, high-tech production. Colour palette: deep blue, teal, purple with bright screen glows.

**Dimensions:** 400 × 500 px minimum, portrait orientation
**Placement:** `what-we-do/data/analytics-bi/index.html` — Industries We Serve grid, Media & Entertainment card

---

## Existing Industry Images (already placed — no action needed)

The following images are already in `/assets/images/industries/` and are live on the Analytics page:

| File | Industry Card |
|------|--------------|
| `fintech.jpg` | Financial Technology |
| `healthcare.jpg` | Healthcare |
| `e-commerce.jpg` | Retail & eCommerce |
| `logistics.jpg` | Logistics |
| `education.jpg` | Education |
| `banking.jpg` | Banking |
| `enterprise.jpg` | Enterprise |

---

## Hero Visuals (other pages — reference)

> These are from earlier page builds. Document here for completeness.

### `/assets/images/hero/analytics-hero.jpg` *(optional upgrade)*
**Page:** `/what-we-do/data/analytics-bi/`
**Prompt (if needed for a full-bleed hero variant):**
> A top-down overhead shot of a large conference table in a modern corporate meeting room. Several laptops are open showing data dashboards and analytics charts. Physical printed reports, sticky notes, and coffee cups scattered. Colour-graded to teal and forest green tones. Shot with shallow depth of field — sharp centre, soft edges. Mood: collaborative business intelligence session. No visible faces.

---

## Notes for Image Generation

- Use tools such as Midjourney, DALL-E 3, Adobe Firefly, or Stable Diffusion
- After generating, optimise images: convert to `.jpg`, compress to under 200KB for card images, under 400KB for hero/banner images
- Recommended tool for compression: `imagemin`, `squoosh.app`, or `tinypng.com`
- File naming: lowercase, hyphens only, no spaces
- After placing an image, do a hard refresh (`Ctrl+Shift+R`) to bypass browser cache and confirm display

---

*Last updated: 2026-11-15*
