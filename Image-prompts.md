# Image Prompts — GreaterHeight Technologies Website

Reference file for AI-generated photography and Open Graph images across the site.
All prompts are written for **Midjourney v6** or **Flux 1.1 Pro** unless noted.
Substitute `--ar` flags for other tools as needed.

---

## Brand Context (read before generating)

**Company:** GreaterHeight Technologies — a Lagos-founded IT consultancy with 15+ years delivering software, AI solutions, and digital infrastructure for banks, telecoms, government agencies, and enterprises across Nigeria and Africa.

**Aesthetic:** Editorial, professional, candid-warm. Not clinical or sterile. Not generic "diverse team smiling at a laptop." Think thoughtful people doing serious, precise work in a modern Lagos setting.

**People:** Primarily West African / Nigerian professionals — engineers, consultants, analysts. Mix of men and women, ages 25–45. Smart-casual attire; some formal. Natural, un-posed where possible.

**Location feel:** Modern open-plan office with character — warm lighting, exposed brickwork or concrete, potted plants, dual monitors, whiteboards, Lagos daylight.

**Brand palette for reference:**
- Deep forest green: `#003020`
- Crimson: `#8C0D0C`
- Mint: `#97EFC9`
- Warm cream: `#FDFAF4`
- Dark teal: `#005A3C`

**Universal negative prompt (add to every generation):**
`stock photo, generic, cheesy smile, fake diversity, Western office clichés, white majority, North American setting, European aesthetic, lens flare, oversaturated, HDR, illustration, cartoon, render, 3D, watermark`

---

## Content Images (800 × 600 px, 4:3)

These appear inside page sections next to body copy, overlaid with a dark tint and a small badge label.
Output: **JPEG, 800 × 600 px, quality 85–90**. After download, run through `squoosh` or `imageoptim` to keep under 120 KB.

---

### 1. `assets/images/hero/company-overview-story.jpg`

**Used on:** `/who-we-are/company-overview/`
**Badge overlay:** "2010 — Year founded, Lagos"
**Alt:** GreaterHeight Technologies engineers in a collaborative technical session at the Lagos headquarters

**Prompt:**
```
A team of four Nigerian software engineers and consultants gathered around a large desk covered with laptops, printed architecture diagrams, and sticky notes. The mood is focused and collaborative — one person is gesturing at a whiteboard diagram while the others listen and take notes. The room is a modern open-plan tech office in Lagos: warm pendant lighting, floor-to-ceiling windows with soft daylight, exposed concrete ceilings, lush potted greenery in the corner. Candid-editorial photography style. Shallow depth of field. Muted, warm tones. Professional attire (shirts, blazers). No phones, no generic handshakes. --ar 4:3 --v 6 --style raw --q 2
```

**Alternative angle:** Close crop on a single engineer reviewing code on a dual-monitor setup, warm Lagos afternoon light from the left, another colleague visible and blurred in the background.

---

### 2. `assets/images/hero/our-culture-story.jpg`

**Used on:** `/who-we-are/our-culture/`
**Badge overlay:** "People — Our greatest asset"
**Alt:** GreaterHeight Technologies team in collaborative session

**Prompt:**
```
Five Nigerian tech professionals of mixed gender and age in a relaxed but purposeful team stand-up meeting. Three stand near a whiteboard covered in hand-drawn system diagrams; two sit on high stools with laptops open. The office is bright and open-plan — large windows, plants, casual seating zones mixed with focused workstations. The tone is warm and collegiate, not corporate. People are mid-conversation, some laughing lightly, some thinking. Smart-casual Lagos tech company. Candid editorial photography. Natural light. --ar 4:3 --v 6 --style raw --q 2
```

**Alternative:** Overhead shot of a round meeting table — hands on laptops, notebooks, coffee cups, a printed project timeline pinned to the centre, taken from directly above. No faces needed.

---

### 3. `assets/images/hero/career-opportunities.jpg`

**Used on:** `/who-we-are/current-openings/`
**Badge overlay:** "Hiring — Across six practice areas"
**Alt:** GreaterHeight Technologies open, modern workspace

**Prompt:**
```
Wide-angle interior shot of a modern Lagos tech office with no people, or one or two people visible in the deep background. The space reads as welcoming and professional: clean hot-desks, ergonomic chairs, dual monitors at tidy workstations, a glass-walled meeting room with a whiteboard visible inside, warm pendant lights above. Lagos afternoon light streaming through floor-to-ceiling windows. The space has personality — exposed brickwork on one wall, a long bookshelf with binders and reference books, a small breakout zone with a couch and coffee table. Architectural interior photography. Tack-sharp, warm. --ar 4:3 --v 6 --style raw --q 2
```

**Alternative:** A single Nigerian professional, early 30s, standing at a standing desk reviewing code on a large monitor, back half-turned to camera, relaxed posture. Out-of-focus warm office background. Editorial style.

---

### 4. `assets/images/services/ai-consulting.jpg`

**Used on:** `/what-we-do/ai/consulting/`
**Badge overlay:** "Strategy — Before implementation"
**Alt:** AI strategy and consulting session

**Prompt:**
```
Two or three Nigerian technology consultants and a client in a focused strategy session at a long conference table. One consultant is standing, gesturing at a large screen or whiteboard showing a simple AI pipeline diagram — boxes, arrows, data flow — nothing too complex. The client, a professional in formal attire, is leaning forward engaged. Laptops, notebooks, printed documents on the table. The room is a smart glass-walled meeting room inside a modern Lagos office building. Natural daylight. The mood is serious and expert, not salesy. No stock-photo poses. Candid editorial. --ar 4:3 --v 6 --style raw --q 2
```

**Alternative:** Close-up of a laptop screen showing a simple ML pipeline diagram or a data dashboard (non-branded, abstract), with a human hand and forearm at the keyboard in the foreground. Shallow depth of field, warm ambient office light.

---

## Open Graph Images (1200 × 630 px, ~1.9:1)

These are the social-preview cards shown when a page is shared on LinkedIn, X, or WhatsApp.
They must read clearly at **small size** (link preview thumbnails) and contain **no small text**.
Output: **JPEG, 1200 × 630 px, quality 80**. Keep under 100 KB.

OG images for this site are branded composites: a strong photographic background + the GreaterHeight wordmark bottom-left + a bold short label. Generate the background photograph first, then composite in a design tool (Canva, Figma, or Adobe Express).

**Common composite spec:**
- Background photo fills the frame (no white borders)
- Dark overlay gradient: `rgba(0,48,32,0.55)` left-to-right
- GreaterHeight wordmark (`greaterheight-logo.png`, white version): bottom-left, ~200 px wide
- Page label in white: 36–48 px, bold, top-left or centre, max 30 characters
- Leave the right 40% of the frame relatively clear and uncluttered

---

### 5. `assets/images/og/og-company-overview.jpg`

**Label text:** "Who We Are"
**Background photo prompt:**
```
Aerial or high-angle view of Lagos island skyline at golden hour — office towers, the lagoon, warm amber and teal sky. Wide cinematic frame. No people, no text. Clean, striking. --ar 19:10 --v 6 --style raw
```

---

### 6. `assets/images/og/og-our-culture.jpg`

**Label text:** "Our Culture"
**Background photo prompt:**
```
Interior of a warm, modern Lagos tech office during working hours — multiple people visible but none prominent, warm pendant lights, greenery, wood tones. The energy is calm and focused. --ar 19:10 --v 6 --style raw
```

---

### 7. `assets/images/og/og-current-openings.jpg`

**Label text:** "Join Our Team"
**Background photo prompt:**
```
Close-up abstract shot of a modern office environment detail: keyboard and monitor edge in the foreground, out-of-focus warm office background. Clean, minimal, professional. Warm tones. --ar 19:10 --v 6 --style raw
```

---

### 8. `assets/images/og/og-ai-consulting.jpg`

**Label text:** "AI Consulting"
**Background photo prompt:**
```
Abstract macro photograph of a circuit board or fiber-optic network cables lit in deep teal and forest green, dark background, sharp and rich in detail. No text. No logos. --ar 19:10 --v 6 --style raw
```

---

## Notes on Production

1. **Aspect ratios** — Content images (4:3) and OG images (1.9:1) have different crops. Generate at native aspect ratio; don't crop from a square or portrait.
2. **File naming** — Filenames are already wired into page HTML; don't rename on upload.
3. **Directory creation** — The following directories don't exist yet in the repo and must be created before adding files:
   - `assets/images/hero/`
   - `assets/images/services/`
   - `assets/images/og/`
4. **Compression** — Run every image through lossless or quality-85 JPEG optimisation (Squoosh, ImageOptim, or `jpegoptim -m85`). The hero slot renders at max ~800 px wide on most screens; no need to supply more than 1200 px wide.
5. **WebP fallback** — If you supply WebP versions alongside JPEG, update each `<img>` tag to use a `<picture>` element with a `<source type="image/webp">`. Currently all tags use `<img src="…jpg">` directly.
