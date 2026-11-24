# Image Generation Prompts — GreaterHeight Tech

This file documents AI image generation prompts for every image placeholder currently on the site.
When an image is generated and placed at the documented path, it will automatically display on the page — no code changes needed.

---

## Global Brand Colour Reference

These colours apply to **every image on the site**. Where the scene allows — office branding, clothing accents, screen glows, plants, furniture, background detail — the palette should appear naturally. Never force them unnaturally; use them wherever a real-world scene would have an accent or brand detail.

| Name | Hex | Use in photography |
|---|---|---|
| Forest green | `#0D3D28` | Dark office backgrounds, jacket/blazer, furniture, branded panels |
| Teal | `#005A3C` | Office plants, clothing accents (tie, pocket square), furniture |
| Teal glow | `#1EB496` | Screen glows, monitor ambient light, accent details |
| Mint | `#97EFC9` | Soft background elements, screen highlights, light fabric accents |
| Crimson | `#8C0D0C` | Bold accent: tie, pocket square, branded signage (use sparingly) |

---

## Analytics & BI Page
**Page:** `/what-we-do/data/analytics-bi/`

### `/assets/images/analytics/unlock-insights.jpg`
**Purpose:** Mid-page CTA banner, right column — full-height atmospheric visual. Displays inside a dark forest-green band.

**Prompt:**
> A modern data operations centre at night — wide-angle photo. Multiple large curved monitors display vibrant teal and green data dashboards, bar charts, and real-time analytics graphs. Soft ambient lighting in deep forest green (`#0D3D28`) and teal (`#005A3C`) tones reflects off a glass desk surface. No people visible. The scene should feel calm, powerful, and technologically sophisticated. The left side of the image should be slightly darker/more shadowed to blend into a dark forest-green background panel. No text overlays. Colour palette: deep forest green, teal glow (`#1EB496`), mint green, with subtle gold accents.

**Dimensions:** 480 × 500 px minimum, 2:3 portrait ratio
**Placement:** `what-we-do/data/analytics-bi/index.html` — `.unlock-img` div, right of "Unlock Better Business Insights" CTA

---

### `/assets/images/analytics/data-strategy-expert.jpg`
**Purpose:** "Evaluate Your Data Strategy" CTA section, right column. Person/expert image.

**Prompt:**
> A professional African data analyst or consultant — mid-shot portrait, natural office setting. The subject is seated at a modern workstation with a large monitor showing colourful analytics dashboards behind them. They are dressed in smart-casual business attire (dark top or shirt), looking slightly off-camera with a confident, thoughtful expression. Warm natural lighting from the left, slight bokeh on the background monitors. Photo should feel approachable and credible — not overly staged. No heavy colour grading. The subject's right side of the frame should be slightly open/lighter to blend into the section's dark background. Colour palette: natural skin tones, teal glow (`#1EB496`) and forest green (`#0D3D28`) monitor ambient light, dark background.

**Dimensions:** 400 × 400 px minimum, 1:1 to 2:3 ratio
**Placement:** `what-we-do/data/analytics-bi/index.html` — `.evaluate-img` div, right of "Evaluate Your Data Strategy" CTA

---

### `/assets/images/analytics/media-analytics.jpg`
**Purpose:** Industry card — Media & Entertainment. Used as a full-bleed background image inside an industry card with a dark overlay.

**Prompt:**
> An aerial view of a modern broadcast studio or streaming production control room — overhead or dramatic angle. Multiple screens show video feeds, waveform graphics, and content dashboards. Rich teal (`#005A3C`) and teal glow (`#1EB496`) ambient lighting with deep forest green (`#0D3D28`) in the shadows. Cinematic and high-contrast. The image should work as a full-bleed background with a dark gradient overlay applied from top. No people required. Mood: creative industry, high-tech production.

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
> A top-down overhead shot of a large conference table in a modern corporate meeting room. Several laptops are open showing data dashboards and analytics charts. Physical printed reports, sticky notes, and coffee cups scattered. Colour palette: forest green (`#0D3D28`) and teal glow (`#1EB496`) screen tones. Shot with shallow depth of field — sharp centre, soft edges. Mood: collaborative business intelligence session. No visible faces.

---

## Notes for Image Generation

- Use tools such as Midjourney, DALL-E 3, Adobe Firefly, or Stable Diffusion
- After generating, optimise images: convert to `.jpg`, compress to under 200KB for card images, under 400KB for hero/banner images
- Recommended tool for compression: `imagemin`, `squoosh.app`, or `tinypng.com`
- File naming: lowercase, hyphens only, no spaces
- After placing an image, do a hard refresh (`Ctrl+Shift+R`) to bypass browser cache and confirm display

---

## Digital Reputation Page
**Page:** `/what-we-do/marketing/reputation/`

All prompts must look like **professional editorial photography** — no dramatic compositing, no cinematic colour grading, no overlay effects. Natural lighting, real environments, real people. Think high-end business magazine or agency website photography.

Brand colours should appear as **environmental accents** — office plants in teal or forest green, monitor screen glows in teal glow/mint, branded office panels or signage, clothing accents (pocket square, tie) in crimson or teal. Never applied as a colour wash or filter.

---

### `/assets/images/reputation/hero-bg.jpg`
**Purpose:** Full-bleed hero background. Displays behind dark forest-green overlay on the page hero.

**Prompt:**
> Wide-angle editorial photograph of a modern open-plan office in Lagos or a major African city. Floor-to-ceiling windows with natural daylight. A team of professionally dressed Black professionals gathered around a glass-topped conference table, some seated and some standing, engaged in a focused working discussion — laptops, notebooks, printed documents visible. Shot from across the room at table height. Real ambient office light, no flash. Warm and confident atmosphere. No text overlays. Office branding details in teal (`#005A3C`) and forest green (`#0D3D28`) — a branded wall panel, a plant, or upholstered furniture. The right side of the image should have more open space and lighter exposure for text overlay contrast.

**Dimensions:** 1600 × 900 px minimum, 16:9 landscape
**Placement:** `.rep-hero` section — full-bleed background image with dark overlay

---

### `/assets/images/reputation/pr-search.jpg`
**Purpose:** Right column of "We Connect PR With Search" dark section.

**Prompt:**
> Editorial photograph of a Black professional woman in her mid-30s, seated at a well-lit contemporary desk, reviewing content on a large external monitor. She is dressed in smart business casual — blazer in deep navy or dark forest green (`#0D3D28`), natural hair styled up. The monitor clearly shows a web browser with search results pages open, with a subtle teal glow (`#1EB496`) from the screen. Beside her: a printed press release, a notepad, and a pen. Shot from a 45-degree angle, shallow depth of field, background softly blurred. Natural window light from the left. No dramatic effects. The image should feel precise and intelligent, not staged. No text on screen legible.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** `.pr-search-img` div — right of the PR + Search two-column dark section

---

### `/assets/images/reputation/service-insight.jpg`
**Purpose:** Service card image — Insight & Clarity card.

**Prompt:**
> Editorial photograph of a Black professional in their early 40s seated at a desk, looking at a large monitor showing a web browser with Google search results for a company or personal name — multiple listings, news articles, and a knowledge panel visible on screen, with a soft teal glow (`#1EB496`) from the monitor. Their expression is analytical and focused. A printed brand audit document and pen sit beside the keyboard. Bright, clean, modern office. A small plant with deep green foliage (`#0D3D28`) sits at the edge of the desk. Natural daylight. Shot at mid-distance from a 45-degree angle. No text on screen legible. No colour overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Insight & Clarity card

---

### `/assets/images/reputation/service-digital-rep.jpg`
**Purpose:** Service card image — Digital Reputation Management (SERP).

**Prompt:**
> Editorial photograph of a Black professional man in a sharp navy suit, seated at a modern desk, reviewing a laptop screen clearly showing a Google search results page. He leans slightly forward, one hand on the trackpad, expression concentrated. The SERP layout on screen is recognisable but no text is legible; a subtle teal glow (`#1EB496`) reflects off his face from the screen. Bright office interior with large windows. A teal (`#005A3C`) branded folder or document holder sits beside the laptop. Natural light. Shot from a 45-degree front angle, chest to screen in frame. Clean, authoritative feel.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Digital Reputation Management card

---

### `/assets/images/reputation/service-pr-media.jpg`
**Purpose:** Service card image — PR & Media Relations card.

**Prompt:**
> Editorial photograph of a confident Black professional woman in her 40s, seated and speaking in a formal television or podcast interview setting. A broadcast microphone is held toward her from one side; a camera and tripod are softly visible in the background out of focus. She is dressed in a formal blazer — deep forest green (`#0D3D28`) or dark navy — expression composed and articulate, mid-sentence. Warm studio or office lighting — natural, not dramatic. A crimson (`#8C0D0C`) branded banner or branded set detail is softly visible in the background. Shot from a slight angle at conversational height. The environment reads as a professional media production, not a press conference. No text overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the PR & Media Relations card

---

### `/assets/images/reputation/service-review.jpg`
**Purpose:** Service card image — Review & Rating Management card.

**Prompt:**
> Editorial photograph of a business owner — Black woman in her 30s — seated at a café counter or small business desk, holding a smartphone showing a 5-star Google Business review page. She reads the screen with a composed, satisfied expression. The star rating and card layout of a review platform are clearly visible but no text is legible. The background is a warm, blurred interior with teal (`#005A3C`) or mint (`#97EFC9`) accent details — a wall colour, plant, or upholstery. Natural ambient light. Phone in sharp focus. Shot at a mid-angle. No colour overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Review & Rating Management card

---

### `/assets/images/reputation/service-crisis.jpg`
**Purpose:** Service card image — Crisis Management card.

**Prompt:**
> Editorial photograph of a small team of two or three Black professionals in a modern open office or glass-walled war room, gathered urgently around a laptop. One person stands and types, two others lean in — all focused on the screen, which emits a teal glow (`#1EB496`). A mobile phone on the table displays a notification alert. Printed documents are scattered across the desk. Expression: controlled urgency, not panic. Business formal attire — one person with a crimson (`#8C0D0C`) tie or pocket square. Shot from just outside, looking in through the glass — environment slightly blurred in foreground, team sharp. Bright, clinical office lighting. No text legible on screens. No dramatic colour.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Crisis Management card

---

### `/assets/images/reputation/service-thought-leadership.jpg`
**Purpose:** Service card image — Thought Leadership card.

**Prompt:**
> Editorial photograph of a confident Black professional man in his 50s, speaking at a corporate panel or business conference stage. He sits at a panel table with a microphone in front of him, hands expressive mid-gesture, audience of business professionals visible and softly out of focus behind him. Conference room or hotel ballroom setting — a branded banner or screen in the background in forest green (`#0D3D28`) or teal, not readable. Dark suit with a crimson (`#8C0D0C`) pocket square. Stage or overhead lighting — clean, bright, not dramatic. Shot from the front at a slight low angle. Authoritative, commanding presence.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Thought Leadership card

---

### `/assets/images/reputation/service-social-pr.jpg`
**Purpose:** Service card image — Social Media PR & Marketing card.

**Prompt:**
> Editorial photograph of a Black professional woman in her late 20s or early 30s at a bright, modern workspace. She sits in front of a large monitor showing a social media content calendar or scheduling tool — grid of posts, analytics figures visible but not legible, with a soft teal glow (`#1EB496`) from the screen. A smartphone on a small ring-light stand is propped beside the desk, suggesting content creation. She wears a mint or teal accent top (`#97EFC9`, `#005A3C`) under a blazer. Co-working space or agency office interior with a forest green (`#0D3D28`) wall panel or plant in the background. Natural light from large windows. Shot from a 45-degree front angle. No text readable on screens.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Social Media PR & Marketing card

---

### `/assets/images/reputation/service-entrepreneur.jpg`
**Purpose:** Service card image — For Entrepreneurs / Personal Brand card.

**Prompt:**
> Editorial portrait photograph of a confident Black male entrepreneur in his mid-30s to early 40s. He stands in a sleek, modern office interior — glass, steel, and lush green plants (`#0D3D28`) in the background, softly out of focus. He faces the camera with composed, direct eye contact. Smart-casual attire: fitted blazer over a clean open-collar shirt, no tie; a teal (`#005A3C`) or forest green pocket square as the single accent. Arms relaxed at sides or one hand in a pocket. Shot from mid-chest to just above the head. Natural light from a large window to one side. The expression reads as founder-energy — assured, forward-thinking. No colour overlays. No props in hands.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the For Entrepreneurs / Personal Brand card

---

### `/assets/images/reputation/service-google-ai.jpg`
**Purpose:** Service card image — Google & AI Visibility card.

**Prompt:**
> Editorial photograph of a well-dressed Black professional man in his late 30s — charcoal or medium-grey suit, white shirt, no tie — seated at a modern desk, working on a laptop. The screen clearly shows a Google search results page with a name or brand prominently at the top alongside an AI overview panel; a subtle teal glow (`#1EB496`) reflects off his face and desk surface from the screen. He leans slightly forward, one hand on the keyboard, reading attentively. Bright, airy corporate office with floor-to-ceiling windows. A forest green (`#0D3D28`) plant or branded office panel is visible in the background, softly blurred. Natural daylight. Shot from a 45-degree front angle. No text on screen legible. No colour overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Google & AI Visibility card

---

### `/assets/images/reputation/service-exec-visibility.jpg`
**Purpose:** Service card image — Founder & Executive Visibility card.

**Prompt:**
> Editorial photograph of a distinguished Black executive man in his 50s — dark suit, white shirt, crimson (`#8C0D0C`) silk tie — seated in a formal interview chair in a warmly lit studio or high-end office interior. A professional TV camera on a tripod is clearly visible in the foreground, partially in frame, suggesting he is being filmed or profiled. He speaks animatedly with composed authority, hands lightly gesturing. A bookcase or executive interior in deep forest green (`#0D3D28`) tones sits in the soft background. Warm, premium lighting — think broadcast interview segment on a business news channel. Shot from a 45-degree angle at conversational height. No text overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Founder & Executive Visibility card

---

### `/assets/images/reputation/service-event-pr.jpg`
**Purpose:** Service card image — Event PR & TV Coverage card.

**Prompt:**
> Editorial photograph of a busy corporate event — a business leadership forum, product launch, or conference — with a large crowd of Black professionals in business attire networking and conversing. In the foreground or midground, a TV camera crew (operator and boom) is filming the event. A branded conference banner or screen is visible in the background in forest green (`#0D3D28`) and teal (`#005A3C`) — the GreaterHeight brand palette — not legible but colourful. Event lighting — overhead, warm, professional. Shot at mid-height from within or at the edge of the crowd, capturing the scale and energy. No staged poses — everyone in genuine motion. No colour overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Event PR & TV Coverage card

---

### `/assets/images/reputation/service-knowledge-panel.jpg`
**Purpose:** Service card image — Google Knowledge Panel card.

**Prompt:**
> Editorial photograph of a Black professional woman in her 30s, seated at a bright, modern desk in front of a large monitor showing a Google Knowledge Panel — the sidebar box that appears in search results for a named person or organisation, showing a photo, title, description, and social links; a soft teal glow (`#1EB496`) illuminates the scene from the screen. She points at or taps the screen with one finger, reviewing the panel with a focused, satisfied expression. Clean office environment with a small teal or forest green (`#005A3C`) potted plant on the desk. Natural window light. Shot from a 45-degree angle. Screen content clearly shows a knowledge panel layout but no text is legible. No colour overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.service-card-img` for the Google Knowledge Panel card

---

### `/assets/images/reputation/case-study-featured.jpg`
**Purpose:** Featured case study card — left image column.

**Prompt:**
> Editorial photograph of a confident Black Nigerian professional man in his late 30s — dressed in a sharp fitted blazer and collared shirt with a teal (`#005A3C`) or forest green pocket square — standing in front of a modern floor-to-ceiling glass office window with a Lagos cityscape visible behind him. He looks toward camera, expression composed and assured. Shot at three-quarter length. Natural daylight from the window behind him gives a mild rim effect. Clean, professional, executive feel. The left and right thirds of the image have slightly darker exposure for text blending. No text overlays.

**Dimensions:** 800 × 700 px minimum, portrait or square orientation
**Placement:** `.work-card-img` div — left half of the featured case study card

---

### `/assets/images/reputation/insight-seo-vs-orm.jpg`
**Purpose:** Blog/article card image — SEO vs Reputation Management article.

**Prompt:**
> Editorial flat-lay photograph on a white or light grey desk surface: a laptop showing a web browser open to a search results page (no legible text, screen emits a subtle teal glow `#1EB496`), a printed document labelled with something resembling "Brand Audit" (not legible), a pen, a small plant with deep forest green foliage (`#0D3D28`), and a coffee mug. Shot directly from above. Clean, contemporary workspace aesthetic. Natural daylight. Colour palette: whites, light greys, with teal and mint green accents (`#005A3C`, `#97EFC9`) from the plant and pen. No colour overlays.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.insight-card-img` for the SEO vs ORM article card

---

### `/assets/images/reputation/insight-google-business.jpg`
**Purpose:** Blog/article card image — How to Delete a Fake Google Review article.

**Prompt:**
> Editorial photograph of a person's hands holding a smartphone in both hands, with the screen clearly showing a 5-star review interface (like Google Maps or Google Business). The screen is bright and in sharp focus with a soft teal glow (`#1EB496`). Background is a blurred café or office interior in warm, natural tones with teal or mint (`#97EFC9`) accent details — a wall colour or plant. Shot at mid-distance, hands and phone fully in frame. No text on screen legible. No colour filters. Contemporary, clean.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.insight-card-img` for the Google review article card

---

### `/assets/images/reputation/insight-personal-brand.jpg`
**Purpose:** Blog/article card image — Personal Branding for Nigerian CEOs article.

**Prompt:**
> Editorial portrait photograph of a Black Nigerian man in his mid-40s dressed in a sharply tailored dark navy or charcoal wool suit — the cut precise and expensive, as worn by a Fortune 500 CEO: notch lapels, pocket square in white linen or teal (`#005A3C`), white barrel-cuff shirt, no tie. He stands or sits slightly turned toward camera with composed, direct eye contact. Expression is quietly authoritative — not smiling, not severe. Shot in a premium executive environment: a glass-walled boardroom, a hotel lobby with marble finishes, or a sleek high-rise office interior. Background is clean and professional, softly out of focus — a large forest green (`#0D3D28`) plant or upholstered panel visible in the background. Lighting is natural and slightly directional — one large window to the side. No studio backdrops, no dramatic shadows, no colour overlays. The image should read as a Financial Times or Bloomberg Businessweek cover portrait — global executive register, West African identity.

**Dimensions:** 600 × 400 px minimum, 3:2 landscape
**Placement:** `.insight-card-img` for the Nigerian CEO personal brand article card

---

*Last updated: 2026-11-24*
