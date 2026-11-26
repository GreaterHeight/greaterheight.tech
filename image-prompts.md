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

### `/assets/images/reputation/audience-featured.jpg`
**Purpose:** Background image for the "Our Core Client Profile" featured card inside the Who We Serve section. Displays behind a dark gradient overlay — the image must read clearly through a semi-transparent forest-green and crimson colour wash, so it needs strong natural light, clear human presence, and an uncluttered mid-ground. Wider, landscape orientation so the composition fills the card at different viewport widths.

**Prompt:**
> Wide editorial photograph of a high-rise executive boardroom in Nigeria — Abuja or Lagos — with a panoramic view of the city and a prominent rock formation (Zuma Rock or Aso Rock) through floor-to-ceiling glass windows. The room is bright with natural daylight. Six Black Nigerian professionals of mixed ages and genders are arranged around a wide conference table: two standing on the left side — a woman in her 30s in a fitted navy blazer holding a notebook, and a distinguished older man in his 60s in a charcoal suit with a subtle crimson pocket square — and four seated at the table: a younger woman in a coloured blazer speaking expressively with hands in motion, a young man in glasses leaning forward with a tablet, a woman in a black top with pearl earrings taking notes, and a senior man in a dark suit at the right end. All are engaged in a focused working discussion. The table has glasses of water, printed documents, and open notebooks. On the wall, a modern abstract artwork with teal (`#005A3C`) and ochre tones. Office plants with deep forest green foliage (`#0D3D28`) in the background. Shot at mid-height from across the room, capturing the full table and all six people. Natural ambient light, no artificial flash. The image should feel premium, boardroom-level, West African executive register — not a stock-photo cliché. Colour palette: natural daylight, forest green and teal environmental accents, warm wood table surface.

**Dimensions:** 1200 × 600 px minimum, 2:1 wide landscape ratio
**Placement:** `.audience-featured` div — background image with dark gradient overlay. Text (eyebrow, h3, paragraph) is overlaid on top.

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

---

## Digital Reputation Services Page

> These images are for the alternating-layout service detail page at `/what-we-do/marketing/digital-reputation-services/`. Each image occupies a full-bleed panel alongside a service description block. All shots must be professional editorial photography — no cinematic colour grades, no overlay washes, no dramatic composite lighting. Brand colours appear as environmental accents only (plant foliage, screen glows, clothing accents, office panels).

---

### `/assets/images/digital-rep-services/svc-insight.jpg`
**Purpose:** Service panel image — Insight & Clarity (Foundation service).

**Prompt:**
> Editorial photograph of a Black Nigerian professional — a woman or man in their late 30s — seated at a large monitor in a modern open-plan office. The screen shows a data dashboard with charts, graphs, and a search results page representing a digital audit. The professional leans slightly forward, one elbow on the desk, reviewing the content with focused attention. The office background is contemporary — glass partitions, timber accents, a large forest green (`#0D3D28`) wall panel or plant visible. Screen glow is the dominant light source, with natural daylight from a window to the side. Clothing is business-casual smart. No colour filters. Shot at eye level, mid-distance. The image should read as a consulting professional examining a client's digital footprint for the first time.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Insight & Clarity section

---

### `/assets/images/digital-rep-services/svc-digital-rep.jpg`
**Purpose:** Service panel image — Digital Reputation Management (Search service).

**Prompt:**
> Editorial photograph of a Black Nigerian professional in a smart business suit seated in front of two large monitors. One screen shows a Google search results page with a prominent positive listing at the top. The other screen shows a content management or SEO analytics dashboard. The professional is typing or gesturing at the screen. Office is modern and clean — large windows, one teal (`#005A3C`) accent wall or upholstered panel in the background. Warm directional natural light. No colour overlays. Shot at mid-distance, the screens legible but not perfectly sharp. Conveys control, strategy, and digital expertise.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Digital Reputation Management section

---

### `/assets/images/digital-rep-services/svc-pr-media.jpg`
**Purpose:** Service panel image — PR & Media Relations (Earned Media service).

**Prompt:**
> Editorial photograph of a Black Nigerian communications professional — a man or woman in their early 40s in professional attire — being interviewed by a journalist or media anchor. The setting is a television studio green room, a media centre lobby, or a branded press background. A microphone or small lapel mic is visible. The professional speaks with composed authority, making eye contact with the interviewer. Studio lights are soft and directional. Background shows teal (`#1EB496`) or forest green (`#0D3D28`) in the branded backdrop or a lush interior plant. No colour filters. Conveys earned media authority, executive visibility, and professional credibility.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for PR & Media Relations section

---

### `/assets/images/digital-rep-services/svc-review.jpg`
**Purpose:** Service panel image — Review & Rating Management (Reviews service).

**Prompt:**
> Editorial photograph of a Black Nigerian professional at a desk, looking at a laptop screen showing a review management interface — star ratings, response fields, and review platform logos. The professional holds a stylus or pen and appears to be crafting a response with care. The desk is tidy and professional — a small mint (`#97EFC9`) plant or teal pen holder as the only colour accent. Office background is neutral and calm — white walls, natural daylight. Shot at mid-close distance, the screen visible but not perfectly legible. No colour filters or overlays. Conveys careful, professional engagement with public customer feedback.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Review & Rating Management section

---

### `/assets/images/digital-rep-services/svc-crisis.jpg`
**Purpose:** Service panel image — Crisis Management (Crisis service).

**Prompt:**
> Editorial photograph of a small team of Black Nigerian professionals — three people — seated around a conference table in an urgent but controlled working session. Laptops are open, one large screen on the wall shows a news monitoring or social media alert dashboard. The atmosphere is focused and calm — these are experienced people managing a situation, not panicking. One person is on a phone call while the others review content on a shared screen. Conference room is sleek and modern — forest green (`#0D3D28`) accent wall or dark upholstered chairs. Overhead lighting is sharp and professional. No colour filters. Shot at mid-distance. Conveys coordinated crisis response, professionalism under pressure, and strategic communication.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Crisis Management section

---

### `/assets/images/digital-rep-services/svc-thought-leadership.jpg`
**Purpose:** Service panel image — Thought Leadership (Authority service).

**Prompt:**
> Editorial photograph of a Black Nigerian thought leader — a man in his late 40s or early 50s — standing at a podium or speaking at a small executive conference. The audience is partially visible in the foreground — attentive, professional. The speaker gestures with quiet confidence, speaking from notes or directly to the audience. The stage or speaking environment is clean and modern — a teal (`#1EB496`) or forest green (`#0D3D28`) branded banner or backdrop behind the speaker. Lighting is warm and directional — stage lighting without dramatic spot effects. Shot from a low or mid angle looking slightly up at the speaker. No colour filters. Conveys intellectual authority, executive gravitas, and confident public presence.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Thought Leadership section

---

### `/assets/images/digital-rep-services/svc-social-pr.jpg`
**Purpose:** Service panel image — Social Media PR & Marketing (Social service).

**Prompt:**
> Editorial photograph of a Black Nigerian digital marketing professional — a woman in her late 20s or early 30s — seated at a standing desk or creative workstation, managing multiple social media feeds visible across a large monitor and a tablet. The screens show LinkedIn, Instagram, or Twitter/X dashboards with active content and notifications. The office is modern and bright — large windows, one mint (`#97EFC9`) or teal (`#005A3C`) plant on the desk. The professional is smiling slightly while reviewing engagement metrics. Shot at mid-distance, natural window light dominant. No colour filters. Conveys proactive, strategic, and professional social media management.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Social Media PR & Marketing section

---

### `/assets/images/digital-rep-services/svc-entrepreneur.jpg`
**Purpose:** Service panel image — For Entrepreneurs / Personal Brand (Personal Brand service).

**Prompt:**
> Editorial portrait photograph of a Black Nigerian entrepreneur — a man or woman in their mid-30s — dressed in well-cut business-casual attire (open-collar shirt, tailored trousers, or a smart fitted blazer). They stand in a bright, airy office or co-working space — large windows, natural greenery in the background including a tall forest green (`#0D3D28`) plant. The person is half-turned toward the camera with a composed, quietly confident expression. One hand rests on a desk or chair back. Shot at mid-distance, natural directional light from the side. No studio backdrops, no colour filters. The image should read as a professional personal brand portrait for a founder or executive — confident, approachable, real.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for For Entrepreneurs section

---

### `/assets/images/digital-rep-services/svc-google-ai.jpg`
**Purpose:** Service panel image — Google & AI Visibility (Search & AI service).

**Prompt:**
> Editorial photograph of a Black Nigerian professional at a bright modern workstation, examining a large monitor displaying a Google search results page or an AI-generated answer card (like Gemini or Perplexity). The screen clearly shows a Knowledge Panel-style result or a prominent featured snippet. The professional leans forward with interest, one hand raised toward the screen in a pointing or framing gesture. Office environment is clean and contemporary — teal (`#1EB496`) accent in the screen glow or a plant on the desk. Natural window light from one side. Shot at mid-distance. No colour overlays or filters. Conveys digital intelligence, search strategy, and technical authority.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Google & AI Visibility section

---

### `/assets/images/digital-rep-services/svc-exec-visibility.jpg`
**Purpose:** Service panel image — Founder & Executive Visibility (Executive Profile service).

**Prompt:**
> Editorial portrait photograph of a Black Nigerian business leader — a man in his late 40s — in a premium executive environment: a glass-walled boardroom, a high-rise office with a city view, or a hotel business lounge. The subject wears a well-tailored dark suit — charcoal or navy — with a white shirt and a teal (`#005A3C`) or forest green pocket square. He sits or stands with composed, direct authority — not stiff, not performative. Expression is calm and focused. Background is sharp enough to establish location but softly out of focus — Zuma Rock, Lagos skyline, or a modern Nigerian cityscape visible through the glass. Shot at a slight angle, natural window light from the side. No colour filters. The image should read as a Bloomberg Businessweek executive profile — global authority, distinctly Nigerian.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Founder & Executive Visibility section

---

### `/assets/images/digital-rep-services/svc-event-pr.jpg`
**Purpose:** Service panel image — Event PR & TV Coverage (Events & Media service).

**Prompt:**
> Editorial photograph taken at a corporate conference or summit in Nigeria. The main subject is a Black Nigerian professional — a presenter or MC — at a branded podium or stage, speaking to a medium-sized audience. TV camera crew or a broadcast journalist is visible at the side of the frame, filming the event. The audience is attentive and professional — business attire, diverse mix. Stage backdrop includes a teal (`#005A3C`) or forest green branded banner or pull-up display. Venue lighting is professional conference-style — overhead LEDs, no dramatic spotlights. Shot from a mid-angle across the room. No colour filters. Conveys professional event visibility, broadcast media coordination, and executive media presence.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Event PR & TV Coverage section

---

### `/assets/images/digital-rep-services/svc-knowledge-panel.jpg`
**Purpose:** Service panel image — Google Knowledge Panel (Entity Signals service).

**Prompt:**
> Editorial photograph of a Black Nigerian professional seated in a modern office, looking at a laptop screen showing a Google Knowledge Panel — a branded entity card on the right side of search results, with a photo, description, and official links. The professional points at or gestures toward the screen with a composed, satisfied expression. The office is clean and bright — a large mint (`#97EFC9`) or teal plant visible in the background. Natural window light from the side, screen glow adds warmth. Shot at mid-close distance. No colour filters. The image should convey digital authority, brand recognition in search, and the precision of entity-level SEO work.

**Dimensions:** 800 × 600 px minimum, 4:3 portrait or tall landscape
**Placement:** `.svc-img` panel for Google Knowledge Panel section

---

---

## Digital Marketing Service Pages

These prompts cover all six Digital Marketing sub-service pages. Each page has a full-bleed hero and in-page images placed at contextually relevant sections.

---

### Content Marketing Page — `/assets/images/content/`

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background — Content Marketing page.

**Prompt:**
> Editorial photograph of a Black Nigerian content strategist or writer working at a clean desk in a modern Lagos office. The professional is focused on a large monitor showing a content calendar or editorial plan — coloured task columns, headings, keyword clusters. A printed outline and a coffee mug sit beside the keyboard. Bookshelves with well-ordered professional books visible in the background. Natural window light from the side with warm overhead LEDs. Office accent colours include teal (`#005A3C`) cushion, forest green (`#0D3D28`) plant, and a small crimson-spined book on the shelf. Shallow depth of field on the subject. Shot from a slight low angle to convey authority. No colour filters. Conveys craft, strategic thinking, and content production at a professional scale.

**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** `.page-hero.photo-hero` background

---

#### `strategy-session.jpg`
**Purpose:** In-page image — content strategy session section.

**Prompt:**
> Editorial photograph of a small team of Black Nigerian professionals in a bright, modern conference room engaged in a content strategy session. A whiteboard behind them shows a mind map or content pillar diagram — teal marker lines on white. One person is presenting while two others take notes. Laptops and printed briefs on the table. A teal (`#1EB496`) accent plant and forest green (`#0D3D28`) wall panel visible in the background. Professional business-casual attire. Natural window light. Shot at a 3/4 angle from outside the table. No colour filters. Conveys collaborative strategy, structured planning, and professional content thinking.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left image beside strategy section copy

---

#### `writing-team.jpg`
**Purpose:** In-page image — writing and production team section.

**Prompt:**
> Editorial photograph of two or three Black Nigerian professionals at adjacent desks in a modern open-plan office, each focused on their screens. One is visibly editing a long-form article on a document editor; another reviews analytics on a dashboard. Quiet, focused energy. Teal (`#005A3C`) plant, mint (`#97EFC9`) cushion on office chair, and a forest green-framed artwork on the wall. Warm overhead lighting. Shot from a slight distance showing both workstations. No colour filters. Conveys a skilled in-house writing team, professional production, and organised editorial workflow.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right image beside writing team section copy

---

### Social Media Marketing Page — `/assets/images/social-media/`

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background — Social Media Marketing page.

**Prompt:**
> Editorial photograph of a Black Nigerian social media strategist or content creator at a bright, modern Lagos studio workspace. The professional is reviewing a content schedule on a large monitor showing a grid of post thumbnails, platform icons (LinkedIn, Instagram, X, Meta), and an analytics graph. A ring light is visible slightly out of frame; a smartphone with a branded profile is propped beside the monitor. Teal (`#1EB496`) plant in the background, forest green (`#0D3D28`) accent chair. Natural light and studio lighting combined. Shot at mid-close distance from a slight angle. No colour filters. Conveys platform expertise, creative production, and strategic social media management.

**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** `.page-hero.photo-hero` background

---

#### `linkedin-strategy.jpg`
**Purpose:** In-page image — LinkedIn strategy platform card.

**Prompt:**
> Close-up editorial photograph of a laptop screen showing a polished LinkedIn profile page of a Nigerian executive — professional headshot, compelling headline, strong About section visible. A Black Nigerian professional's hands are visible on the keyboard, slightly blurred, as if reviewing or editing. Desk surface is clean — a branded notebook and pen beside the laptop. Office background softly blurred: teal plant, forest green wall panel. Natural window light from the left. No colour filters. Conveys LinkedIn brand engineering, executive digital presence, and professional profile strategy.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Platform card image — LinkedIn section

---

#### `instagram-content.jpg`
**Purpose:** In-page image — Instagram content creation platform card.

**Prompt:**
> Editorial photograph of a Black Nigerian creative professional photographing a styled flat-lay setup — a branded product or book, stationery, and a teal accent fabric — with a smartphone on a small tripod. The professional is adjusting the composition carefully. Bright, airy creative studio. White background, natural light. Teal (`#1EB496`) and mint (`#97EFC9`) accent props in the flat-lay. Shot from a slight overhead-angle to include both the person and the subject. No colour filters. Conveys creative content production, Instagram aesthetic intentionality, and visual brand consistency.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Platform card image — Instagram section

---

#### `twitter-engagement.jpg`
**Purpose:** In-page image — X (Twitter) engagement platform card.

**Prompt:**
> Editorial photograph of a Black Nigerian professional at a home office desk, engaged in a conversation on X (Twitter) on a laptop. The screen shows a thread with multiple replies — text visible but not legible. The professional leans slightly forward, focused and thoughtful. A notebook with handwritten talking points is open beside the laptop. Teal (`#005A3C`) plant, warm overhead lighting, wood desk. Shot at mid-close distance from a 3/4 angle. No colour filters. Conveys thought leadership, real-time engagement, and consistent presence on X.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Platform card image — X (Twitter) section

---

#### `meta-ads.jpg`
**Purpose:** In-page image — Meta Ads (Facebook/Instagram) platform card.

**Prompt:**
> Editorial photograph of a Black Nigerian digital marketing professional reviewing Meta Ads Manager on a large monitor. The dashboard shows active campaigns, audience targeting panels, and performance graphs. The professional has a focused, analytical expression — one hand resting on the mouse, the other holding a printed report. Office is modern and bright. Forest green (`#0D3D28`) wall panel visible in background. Warm overhead LEDs. Shot at mid-distance from a slight side angle. No colour filters. Conveys paid social strategy, data-driven campaign management, and advertising expertise.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Platform card image — Meta Ads section

---

#### `content-creation.jpg`
**Purpose:** In-page image — community vs. audience story grid section.

**Prompt:**
> Editorial photograph of a Black Nigerian content creator recording a short-form video in a well-lit home studio setup. A ring light illuminates the professional, who speaks directly to camera with an engaged, natural expression. A branded backdrop (teal `#005A3C` or forest green `#0D3D28` tones) is visible behind. A smartphone on a gimbal captures the shot. Shot from a slight side angle to show both the creator and the camera setup. No colour filters. Conveys authentic content creation, platform-native video production, and community-building intent.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — image beside community vs. audience section copy

---

### SEO Page — `/assets/images/seo/`

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background — SEO page.

**Prompt:**
> Editorial photograph of a Black Nigerian SEO specialist at a dual-monitor workstation in a modern Lagos office. The left monitor shows a technical SEO audit tool (crawl report, error list, site structure visualisation); the right shows Google Search Console with performance graphs. The professional is mid-analysis — focused, slightly leaning forward. Forest green (`#0D3D28`) wall panel behind, teal (`#1EB496`) plant on the desk corner. Overhead LEDs, screen glow adds secondary light. Shot from a slight low angle at mid distance. No colour filters. Conveys technical rigour, analytical authority, and deep SEO expertise.

**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** `.page-hero.photo-hero` background

---

#### `technical-audit.jpg`
**Purpose:** In-page image — technical SEO audit team story grid section.

**Prompt:**
> Editorial photograph of a Black Nigerian technical SEO professional presenting a site audit report on a wall-mounted screen in a small meeting room. The screen shows a crawl map or technical error report — coloured nodes and lines. Two colleagues (also Black Nigerian professionals) are seated, reviewing printed reports. Conference table is clean; branded notebooks and laptops visible. Teal (`#005A3C`) plant in the corner, forest green `#0D3D28` accent on wall. Warm conference lighting. Shot from a 3/4 angle outside the table. No colour filters. Conveys technical depth, structured audit process, and collaborative analysis.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — image beside technical SEO team section copy

---

#### `content-team.jpg`
**Purpose:** In-page image — content/E-E-A-T SEO pillar section (optional in-page).

**Prompt:**
> Editorial photograph of two Black Nigerian professionals co-reviewing content on a laptop — one is a writer, the other a subject-matter expert (suggested by a bookshelf with professional titles behind them). They are discussing a long-form article draft visible on screen, one pointing at a paragraph. Warm, natural office lighting. Teal (`#1EB496`) plant, clean desk, printed research notes. Shot at mid-close distance from a slight angle. No colour filters. Conveys the expertise + authoritativeness + trustworthiness standard (E-E-A-T), content credibility, and expert-led editorial production.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Optional in-page image — E-E-A-T / Content SEO section

---

#### `analytics-review.jpg`
**Purpose:** In-page image — SEO results and reporting section (optional).

**Prompt:**
> Editorial photograph of a Black Nigerian SEO account manager presenting organic search performance data on a laptop in a client meeting. The laptop screen shows a GA4 or Google Search Console graph — traffic trend lines showing clear upward movement. The client (also a Black Nigerian professional) leans in with interest. Meeting table is clean and modern. Teal (`#005A3C`) wall accent, natural light from a window. Shot at a 3/4 angle from the client's side of the table. No colour filters. Conveys measurable SEO results, transparent reporting, and client-agency trust.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Optional in-page image — results/reporting section

---

### PPC / Paid Advertising Page — `/assets/images/ppc/`

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background — PPC & Paid Advertising page.

**Prompt:**
> Editorial photograph of a Black Nigerian PPC specialist at a wide workstation with two monitors — one showing Google Ads campaign manager with active campaigns, bids, and quality scores; the other showing a live conversion graph. The professional is focused and analytical, one hand on the mouse. Modern open-plan office, mid-afternoon. Forest green (`#0D3D28`) wall panel, teal (`#1EB496`) plant on desk edge. Overhead LEDs with screen glow. Shot from a slight low angle at mid distance. No colour filters. Conveys paid advertising precision, platform expertise, and data-driven campaign management.

**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** `.page-hero.photo-hero` background

---

#### `campaign-setup.jpg`
**Purpose:** In-page image — account ownership / campaign setup story grid section.

**Prompt:**
> Editorial photograph of a Black Nigerian digital advertising professional setting up a new Google Ads campaign on a laptop. The screen shows the campaign creation flow — campaign goal selection, targeting options, budget fields. The professional types carefully, with a printed campaign brief open beside the laptop. Quiet, focused workspace. Teal (`#1EB496`) plant in the background. Warm overhead light. Shot at mid-close distance from a slight angle showing both the person and the screen. No colour filters. Conveys careful setup, professional campaign architecture, and transparent account management.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — image beside account ownership section copy

---

#### `reporting-review.jpg`
**Purpose:** In-page image — reporting and results section (optional).

**Prompt:**
> Editorial photograph of a Black Nigerian PPC account manager presenting a monthly performance report to a client in a modern meeting room. The report on a printed or tablet screen shows ROAS, CPL, and conversion graphs — with an upward trend line highlighted. The client (also a Black Nigerian professional) is engaged, leaning slightly forward. Conference table is tidy. Forest green (`#0D3D28`) wall, teal plant, natural light from window. Shot at a 3/4 angle from the manager's side. No colour filters. Conveys results accountability, transparent reporting, and professional client partnership.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Optional in-page image — results/reporting section

---

### Link Building Page — `/assets/images/link-building/`

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background — Link Building page.

**Prompt:**
> Editorial photograph of a Black Nigerian digital PR and link-building specialist at a laptop in a modern Lagos office. The screen shows an outreach CRM or link prospecting tool — a list of media contacts, domains, and outreach status columns. The professional is mid-composition of an outreach email. Printed media list and branded notepad visible on the desk. Teal (`#005A3C`) plant, forest green (`#0D3D28`) wall panel behind. Natural window light from the side. Shot at mid distance from a slight side angle. No colour filters. Conveys methodical outreach, media relationship building, and authoritative link acquisition.

**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** `.page-hero.photo-hero` background

---

#### `outreach-team.jpg`
**Purpose:** In-page image — transparency / outreach team story grid section.

**Prompt:**
> Editorial photograph of two Black Nigerian digital PR professionals working side by side at adjacent desks — one drafting a media pitch on a laptop, the other reviewing a list of target publications on a second monitor. A sticky-note board behind them shows a campaign timeline and media targets. Teal (`#1EB496`) plant, clean professional office. Warm overhead lighting. Shot from a slight distance at a 3/4 angle to show both workstations. No colour filters. Conveys team-based outreach, editorial targeting, and a structured link-building process.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — image beside transparency/outreach section copy

---

#### `media-room.jpg`
**Purpose:** In-page image — digital PR / media placement section (optional).

**Prompt:**
> Editorial photograph of a Black Nigerian professional reviewing a live news article featuring their client's brand on a large monitor. The article headline is visible (not legible) on a recognisable editorial layout. The professional has a satisfied, focused expression — reviewing coverage on what is clearly a media monitoring dashboard. Teal (`#005A3C`) plant in background, warm office lighting, wood desk. Shot at mid-close distance from a slight side angle showing face and screen. No colour filters. Conveys earned media placement, editorial credibility, and digital PR outcomes.

**Dimensions:** 800 × 600 px minimum, 4:3 landscape
**Placement:** Optional in-page image — digital PR / media placement section

---

### Personal Branding Page — `/assets/images/personal-branding/`

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background — Personal Branding page.

**Prompt:**
> Editorial photograph of a Black Nigerian executive or founder in a modern Lagos office, seated at a well-appointed desk — confident posture, professional attire (dark suit, forest green `#0D3D28` or teal `#005A3C` accent tie). The professional looks slightly off-camera toward an unseen horizon, conveying vision and authority. Behind them: a floor-to-ceiling bookshelf with well-ordered professional books, a teal plant, and a large window with Lagos cityscape softly visible. Warm, premium office lighting — no harsh shadows. Shot at mid-distance, slight low angle. No colour filters. Conveys executive authority, personal brand gravitas, and leadership presence.

**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** `.page-hero.photo-hero` background

---

#### `linkedin-profile.jpg`
**Purpose:** In-page image — LinkedIn brand engineering story grid section.

**Prompt:**
> Editorial photograph of a Black Nigerian executive reviewing their own LinkedIn profile on a large desktop monitor. The profile is polished and complete — professional headshot, featured banner, compelling headline visible at a readable size. The professional is seated, reviewing the page with a composed, strategic expression. Modern home office or executive suite. Teal (`#1EB496`) plant beside the monitor, natural window light. Shot at mid-close distance showing both subject and screen in frame. No colour filters. Conveys executive LinkedIn engineering, digital authority positioning, and personal brand visibility.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — image beside LinkedIn brand section copy

---

#### `speaking-event.jpg`
**Purpose:** In-page image — speaking and visibility story grid section.

**Prompt:**
> Editorial photograph of a Black Nigerian executive or thought leader speaking on stage at a professional conference or corporate forum in Nigeria. The speaker stands at a branded podium or open-stage position, addressing a medium-to-large professional audience. Stage lighting is bright and professional. Audience is attentive — business professionals, diverse mix. A large presentation screen behind the speaker shows a branded slide (teal `#005A3C` or forest green `#0D3D28` colour scheme). Shot from mid-hall at a slight angle, capturing both speaker and audience reaction. No colour filters. Conveys speaking authority, industry visibility, and executive thought leadership.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — image beside speaking/visibility section copy

---

---

## Who We Serve Pages

> Images for the four audience segment pages. All images should feature real, diverse people — no stock-photo sterility, no overly cinematic drama. Professional photographer aesthetic: documentary warmth, natural light where possible, credible environments. People should represent African and global diversity in professional contexts.

---

### Who We Serve: Individuals (`/who-we-serve/individuals/`)

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background image — Professionals, Founders & Creators page.

**Prompt:**
> Wide-format editorial photograph of a confident Black African professional woman in her mid-30s, seated at a clean, well-lit desk in a modern co-working space or private office in Lagos or Nairobi. She looks directly into camera with quiet authority — not a smile, a composed confidence. A laptop screen glows softly in front of her, out of focus. Natural window light from the left. Warm-toned workspace with subtle greenery or indoor plants in the background. The image feels like a documentary portrait from a business magazine — no dramatic editing, natural colour grading, shallow depth of field. She wears smart-casual professional attire. The composition is wide with significant negative space on the right third of the frame for headline text overlay.

**Dimensions:** 2400 × 1400 px minimum, 16:9 landscape
**Placement:** Page hero — full-bleed with dark gradient overlay

---

#### `professional-working.jpg`
**Purpose:** In-page story grid — The Visibility Problem section.

**Prompt:**
> Editorial photograph of a Black African male professional in his late 30s or early 40s, working at a standing desk or seated at a large monitor in a bright, modern Lagos office or home office environment. He is writing notes in a notebook while reviewing something on-screen, clearly in a state of focused work rather than posing. Nearby: a cup of coffee, a few business books, natural plants. Shot from a 45-degree angle — slightly above eye level. Natural daylight from a window. Warm neutral tones, no artificial colour enhancement. The image reads as genuine productivity, not stock-photo performance. No props that signal "tech startup" stereotypically. Conveys professional seriousness and expertise.

**Dimensions:** 1200 × 900 px minimum, 4:3 portrait or square
**Placement:** Story grid — left column image beside "The Visibility Problem" copy

---

#### `digital-authority.jpg`
**Purpose:** In-page story grid — The Digital Trust Economy section (dark background).

**Prompt:**
> Wide editorial photograph of a Black African professional woman in her early 40s, shot from behind or at a 3/4 angle, looking at a large monitor or dual-screen setup showing website analytics, LinkedIn data, or a professional personal website. The room is dimly lit except for the screen glow — evening or controlled studio light. The image is moody but not dramatic: she is reading data or reviewing her digital presence, not posing. The monitors show graphs, profile pages, or dashboards in cool blue-green tones. Shot with natural shallow depth of field. The image conveys the idea of monitoring and building a digital presence — quiet professional authority. No text visible on screen. Cinematic restraint, not cinematic excess.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "The Digital Trust Economy" copy

---

### Who We Serve: Businesses (`/who-we-serve/businesses/`)

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background image — Startups, SMEs & Enterprises page.

**Prompt:**
> Wide-format editorial photograph of a diverse team of three to four African professionals gathered around a large table covered with laptops, printed reports, and sticky-note planning materials. The setting is a modern co-working space or open-plan tech office in Lagos or Accra — glass-walled meeting room, exposed ceiling, contemporary furniture. The team is mid-discussion — one person is pointing at something on a laptop, others are leaning in. Faces are visible and show professional engagement, not posed smiles. Mix of genders and ages (late 20s to early 40s). Shot wide at a slight overhead angle to capture the whole table environment. Natural or large-format office light, warm-neutral colour balance. Significant space on the left or right edge for headline text overlay. No obvious corporate branding visible. Conveys capable, collaborative business technology work.

**Dimensions:** 2400 × 1400 px minimum, 16:9 landscape
**Placement:** Page hero — full-bleed with dark gradient overlay

---

#### `team-working.jpg`
**Purpose:** In-page story grid — The Business Problem section.

**Prompt:**
> Editorial photograph of two Black African software engineers or technical professionals — one man, one woman, both in their late 20s or early 30s — reviewing code on dual monitors side by side. They are leaning in slightly, in a focused discussion about what is on screen. The setting is a real working environment — a software development studio or tech company office, not a staged background. Shot at a natural angle, mid-distance. The screens show code or a technical diagram, not illegible blur. Good ambient office light with no artificial colour effects. No props that feel forced. The image conveys collaborative technical work and professional competence. Both individuals look engaged and capable.

**Dimensions:** 1200 × 900 px minimum, 4:3 landscape
**Placement:** Story grid — left column image beside "The Business Problem" copy

---

#### `delivery-approach.jpg`
**Purpose:** In-page story grid — How We Deliver section (dark background).

**Prompt:**
> Editorial photograph of a Black African male software engineer or DevOps professional in his early 30s, standing in front of a large monitor or display showing a CI/CD pipeline dashboard, deployment logs, or a production monitoring interface. He has his arms folded, looking at the screen with concentration — not at the camera. The room is a modern server room, tech operations centre, or dark-mode developer environment. Blue and green screen light is the dominant ambient illumination. Shot from a slight angle, capturing the person and the screens in the same frame. No stock-photo posing. The image conveys infrastructure thinking, technical depth, and production focus — not design or business process.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "How We Deliver" copy (dark section)

---

### Who We Serve: Organisations (`/who-we-serve/organisations/`)

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background image — NGOs, Institutions & Associations page.

**Prompt:**
> Wide editorial photograph of a diverse group of African professionals in an NGO or institutional meeting environment — a conference room or community centre with large windows, natural light, and simple but professional furnishings. Five to six people are seated or standing around a table. Ages range from late 20s to early 50s. Mix of professional attire and smart-casual. One person is presenting from a laptop. Others are listening attentively, some with notebooks. The atmosphere is purposeful and collaborative — not corporate glamour, not poverty-signalling development-sector tropes. Shot wide to capture the full group, with space in the upper third for headline text overlay. Warm natural daylight. The image reads as mission-driven competence. No visible logos or identifiable branding.

**Dimensions:** 2400 × 1400 px minimum, 16:9 landscape
**Placement:** Page hero — full-bleed with dark gradient overlay

---

#### `mission-team.jpg`
**Purpose:** In-page story grid — The Paradox section.

**Prompt:**
> Editorial photograph of three or four African professionals — representing a mix of genders and ages, from late 20s to early 50s — seated around a conference table in an NGO or institutional office. The table has printed reports, laptops, and a whiteboard visible in the background with planning notes. The group is mid-discussion: one person is speaking, others are actively listening or writing. The environment looks like a real working NGO or association office — practical furnishings, some organisational signage on the wall (not legible). Natural light from a window. Shot at a 45-degree angle, capturing the group dynamic. The image conveys people genuinely working toward a collective purpose — not a staged collaboration photo.

**Dimensions:** 1200 × 900 px minimum, 4:3 landscape
**Placement:** Story grid — left column image beside "The Paradox" copy

---

#### `community-impact.jpg`
**Purpose:** In-page story grid — Our Commitment section (dark background).

**Prompt:**
> Editorial photograph of a Black African woman in her mid-30s or 40s — the kind of person who runs a community programme or manages an association — sitting with a small group of community members around a table in a community hall or church hall. She is showing them something on a tablet or laptop. The group includes older men and women, a younger person. The setting is humble but dignified — not photogenic poverty, not corporate glamour. Natural light from windows. Shot at a slight distance with a medium focal length to capture the full scene. The image conveys a real service relationship and the responsibility of running a mission-driven organisation well. Warm tones, unposed.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "Our Commitment" copy (dark section)

---

### Who We Serve: Nations (`/who-we-serve/nations/`)

#### `hero-bg.jpg`
**Purpose:** Full-bleed hero background image — Government & Public Sector page.

**Prompt:**
> Wide editorial photograph of a modern government operations centre or ministerial conference room in a West African context — Nigeria, Ghana, or similar. A group of four to five senior public servants and officials in professional attire (some in traditional formal wear, others in suits) are standing or seated around a large table with laptops and printed documents. One person is presenting data on a wall-mounted display showing a dashboard or government portal interface. The room has the aesthetic of a modern African government institution — professional, functional, serious. No cartoon-villain bureaucracy or poverty tropes. Shot wide with the group and the display both visible. Significant space in the frame for headline overlay. The image conveys effective, capable government work.

**Dimensions:** 2400 × 1400 px minimum, 16:9 landscape
**Placement:** Page hero — full-bleed with dark gradient overlay

---

#### `government-digital.jpg`
**Purpose:** In-page story grid — The Public Sector Mandate section.

**Prompt:**
> Editorial photograph of two or three African government officials or public sector professionals in a modern office environment — a ministry or agency operations room — reviewing large monitor screens showing a government digital services portal or public data dashboard. The professionals are Black African, mix of genders, early 30s to mid-40s, in formal professional or smart-casual attire. One is pointing at the screen, another is taking notes. The screens show a clean government portal interface (no actual identifiable branding). Shot at a natural mid-distance, slightly to the side. Good office lighting. No dramatic post-processing. The image conveys careful, deliberate attention to public digital infrastructure — not a photo op.

**Dimensions:** 1200 × 900 px minimum, 4:3 landscape
**Placement:** Story grid — left column image beside "The Public Sector Mandate" copy

---

#### `public-servants.jpg`
**Purpose:** In-page story grid — Delivery Principles section (dark background).

**Prompt:**
> Editorial photograph of three African public sector officials or government IT professionals — two men and one woman, mix of ages 30s to 50s, in formal attire — in a planning or strategy session in a modern government conference room. One is standing at a whiteboard that has system architecture or project phases diagrammed in simple markers. Others are seated, reviewing printed documents or laptops. The environment is a real institutional space — not a glossy corporate boardroom, not a rundown civil service office. Practical, professional, purposeful. Natural office light. Shot from a slight angle. The image conveys structured, rigorous government technology planning — the kind that happens before a system goes live. No stock-photo dynamics.

**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "Delivery Principles" copy (dark section)

---

*Last updated: 2026-11-26*

---

## Industries Pages

The following prompts cover the 12 industry-specific pages. Each page has three images: the hero background and two in-body images woven into the layout. All images must look like photographs taken by a professional editorial photographer — natural, candid where appropriate, technically excellent. No overly cinematic or hyper-saturated look. People in every image should be diverse in age, gender, and appearance. Where Nigerian or African settings apply, they should feel authentic, not stock-photo generic.

---

### Agriculture

#### `hero-bg.jpg`
**Prompt:** A wide-angle aerial photograph of a large-scale Nigerian farm at golden hour — rows of crops stretching to the horizon, with two farmers (one man, one woman, both in their 30s, wearing practical work clothing) visible in the mid-ground reviewing something on a rugged tablet. Natural light, warm tones. No text or graphic overlays. Shot from a low drone angle. Farm background includes red clay soil typical of West Africa. Brand accent: one piece of clothing in deep forest green.

**Path:** `/assets/images/industries/agriculture/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `farmers-tablet.jpg`
**Prompt:** A close-up photograph of two Nigerian farmers — a woman in her 40s wearing a wide-brimmed sun hat, and a man in his late 30s — both leaning over a durable tablet together in an open field. The tablet screen shows what appears to be a farm data dashboard. The background is blurred green farmland. Natural daylight. Relaxed, documentary-style composition. No stock-photo stiffness — these look like real farmers engaging with technology that matters to them.

**Path:** `/assets/images/industries/agriculture/farmers-tablet.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Challenge" copy

---

#### `agritech-dashboard.jpg`
**Prompt:** A professional photograph of a laptop screen showing an agricultural data analytics dashboard — charts, maps, crop yield metrics — placed on a desk in a bright, modern Lagos office. A Black woman in her 30s, in business casual attire, sits in the background partially visible, working. Clean, editorial look. Office environment includes a plant in teal-green. The screen is sharp and readable. Natural window light supplemented by indoor lighting.

**Path:** `/assets/images/industries/agriculture/agritech-dashboard.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "Our Approach" copy (dark section)

---

### Media & Entertainment

#### `hero-bg.jpg`
**Prompt:** A production studio photograph — a modern Lagos film set with professional lighting rigs, cameras, and crew members at work. The scene shows approximately four crew members (diverse — two men, two women, mixed ages) in a high-energy but controlled environment. Dramatic directional studio lighting with deep shadows and warm key lights. The look is cinematic but editorial — a real production, not a posed ad. No text overlays. Rich, atmospheric tones.

**Path:** `/assets/images/industries/media-entertainment/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `media-team.jpg`
**Prompt:** A professional documentary photograph of a diverse Nigerian media production team in a modern studio — four people (two men, two women) in their 20s and 30s gathered around a monitor reviewing footage. Relaxed but focused energy. Visible equipment: camera rigs, lighting stands. The room has a creative, professional feel — dark walls, coloured lighting accents in teal-green. Candid, editorial style. No posing for the camera.

**Path:** `/assets/images/industries/media-entertainment/media-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Landscape" copy

---

#### `streaming-platform.jpg`
**Prompt:** A photograph of multiple screens — a laptop, a large monitor, and a tablet — all displaying a streaming platform interface with video thumbnails, a search bar, and a recommendation carousel. The screens are arranged on a desk in a modern Lagos office. Ambient office background, partially blurred. The screens are sharp and the UI design looks clean and professional. Natural and office lighting blend. No people visible — focused on the technology.

**Path:** `/assets/images/industries/media-entertainment/streaming-platform.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "Our Technology" copy (dark section)

---

### Education & eLearning

#### `hero-bg.jpg`
**Prompt:** A wide-angle photograph of a modern Nigerian secondary school classroom with 20–25 students — diverse, ages 14–17, mixed gender — using laptops and tablets in a bright, well-lit room. The teacher (a woman in her early 40s) stands near a large digital whiteboard at the front. The energy is engaged and productive. Daylight through large windows. No stock-photo stiffness — this looks like a real, well-resourced classroom.

**Path:** `/assets/images/industries/education-elearning/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `students-learning.jpg`
**Prompt:** A close-up documentary photograph of three Nigerian secondary school students (two girls, one boy, ages 15–17) gathered around a single tablet, working together on something. Their expressions are curious and engaged. The classroom background is blurred but visible — desks, windows, natural light. One student points at the screen. Editorial, candid style. The image should feel warm and positive without being saccharine.

**Path:** `/assets/images/industries/education-elearning/students-learning.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Gap" copy

---

### Travel & Hospitality

#### `hero-bg.jpg`
**Prompt:** A wide-angle exterior photograph of a modern upscale Nigerian hotel — a clean architectural building with a landscaped entrance, palm trees, and a broad driveway. Shot at dusk with warm golden interior lights visible through the lobby windows against a blue-purple twilight sky. No people. Architecture photography style — sharp, well-composed, aspirational but not exaggerated. The building has contemporary African architectural details.

**Path:** `/assets/images/industries/travel-hospitality/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `hotel-lobby.jpg`
**Prompt:** An interior photograph of a modern, upscale hotel lobby in Nigeria — marble floors, natural wood accents, large plants, and warm lighting. At the reception desk, a male hotel guest (Black, 30s, business attire) uses a digital self-check-in kiosk. Behind the desk, a female receptionist (Black, late 20s, in hotel uniform) is visible in the background. The lobby feels spacious and premium. Natural and artificial lighting blend. Editorial, architectural photography style.

**Path:** `/assets/images/industries/travel-hospitality/hotel-lobby.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Shift" copy

---

#### `booking-platform.jpg`
**Prompt:** A photograph of a Black man (40s, in a professional hotel manager's suit) holding a tablet showing a hotel property management dashboard. He stands in the corridor of a modern hotel with rooms visible behind him. The screen shows occupancy charts and booking stats. Sharp screen, slightly blurred background. Confident, working pose — not staged. Natural hotel corridor lighting supplemented by fill light. Editorial style.

**Path:** `/assets/images/industries/travel-hospitality/booking-platform.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "What We Build" copy (dark section)

---

### Logistics

#### `hero-bg.jpg`
**Prompt:** A wide-angle photograph inside a large modern logistics warehouse in Nigeria — high metal shelving stacked with organised parcels and packages, a wide central aisle, and several workers visible in the mid-ground. Industrial overhead lighting. The scene feels busy, organised, and professional. No stock photo staging — the people are working, not posing. Shot from a low angle to emphasise the scale of the shelving. Brand colour accent in one worker's safety vest.

**Path:** `/assets/images/industries/logistics/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `warehouse-team.jpg`
**Prompt:** A documentary photograph of three Nigerian warehouse workers — two men and one woman, in their 30s, wearing high-visibility vests — examining and sorting packages on a conveyor belt. Focused, candid expressions. The warehouse environment is visible in the background: industrial shelving, overhead lights, forklifts. Editorial style — this looks like a real operation, not a photoshoot. One high-vis vest has a forest green colour.

**Path:** `/assets/images/industries/logistics/warehouse-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Challenge" copy

---

#### `dispatch-centre.jpg`
**Prompt:** A photograph of a logistics operations control room — three large monitors on a wall showing a live fleet tracking map with GPS dots, delivery status panels, and route visualisations. Three managers (two Black women, one Black man, all in their 30s and 40s) stand or sit watching the screens and taking notes. Modern office environment. The room is lit mainly by screen glow with overhead office lighting. Professional, editorial style.

**Path:** `/assets/images/industries/logistics/dispatch-centre.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "Built for the African Logistics Reality" copy (dark section)

---

### Financial Technology

#### `hero-bg.jpg`
**Prompt:** A wide-angle exterior photograph of a modern fintech office building in Lagos — a contemporary glass-and-steel structure with Nigerian architectural touches, shot in bright midday light. The entrance area shows a few professionals walking in and out. Clean, corporate but dynamic feel. No text or graphics visible. Clear sky, strong light. The image feels like it belongs in a fintech company's annual report.

**Path:** `/assets/images/industries/financial-technology/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `fintech-team.jpg`
**Prompt:** A professional photograph of four fintech professionals — two men and two women (Black Nigerians, ages 25–40) gathered around a large monitor showing financial analytics charts. The office environment is modern and open-plan with natural light. The team are engaged in discussion, pointing at the screen. Casual business attire. Editorial, candid style — not a posed shot. The workspace feels like a real Lagos tech company: clean, well-resourced, energetic.

**Path:** `/assets/images/industries/financial-technology/fintech-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Opportunity" copy

---

### Retail & eCommerce

#### `hero-bg.jpg`
**Prompt:** A wide-angle photograph inside a modern, well-stocked Nigerian retail store — bright overhead lighting, clean product shelving, and a few shoppers visible. The store has a premium feel without being a luxury boutique. Shot from the entrance looking in, capturing the full depth of the retail space. A digital display near the entrance shows product offers. No clutter — this is a well-organised, aspirational retail environment.

**Path:** `/assets/images/industries/retail-ecommerce/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `marketplace-team.jpg`
**Prompt:** A close-up documentary photograph of a Nigerian small business owner — a woman in her 30s — sitting at a desk in her small but well-organised Lagos store, reviewing eCommerce analytics on an open laptop. The screen shows order counts and sales charts. Relaxed, candid expression. Products visible in the background (fabric, goods). Natural window light. The image should feel like a portrait of a real entrepreneur working, not a stock photo.

**Path:** `/assets/images/industries/retail-ecommerce/marketplace-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Shift" copy

---

### Healthcare

#### `hero-bg.jpg`
**Prompt:** A wide-angle interior photograph of a modern, well-lit Nigerian private hospital reception area — clean, contemporary design with marble or tile floors, natural light from large windows, and a staffed reception desk. A few patients and healthcare workers are visible in the background, moving naturally. No posing. Warm, reassuring atmosphere. The space looks well-resourced and professional without being sterile or cold.

**Path:** `/assets/images/industries/healthcare/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `healthcare-team.jpg`
**Prompt:** A professional documentary photograph of a Nigerian doctor (a man in his early 40s, in a white coat) and a nurse (a woman in her 30s, in scrubs) standing together in a modern clinic corridor, reviewing patient data on a tablet. The tablet screen is visible showing what appears to be an electronic medical record. Both look focused and engaged. Candid, editorial style. Hospital corridor behind them is clean and modern. Natural window light and clinic lighting.

**Path:** `/assets/images/industries/healthcare/healthcare-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Imperative" copy

---

### Automotive

#### `hero-bg.jpg`
**Prompt:** A wide-angle exterior photograph of a modern car dealership in Lagos — a bright, well-branded showroom with floor-to-ceiling glass, several cars visible inside, and the forecourt showing a few vehicles under display canopies. Shot in midday light. Clean, corporate, aspirational. A few customers and a salesperson visible through the glass or in the forecourt, naturally positioned. No posing. The image should feel like editorial automotive photography.

**Path:** `/assets/images/industries/automotive/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `car-dealership.jpg`
**Prompt:** A professional interior photograph of a modern Nigerian car dealership showroom — two customers (a Black couple, mid-30s, casually dressed) standing beside a new SUV, interacting with a touchscreen display panel showing vehicle specifications. A salesperson (Black woman, late 20s, in professional attire) stands nearby facilitating. The showroom floor is clean and bright with overhead lighting. The atmosphere is relaxed and positive. Editorial, candid style.

**Path:** `/assets/images/industries/automotive/car-dealership.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Shift" copy

---

### ISVs & Product Companies

#### `hero-bg.jpg`
**Prompt:** A wide-angle open-plan office photograph of a modern Nigerian software company — rows of developer workstations, large monitors, good natural light from wide windows, plants, and a generally energetic atmosphere. Several developers (diverse — men and women, ages 24–35) are at their stations working. The office feels professional and creative without being a cliché startup ping-pong room. Shot from a slight elevated angle to show the depth of the space.

**Path:** `/assets/images/industries/isvs-product-companies/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `product-team.jpg`
**Prompt:** A close-up documentary photograph of three software developers (two men, one woman, all Black Nigerians in their late 20s to mid-30s) gathered at one workstation, reviewing code or a technical diagram on a large monitor. Engaged, collaborative. The workspace has visible monitors, sticky notes, and a coffee cup. Natural and monitor light blend. Candid style — not posed. The energy feels like a real product team doing real work.

**Path:** `/assets/images/industries/isvs-product-companies/product-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Challenge" copy

---

### Digital & Marketing Agencies

#### `hero-bg.jpg`
**Prompt:** A wide-angle open-plan creative agency office in Lagos — large creative monitors showing design and campaign work, whiteboards covered in strategy notes, and a diverse team of creatives (men and women, ages 24–38) in a mix of focused desk work and small group discussion. The office feels energetic and creative: exposed ceilings, good lighting, plants, one accent wall in deep green. Shot from a mid-level angle capturing the full breadth of the space.

**Path:** `/assets/images/industries/digital-marketing-agencies/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `agency-team.jpg`
**Prompt:** A professional documentary photograph of four marketing agency professionals (two Black women, one Black man, one mixed ethnicity woman, ages 25–38) gathered around a large monitor showing a campaign analytics dashboard — click-through rates, audience data, and social metrics visible on screen. The room is a modern Lagos agency meeting space. The team is engaged in discussion. Candid, editorial style. Modern office lighting, natural light from a window.

**Path:** `/assets/images/industries/digital-marketing-agencies/agency-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Opportunity" copy

---

### Real Estate

#### `hero-bg.jpg`
**Prompt:** A wide-angle aerial photograph of a modern residential development in Lagos — rows of well-designed houses or apartments with landscaped communal areas, shot from a drone at medium altitude in daylight. The development looks contemporary and aspirational without being out of reach. Palm trees, clean roads, and green spaces visible. The image has the quality of professional real estate marketing photography — sharp, balanced, beautiful light.

**Path:** `/assets/images/industries/real-estate/hero-bg.jpg`
**Dimensions:** 1920 × 1080 px minimum, 16:9 landscape
**Placement:** Page hero background

---

#### `property-team.jpg`
**Prompt:** A professional photograph of a real estate team — two men and one woman (Black Nigerians, ages 30–45) in a modern property agency office, gathered around a table with a laptop showing property listings and printed floor plans. The team looks engaged in a client discussion or internal review. Office environment is professional: branded signage, clean desk, good lighting. Editorial, candid style. The atmosphere is confident and competent.

**Path:** `/assets/images/industries/real-estate/property-team.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — left column image beside "The Moment" copy

---

#### `property-development.jpg`
**Prompt:** A wide-angle aerial photograph of an active residential construction site in Lagos — multiple buildings at various stages of construction, with cranes, scaffolding, and construction workers visible at ground level. Shot in midday light from a drone angle that shows both the scale of the development and the urban context surrounding it. The image should feel like high-quality architectural and development photography — not a stock image of generic construction.

**Path:** `/assets/images/industries/real-estate/property-development.jpg`
**Dimensions:** 1200 × 800 px minimum, 3:2 landscape
**Placement:** Story grid — right column image beside "Who We Serve" copy (dark section)
