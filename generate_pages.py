#!/usr/bin/env python3 -I
"""
Generate 32 missing pages for greaterheight.tech
All pages use the canonical nav/footer from how-we-do-it/index.html
"""
import os, re

ROOT = "/home/claude/greaterheight.tech"

# ── Load shared blocks ────────────────────────────────────────────────────────
with open(f"{ROOT}/how-we-do-it/index.html", encoding="utf-8") as f:
    TMPL = f.read()

# Full CSS block (lines 35–507 → everything inside <style>...</style>)
# We grab from first /* === to just before </style>
CSS_MATCH = re.search(r'(<style[^>]*>)(.*?)(</style>)', TMPL, re.DOTALL)
SHARED_CSS = CSS_MATCH.group(2)   # everything between <style> and </style>

# Nav block (lines 520–1313)
NAV_BLOCK = re.search(r'(<nav id="main-nav".*?</nav>.*?</div><!--\s*/mobile-nav\s*-->)', TMPL, re.DOTALL)
if not NAV_BLOCK:
    # fallback: grab from <nav ... to id="mobile-nav" closing div
    nav_start = TMPL.index('<nav id="main-nav"')
    # find the </div> that closes #mobile-nav
    mobile_end = TMPL.index('</div>', TMPL.index('id="mobile-nav"'))
    # advance past a few more </div>s to get the full block
    NAV_HTML = TMPL[nav_start:mobile_end+6]
else:
    NAV_HTML = NAV_BLOCK.group(1)

# More reliable extraction: grab nav + mobile-nav as one block
nav_start = TMPL.find('<nav id="main-nav"')
# The mobile nav ends with </div>\n</div> after id="mobile-nav" section
# Find the closing pattern
mobile_nav_start = TMPL.find('<div id="mobile-nav"', nav_start)
# mobile-nav ends at its own </div>
# It has nested divs; count depth
pos = mobile_nav_start
depth = 0
i = pos
while i < len(TMPL):
    if TMPL[i:i+4] == '<div':
        depth += 1
        i += 4
    elif TMPL[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1
NAV_HTML = TMPL[nav_start:i]

# Footer block
footer_start = TMPL.find('<footer>')
footer_end = TMPL.find('</footer>') + 9
FOOTER_HTML = TMPL[footer_start:footer_end]

# Scroll progress bar — self-contained empty div
SCROLLPROG_HTML = '<div id="scroll-progress" aria-hidden="true"></div>'

# Preloader — use depth-counting to capture the full outer div
_pl_start = TMPL.find('<div id="preloader"')
_i = _pl_start
_depth = 0
while _i < len(TMPL):
    if TMPL[_i:_i+4] == '<div':
        _depth += 1; _i += 4
    elif TMPL[_i:_i+6] == '</div>':
        _depth -= 1; _i += 6
        if _depth == 0:
            break
    else:
        _i += 1
PRELOADER_HTML = TMPL[_pl_start:_i]

# Back-to-top button
backtop_start = TMPL.find('<button id="back-top"')
backtop_end = TMPL.find('</button>', backtop_start) + 9
BACKTOP_HTML = TMPL[backtop_start:backtop_end]

# Search overlay
search_start = TMPL.find('<div id="search-overlay"')
search_end = TMPL.find('</div>', TMPL.find('</div>', search_end := TMPL.find('</form>', search_start))+6)+6
# simpler: find it by landmark comment
so_start = TMPL.find('<div id="search-overlay"')
# count divs
pos = so_start
depth = 0
i = pos
while i < len(TMPL):
    if TMPL[i:i+4] == '<div':
        depth += 1
        i += 4
    elif TMPL[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1
SEARCH_HTML = TMPL[so_start:i]

# Cookie banner
cb_start = TMPL.find('<div id="cookie-overlay"')
pos = cb_start
depth = 0
i = pos
while i < len(TMPL):
    if TMPL[i:i+4] == '<div':
        depth += 1
        i += 4
    elif TMPL[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1
COOKIE_HTML = TMPL[cb_start:i]

# Full JS block (from <script> before </body> to end)
js_start = TMPL.rfind('<script>')
js_end = TMPL.rfind('</script>') + 9
JS_BLOCK = TMPL[js_start:js_end]

# Google Fonts link
FONTS_LINK = '<link href="https://fonts.googleapis.com/css2?family=Lato:wght@100;300;400;700&display=swap" rel="stylesheet">'

# ── Path helper ───────────────────────────────────────────────────────────────
def asset_path(url_path):
    """Given a URL path like /about or /services/ai-engineering, return asset prefix"""
    depth = url_path.strip('/').count('/') + 1
    return '../' * depth

def fix_logo_path(html, prefix):
    """Replace the template logo path (1 level up) with the correct prefix"""
    # Template uses ../assets/... (1 level up from how-we-do-it/)
    return html.replace('../assets/', f'{prefix}assets/')

# ── Page builder ─────────────────────────────────────────────────────────────
def build_page(url_path, title, meta_desc, og_image, schema_json, page_css, page_html, aria_current_href=None):
    """
    Build a complete HTML page.
    aria_current_href: the href value in the nav that should get aria-current="page"
                       e.g. "/industries/" for industry pages
    """
    prefix = asset_path(url_path)
    canonical = f"https://greaterheight.tech{url_path}/"

    # Fix all asset paths in nav and footer
    nav = fix_logo_path(NAV_HTML, prefix)
    footer = fix_logo_path(FOOTER_HTML, prefix)

    # Remove aria-current="page" from How We Do It nav item (it's set in template)
    nav = nav.replace(' aria-current="page"', '')

    # Add aria-current to the correct nav link if specified
    if aria_current_href:
        nav = nav.replace(f'href="{aria_current_href}"', f'href="{aria_current_href}" aria-current="page"', 1)

    preloader = fix_logo_path(PRELOADER_HTML, prefix)

    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | GreaterHeight Technologies</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title} | GreaterHeight Technologies">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="https://greaterheight.tech/assets/images/og/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{prefix}assets/images/logo/favicon.png">
<link rel="apple-touch-icon" href="{prefix}assets/images/logo/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS_LINK}
<script type="application/ld+json">
{schema_json}
</script>
<style>
{SHARED_CSS}
/* =============================================
   PAGE-SPECIFIC
============================================= */
{page_css}
</style>
</head>
<body>
{SCROLLPROG_HTML}
{preloader}
{nav}
{page_html}
{footer}
{BACKTOP_HTML}
{SEARCH_HTML}
{COOKIE_HTML}
{JS_BLOCK}
</body>
</html>"""

# ── Schema helpers ─────────────────────────────────────────────────────────────
ORG = '''{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "GreaterHeight Technologies",
  "url": "https://greaterheight.tech",
  "logo": "https://greaterheight.tech/assets/images/logo/greaterheight-logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "17B Debo Aina Street, Omole Phase 1",
    "addressLocality": "Ikeja, Lagos",
    "addressCountry": "NG"
  }
}'''

def webpage_schema(url, name, desc):
    return f'''{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "https://greaterheight.tech{url}/",
  "name": "{name}",
  "description": "{desc}",
  "publisher": {{
    "@type": "Organization",
    "name": "GreaterHeight Technologies",
    "url": "https://greaterheight.tech"
  }}
}}'''

def article_schema(url, headline, desc, date_pub="2024-06-01", date_mod="2026-01-15"):
    return f'''{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{headline}",
  "url": "https://greaterheight.tech{url}/",
  "datePublished": "{date_pub}",
  "dateModified": "{date_mod}",
  "publisher": {{
    "@type": "Organization",
    "name": "GreaterHeight Technologies",
    "logo": "https://greaterheight.tech/assets/images/logo/greaterheight-logo.png"
  }}
}}'''

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════════

PAGES = []

# ── HERO CSS reused across many pages ──────────────────────────────────────────
HERO_CSS = """
.page-hero{background:linear-gradient(135deg,var(--forest-deep) 0%,var(--teal) 100%);padding:5rem 0 4rem;color:#fff;text-align:center;}
.page-hero .eyebrow{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--mint);font-weight:700;margin-bottom:1rem;}
.page-hero h1{font-size:clamp(2rem,4vw,3.2rem);font-weight:700;line-height:1.15;margin-bottom:1.25rem;}
.page-hero .hero-lead{font-size:1.1rem;line-height:1.75;max-width:680px;margin:0 auto 2rem;color:rgba(255,255,255,.85);}
.hero-cta-row{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;}
.btn-primary{display:inline-block;padding:.85rem 2.2rem;background:var(--cr);color:#fff;border-radius:4px;font-size:.88rem;font-weight:700;text-decoration:none;transition:background .2s;}
.btn-primary:hover{background:var(--cr-mid);}
.btn-secondary{display:inline-block;padding:.85rem 2.2rem;background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.5);border-radius:4px;font-size:.88rem;font-weight:700;text-decoration:none;transition:border-color .2s,color .2s;}
.btn-secondary:hover{border-color:#fff;color:#fff;}

.section{padding:4rem 0;}
.section-alt{background:var(--bg-2);}
.section h2{font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;color:var(--forest-deep);margin-bottom:1.2rem;}
.section h3{font-size:1.1rem;font-weight:700;color:var(--forest-deep);margin-bottom:.6rem;}
.section p{line-height:1.8;color:var(--txt-2);margin-bottom:1rem;}
.lead-p{font-size:1.05rem;max-width:720px;}

.cards-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1.5rem;margin-top:2rem;}
.card{background:#fff;border-radius:8px;padding:2rem;border:1px solid var(--border);transition:box-shadow .2s,transform .2s;}
.card:hover{box-shadow:0 8px 28px rgba(0,0,0,.1);transform:translateY(-3px);}
.card-icon{width:48px;height:48px;background:linear-gradient(135deg,var(--forest),var(--teal));border-radius:10px;display:flex;align-items:center;justify-content:center;margin-bottom:1.2rem;}
.card-icon svg{width:24px;height:24px;stroke:#fff;fill:none;stroke-width:1.8;}
.card h3{font-size:1rem;font-weight:700;color:var(--forest-deep);margin-bottom:.5rem;}
.card p{font-size:.88rem;line-height:1.7;color:var(--txt-2);margin:0;}

.cta-band{background:linear-gradient(135deg,var(--forest-deep),var(--teal));padding:4rem 0;text-align:center;color:#fff;}
.cta-band h2{font-size:clamp(1.5rem,3vw,2.2rem);font-weight:700;margin-bottom:1rem;}
.cta-band p{font-size:1rem;color:rgba(255,255,255,.85);max-width:580px;margin:0 auto 2rem;}

.two-col{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start;}
@media(max-width:768px){.two-col{grid-template-columns:1fr;}.cards-grid{grid-template-columns:1fr;}}
"""

STAT_CSS = """
.stats-row{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:1.5rem;margin-top:2.5rem;}
.stat-box{text-align:center;padding:1.5rem 1rem;background:#fff;border-radius:8px;border:1px solid var(--border);}
.stat-num{font-size:2.2rem;font-weight:900;color:var(--cr);line-height:1;}
.stat-label{font-size:.78rem;color:var(--txt-3);margin-top:.4rem;line-height:1.4;}
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. /about  — Who We Are hub
# ═══════════════════════════════════════════════════════════════════════════════
about_css = HERO_CSS + STAT_CSS + """
.about-nav-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1.25rem;margin-top:2rem;}
.about-nav-card{display:flex;flex-direction:column;gap:.5rem;padding:1.5rem;background:#fff;border:1px solid var(--border);border-radius:8px;text-decoration:none;color:inherit;transition:box-shadow .2s,transform .2s;}
.about-nav-card:hover{box-shadow:0 6px 22px rgba(0,0,0,.1);transform:translateY(-2px);}
.about-nav-card span{font-size:.75rem;text-transform:uppercase;letter-spacing:.1em;color:var(--teal-mid);font-weight:700;}
.about-nav-card strong{font-size:1rem;color:var(--forest-deep);font-weight:700;}
.about-nav-card p{font-size:.85rem;color:var(--txt-2);line-height:1.6;margin:0;}
"""

about_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Who We Are</div>
      <h1>Building Africa's Premier<br>Technology Partner</h1>
      <p class="hero-lead">Founded in 2010, GreaterHeight Technologies has grown from a Lagos-based consultancy into a full-spectrum AI-augmented engineering company — serving clients across Africa, Europe, and North America.</p>
      <div class="hero-cta-row">
        <a href="/who-we-are/company-overview/" class="btn-primary">Our Story</a>
        <a href="/contact/" class="btn-secondary">Work With Us</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stats-row reveal">
        <div class="stat-box"><div class="stat-num">15+</div><div class="stat-label">Years Delivering Excellence</div></div>
        <div class="stat-box"><div class="stat-num">200+</div><div class="stat-label">Projects Shipped</div></div>
        <div class="stat-box"><div class="stat-num">40+</div><div class="stat-label">Expert Engineers</div></div>
        <div class="stat-box"><div class="stat-num">3</div><div class="stat-label">Continents Served</div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <h2>Explore Who We Are</h2>
      <p class="lead-p">From our founding story to our team culture, everything that shapes GreaterHeight is documented here.</p>
      <div class="about-nav-grid reveal">
        <a href="/who-we-are/company-overview/" class="about-nav-card">
          <span>Foundation</span>
          <strong>Company Overview</strong>
          <p>Our history, mission, and what drives us to deliver excellence every engagement.</p>
        </a>
        <a href="/who-we-are/core-purpose-mission/" class="about-nav-card">
          <span>Direction</span>
          <strong>Purpose &amp; Mission</strong>
          <p>The core belief and strategic intent that shapes every decision we make.</p>
        </a>
        <a href="/who-we-are/our-values/" class="about-nav-card">
          <span>Principles</span>
          <strong>Our Values</strong>
          <p>The non-negotiables that guide how we work with clients and each other.</p>
        </a>
        <a href="/who-we-are/our-team/" class="about-nav-card">
          <span>People</span>
          <strong>Leadership Team</strong>
          <p>Meet the strategists, architects, and engineers who lead our practice areas.</p>
        </a>
        <a href="/who-we-are/why-greaterheight/" class="about-nav-card">
          <span>Differentiation</span>
          <strong>Why GreaterHeight?</strong>
          <p>What separates us from other technology partners operating in Africa and beyond.</p>
        </a>
        <a href="/culture/" class="about-nav-card">
          <span>Environment</span>
          <strong>Culture &amp; Careers</strong>
          <p>Life inside GreaterHeight — our working culture, development programmes, and open roles.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-col">
      <div class="reveal">
        <h2>Rooted in Nigeria.<br>Trusted Globally.</h2>
        <p>GreaterHeight Technologies began in Lagos with a singular conviction: that world-class software engineering could be built, delivered, and sustained from Africa. Over 15 years later, that conviction has been proven — in production systems running in fintech, healthcare, telecoms, and the public sector.</p>
        <p>We are not an outsourcing vendor. We are a technology partner that embeds alongside your team, brings structured methodology, and exits only when you no longer need us.</p>
        <a href="/who-we-are/company-overview/" class="btn-primary" style="margin-top:1rem;display:inline-block;">Read Our Story</a>
      </div>
      <div class="reveal" style="display:grid;gap:1.2rem;">
        <div class="card">
          <h3>AI-Augmented Teams</h3>
          <p>Every engagement is now AI-enhanced — from code review and test generation to documentation and sprint retrospectives.</p>
        </div>
        <div class="card">
          <h3>Structured Delivery</h3>
          <p>Agile at the team level, programme-managed at the engagement level. Quality gates, sprint reviews, and stakeholder reporting are built in.</p>
        </div>
        <div class="card">
          <h3>Domain Expertise</h3>
          <p>Deep specialisation in fintech, healthcare, public sector, and telecoms — the industries that demand the highest standards.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Ready to build something that lasts?</h2>
      <p>Tell us what you're trying to achieve. We'll tell you how we'd approach it.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/case-studies/" class="btn-secondary">See Our Work</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/about",
    "title": "About GreaterHeight Technologies",
    "meta": "Learn about GreaterHeight Technologies — a Lagos-based AI-augmented engineering firm serving clients across Africa, Europe and North America since 2010.",
    "og": "about.jpg",
    "schema": webpage_schema("/about", "About GreaterHeight Technologies", "Learn about GreaterHeight Technologies — AI-augmented software engineering from Lagos."),
    "css": about_css,
    "html": about_html,
    "aria": "/who-we-are/company-overview/",
})

# ═══════════════════════════════════════════════════════════════════════════════
# 2. /culture  — Culture hub
# ═══════════════════════════════════════════════════════════════════════════════
culture_css = HERO_CSS + """
.culture-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1.5rem;margin-top:2rem;}
.culture-card{background:#fff;border-radius:8px;overflow:hidden;border:1px solid var(--border);text-decoration:none;color:inherit;display:flex;flex-direction:column;transition:box-shadow .2s,transform .2s;}
.culture-card:hover{box-shadow:0 8px 28px rgba(0,0,0,.12);transform:translateY(-3px);}
.culture-card-top{background:linear-gradient(135deg,var(--forest),var(--teal-mid));padding:2rem;color:#fff;}
.culture-card-top h3{font-size:1.1rem;font-weight:700;margin-bottom:.5rem;}
.culture-card-top p{font-size:.85rem;opacity:.85;line-height:1.6;}
.culture-card-bottom{padding:1.25rem 1.5rem;font-size:.88rem;color:var(--cr);font-weight:700;display:flex;align-items:center;gap:.4rem;}
"""

culture_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Life at GreaterHeight</div>
      <h1>Where Ambition Meets<br>Meaningful Work</h1>
      <p class="hero-lead">We don't just build software — we build careers. Our culture is rooted in continuous learning, ownership, and the belief that great engineers deserve a great environment.</p>
      <div class="hero-cta-row">
        <a href="/culture/career-opportunities/" class="btn-primary">View Open Roles</a>
        <a href="/culture/career-overview/" class="btn-secondary">Life at GHT</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Explore Our Culture</h2>
      <p class="lead-p">From your first day to your tenth year, GreaterHeight is built to help you grow.</p>
      <div class="culture-grid reveal">
        <a href="/culture/career-overview/" class="culture-card">
          <div class="culture-card-top">
            <h3>Career Overview</h3>
            <p>Understand what a career at GreaterHeight looks like — growth paths, mentorship structures, and what we expect from every team member.</p>
          </div>
          <div class="culture-card-bottom">Explore Career Path →</div>
        </a>
        <a href="/culture/career-opportunities/" class="culture-card">
          <div class="culture-card-top">
            <h3>Open Opportunities</h3>
            <p>Browse active roles across engineering, design, data, marketing, and business operations.</p>
          </div>
          <div class="culture-card-bottom">See Open Roles →</div>
        </a>
        <a href="/culture/csr/" class="culture-card">
          <div class="culture-card-top">
            <h3>Social Responsibility</h3>
            <p>How GreaterHeight gives back — from free tech education in underserved communities to public-sector pro-bono engagements.</p>
          </div>
          <div class="culture-card-bottom">Our CSR Programme →</div>
        </a>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap two-col">
      <div class="reveal">
        <h2>What We Stand For</h2>
        <p>Engineering culture at GreaterHeight is shaped by three non-negotiables: ownership, transparency, and growth. Every engineer is accountable for their output, every team is transparent about blockers, and every individual has a clear path to the next level.</p>
        <p>We run structured bi-annual performance reviews, quarterly skills assessments, and regular knowledge-sharing sessions that keep the whole team sharp.</p>
      </div>
      <div class="reveal" style="display:grid;gap:1.2rem;">
        <div class="card">
          <h3>Continuous Learning</h3>
          <p>Dedicated learning budget, access to online courses, and internal tech talks every fortnight.</p>
        </div>
        <div class="card">
          <h3>Flexible Working</h3>
          <p>Hybrid and remote-friendly arrangements built around delivery targets, not seat time.</p>
        </div>
        <div class="card">
          <h3>Career Progression</h3>
          <p>Clear engineering ladders from junior through staff and principal — with a people management track available from senior level.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Join the Team</h2>
      <p>We're always looking for engineers who care about craft, delivery, and impact. See what's open.</p>
      <div class="hero-cta-row">
        <a href="/culture/career-opportunities/" class="btn-primary">View Open Roles</a>
        <a href="/contact/" class="btn-secondary">Send a Speculative CV</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/culture",
    "title": "Culture & Careers",
    "meta": "Life at GreaterHeight Technologies — career paths, open roles, CSR, and what it means to be part of a world-class engineering team based in Lagos.",
    "og": "culture.jpg",
    "schema": webpage_schema("/culture", "Culture & Careers at GreaterHeight Technologies", "Life at GreaterHeight — engineering careers, CSR, and open roles in Lagos."),
    "css": culture_css,
    "html": culture_html,
    "aria": "/culture/career-opportunities/",
})

# ═══════════════════════════════════════════════════════════════════════════════
# CASE STUDIES — shared CSS
# ═══════════════════════════════════════════════════════════════════════════════
CS_CSS = HERO_CSS + """
.article-layout{display:grid;grid-template-columns:1fr 320px;gap:3rem;align-items:start;}
.article-body h2{font-size:1.5rem;font-weight:700;color:var(--forest-deep);margin:2.5rem 0 1rem;}
.article-body h3{font-size:1.1rem;font-weight:700;color:var(--forest-deep);margin:1.8rem 0 .7rem;}
.article-body p{line-height:1.9;color:var(--txt-2);margin-bottom:1.2rem;}
.article-body ul{margin:0 0 1.2rem 1.5rem;color:var(--txt-2);line-height:1.8;}
.article-body blockquote{border-left:4px solid var(--teal-glow);padding:1rem 1.5rem;background:var(--bg-2);border-radius:0 6px 6px 0;margin:2rem 0;font-style:italic;color:var(--txt);}
.sidebar-box{background:var(--bg-2);border-radius:8px;padding:1.5rem;border:1px solid var(--border);margin-bottom:1.5rem;}
.sidebar-box h3{font-size:.85rem;text-transform:uppercase;letter-spacing:.1em;color:var(--teal-mid);font-weight:700;margin-bottom:1rem;}
.sidebar-row{display:flex;justify-content:space-between;padding:.5rem 0;border-bottom:1px solid var(--border);font-size:.88rem;}
.sidebar-row:last-child{border-bottom:none;}
.sidebar-row span:first-child{color:var(--txt-3);}
.sidebar-row span:last-child{font-weight:700;color:var(--forest-deep);}
.result-pill{display:inline-block;background:var(--forest-deep);color:#fff;padding:.3rem .9rem;border-radius:20px;font-size:.8rem;font-weight:700;margin:.25rem .15rem;}
@media(max-width:900px){.article-layout{grid-template-columns:1fr;}}
"""

# ── Case Study 1: AI Telehealth ────────────────────────────────────────────────
cs1_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Case Study — Healthcare &amp; AI</div>
      <h1>AI-Powered Telehealth Platform<br>for a Pan-African Health Network</h1>
      <p class="hero-lead">How GreaterHeight built a scalable, ML-driven telehealth system that reduced diagnostic wait times by 60% and expanded specialist access to rural communities across five African countries.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap article-layout">
      <div class="article-body reveal">
        <h2>The Challenge</h2>
        <p>Our client — a pan-African health network operating in Nigeria, Ghana, Kenya, Rwanda, and Senegal — faced a critical bottleneck: too few specialists, too many patients, and diagnostic delays that were costing lives. Patients in rural areas were waiting up to 14 days for specialist consultations that could take 20 minutes via video.</p>
        <p>They needed a telehealth platform that could triage patients intelligently, route cases to the right specialists, generate preliminary AI-assisted diagnostic notes, and operate on low-bandwidth mobile connections.</p>

        <h2>Our Approach</h2>
        <h3>Phase 1: Discovery and Architecture (Weeks 1–6)</h3>
        <p>We began with a clinical workflow audit across three sites, interviewing 42 clinicians, 8 administrative staff, and 15 patients. This produced a detailed journey map that informed every architectural decision. We recommended a microservices architecture built on Node.js and Python, with a React Native mobile client, deployed on AWS with Nigerian and Kenyan data residency.</p>

        <h3>Phase 2: Core Platform Build (Weeks 7–24)</h3>
        <p>The platform's centrepiece is a triage AI module trained on over 400,000 anonymised clinical cases from the network's 10-year patient records. The model — a gradient-boosted classifier combined with an NLP module for symptom extraction from free-text notes — achieved 87% triage accuracy in internal validation.</p>
        <ul>
          <li>Video consultation engine built on WebRTC with adaptive bitrate streaming</li>
          <li>AI-generated consultation summaries using a fine-tuned LLM</li>
          <li>Real-time translation between English, French, Swahili, and Hausa</li>
          <li>Offline-first mobile app with sync-on-reconnect for low-connectivity zones</li>
          <li>EHR integration via FHIR R4 with existing hospital management systems</li>
        </ul>

        <h3>Phase 3: Rollout and Optimisation (Weeks 25–36)</h3>
        <p>We ran a phased rollout — starting with two clinics in Lagos and Nairobi before expanding to all 34 network sites. Each rollout phase was preceded by a 2-day on-site training programme for clinical and administrative staff.</p>

        <blockquote>"GreaterHeight didn't just build software. They embedded with our clinical teams, understood our workflows, and built something our doctors actually use. That's rare."<br>— Chief Medical Officer, Pan-African Health Network</blockquote>

        <h2>Results</h2>
        <p>Twelve months after full deployment, the platform was processing over 3,200 consultations per week — up from 480 in-person specialist visits per month.</p>

        <h2>Technologies Used</h2>
        <p>Node.js, Python (FastAPI), React Native, PostgreSQL, Redis, AWS (ECS, RDS, S3, CloudFront), TensorFlow, WebRTC, FHIR R4, Docker, Kubernetes.</p>
      </div>

      <aside class="reveal">
        <div class="sidebar-box">
          <h3>Engagement Overview</h3>
          <div class="sidebar-row"><span>Industry</span><span>Healthcare</span></div>
          <div class="sidebar-row"><span>Duration</span><span>36 weeks</span></div>
          <div class="sidebar-row"><span>Team Size</span><span>8 engineers</span></div>
          <div class="sidebar-row"><span>Countries</span><span>5</span></div>
          <div class="sidebar-row"><span>Delivery Model</span><span>Dedicated Pod</span></div>
        </div>
        <div class="sidebar-box">
          <h3>Key Results</h3>
          <div style="display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.5rem;">
            <span class="result-pill">60% less wait time</span>
            <span class="result-pill">3,200+ weekly consults</span>
            <span class="result-pill">87% AI triage accuracy</span>
            <span class="result-pill">34 network sites</span>
            <span class="result-pill">5 languages</span>
          </div>
        </div>
        <div class="sidebar-box">
          <h3>Services Used</h3>
          <div style="display:flex;flex-direction:column;gap:.5rem;margin-top:.5rem;">
            <a href="/what-we-do/ai/" style="color:var(--cr);font-size:.88rem;font-weight:600;">AI Engineering</a>
            <a href="/what-we-do/engineering/custom-software/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Custom Software Development</a>
            <a href="/services/delivery-pods/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Delivery Pods</a>
          </div>
        </div>
        <div style="margin-top:1.5rem;">
          <a href="/contact/" class="btn-primary" style="width:100%;text-align:center;display:block;">Discuss Your Project</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Building something in healthcare or AI?</h2>
      <p>Our team has deep expertise in regulated industries, clinical workflows, and production AI systems.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start a Conversation</a>
        <a href="/case-studies/" class="btn-secondary">More Case Studies</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/case-studies/ai-telehealth",
    "title": "AI-Powered Telehealth Platform — Case Study",
    "meta": "How GreaterHeight built an ML-driven telehealth platform that cut diagnostic wait times by 60% across a five-country African health network.",
    "og": "case-studies.jpg",
    "schema": article_schema("/case-studies/ai-telehealth", "AI-Powered Telehealth Platform Case Study", "ML-driven telehealth system for a pan-African health network — 60% faster diagnostics."),
    "css": CS_CSS,
    "html": cs1_html,
    "aria": None,
})

# ── Case Study 2: Fintech Platform ────────────────────────────────────────────
cs2_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Case Study — Financial Technology</div>
      <h1>Core Banking Platform Migration<br>for a Tier-2 Nigerian Lender</h1>
      <p class="hero-lead">How GreaterHeight orchestrated a zero-downtime migration from a legacy core banking system to a modern, cloud-native platform — processing ₦4.2 billion in transactions daily within six months of go-live.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap article-layout">
      <div class="article-body reveal">
        <h2>The Challenge</h2>
        <p>Our client, a CBN-licensed microfinance bank with over 280,000 active customers, was running on a 15-year-old core banking system that could not scale to support their digital lending ambitions. The system was unable to process real-time loan decisions, lacked API connectivity for fintech partnerships, and required 4-hour nightly maintenance windows that cut off digital banking access.</p>

        <h2>Our Approach</h2>
        <h3>Architecture Design and Risk Mitigation</h3>
        <p>The highest risk in any core banking migration is data integrity and transaction continuity. We proposed a parallel-run strategy: both systems would process transactions simultaneously for 90 days, with an automated reconciliation engine comparing outputs in real time. Any discrepancy above ₦1 would trigger an alert and halt the new system's processing of that transaction type.</p>

        <h3>Build Phase</h3>
        <p>We built the new platform on a microservices architecture — 14 bounded services covering accounts, loans, transactions, notifications, compliance, and reporting — deployed on AWS using ECS Fargate with an Aurora PostgreSQL cluster in multi-AZ configuration.</p>
        <ul>
          <li>Real-time loan decision engine using rule-based scoring augmented by an ML credit model</li>
          <li>Open Banking API layer (RESTful + ISO 20022) for fintech partner integrations</li>
          <li>Automated CBN regulatory reporting with zero manual intervention</li>
          <li>End-to-end encryption at rest and in transit, ISO 27001-aligned</li>
        </ul>

        <blockquote>"The parallel-run approach gave our board the confidence that we weren't gambling with our customers' money. GreaterHeight's risk management discipline was exceptional."<br>— Managing Director, Microfinance Bank</blockquote>

        <h2>Results</h2>
        <p>Go-live was achieved with zero unplanned downtime. Within six months, the bank had launched three new digital lending products, onboarded four fintech API partners, and eliminated its nightly maintenance window entirely.</p>

        <h2>Technologies Used</h2>
        <p>Java (Spring Boot), Node.js, React, AWS (ECS Fargate, Aurora, SQS, SNS, CloudWatch), PostgreSQL, Redis, Docker, Terraform, ISO 20022, Open Banking API standards.</p>
      </div>

      <aside class="reveal">
        <div class="sidebar-box">
          <h3>Engagement Overview</h3>
          <div class="sidebar-row"><span>Industry</span><span>Fintech / Banking</span></div>
          <div class="sidebar-row"><span>Duration</span><span>52 weeks</span></div>
          <div class="sidebar-row"><span>Team Size</span><span>11 engineers</span></div>
          <div class="sidebar-row"><span>Delivery Model</span><span>Dedicated Pod</span></div>
        </div>
        <div class="sidebar-box">
          <h3>Key Results</h3>
          <div style="display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.5rem;">
            <span class="result-pill">Zero downtime go-live</span>
            <span class="result-pill">₦4.2B daily transactions</span>
            <span class="result-pill">3 new products launched</span>
            <span class="result-pill">4 fintech partners</span>
          </div>
        </div>
        <div style="margin-top:1.5rem;">
          <a href="/contact/" class="btn-primary" style="width:100%;text-align:center;display:block;">Discuss Your Project</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Modernising a financial platform?</h2>
      <p>We've done it before — with zero customer disruption. Let's talk about your migration.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/case-studies/" class="btn-secondary">More Case Studies</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/case-studies/fintech-platform",
    "title": "Core Banking Platform Migration — Case Study",
    "meta": "How GreaterHeight Technologies orchestrated a zero-downtime core banking migration for a Nigerian lender, now processing ₦4.2 billion in transactions daily.",
    "og": "case-studies.jpg",
    "schema": article_schema("/case-studies/fintech-platform", "Core Banking Platform Migration Case Study", "Zero-downtime core banking migration for a Nigerian microfinance bank."),
    "css": CS_CSS,
    "html": cs2_html,
    "aria": None,
})

# ── Case Study 3: Salon Booking ───────────────────────────────────────────────
cs3_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Case Study — Consumer Tech</div>
      <h1>Beauty-on-Demand: Scaling a Salon<br>Booking Marketplace Across Nigeria</h1>
      <p class="hero-lead">How GreaterHeight built, launched, and scaled a multi-vendor beauty services marketplace from MVP to 12,000 monthly active users in under 18 months — with an average booking completion rate of 91%.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap article-layout">
      <div class="article-body reveal">
        <h2>The Challenge</h2>
        <p>The client — a Lagos-based startup with a proven offline network of 400+ salons — needed to digitise their business model before a well-funded competitor entered the market. They had 90 days to MVP and a budget constrained by seed funding.</p>
        <p>The technical complexity was significant: real-time slot management across 400 vendors, in-app payments via multiple Nigerian payment gateways, geolocation-based discovery, and a loyalty programme with its own points economy.</p>

        <h2>Our Approach</h2>
        <h3>MVP in 90 Days</h3>
        <p>We made deliberate scope decisions to hit the deadline. The MVP launched with: vendor discovery (location + category), real-time slot booking, Paystack and Flutterwave integration, and push notifications. Everything else — loyalty points, reviews, in-app messaging — was scheduled for Phase 2.</p>

        <h3>Platform Architecture</h3>
        <p>The backend was built as a monolith-first architecture — a deliberate choice given the 90-day timeline — with clean domain boundaries that allowed us to extract services in Phase 2 without a rewrite. The mobile apps (iOS and Android) were built in React Native to share 85% of code between platforms.</p>
        <ul>
          <li>Real-time slot management with optimistic locking to prevent double-bookings</li>
          <li>Geofenced push notifications triggering when users enter target areas</li>
          <li>Vendor dashboard with analytics, booking management, and payout tracking</li>
          <li>AI-powered service recommendation engine (Phase 2) trained on booking history</li>
          <li>Automated vendor payout via Flutterwave transfers API</li>
        </ul>

        <blockquote>"We went from zero to 12,000 users in 18 months. The booking reliability is what kept people coming back — GreaterHeight built that in from day one."<br>— CEO, Beauty Marketplace</blockquote>

        <h2>Results</h2>
        <p>18 months post-launch: 12,000 monthly active users, 400+ vendor partners, ₦180M in GMV processed, and 91% booking completion rate. The AI recommendation engine (Phase 2) increased repeat booking rate by 34%.</p>

        <h2>Technologies Used</h2>
        <p>Node.js, React Native, PostgreSQL, Redis, AWS (ECS, RDS, ElastiCache, SES, SNS), Paystack, Flutterwave, Python (ML recommendation), Firebase (push notifications).</p>
      </div>

      <aside class="reveal">
        <div class="sidebar-box">
          <h3>Engagement Overview</h3>
          <div class="sidebar-row"><span>Industry</span><span>Consumer Tech</span></div>
          <div class="sidebar-row"><span>Duration</span><span>MVP 90 days + Scale</span></div>
          <div class="sidebar-row"><span>Team Size</span><span>6 engineers</span></div>
          <div class="sidebar-row"><span>Delivery Model</span><span>Project</span></div>
        </div>
        <div class="sidebar-box">
          <h3>Key Results</h3>
          <div style="display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.5rem;">
            <span class="result-pill">12K monthly users</span>
            <span class="result-pill">91% booking rate</span>
            <span class="result-pill">₦180M GMV</span>
            <span class="result-pill">400+ vendors</span>
            <span class="result-pill">34% repeat uplift</span>
          </div>
        </div>
        <div style="margin-top:1.5rem;">
          <a href="/contact/" class="btn-primary" style="width:100%;text-align:center;display:block;">Discuss Your Project</a>
        </div>
      </aside>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Building a marketplace or consumer platform?</h2>
      <p>We know how to scope an MVP that works, then scale it without a rewrite.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/case-studies/" class="btn-secondary">More Case Studies</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/case-studies/salon-booking",
    "title": "Beauty-on-Demand Salon Booking Marketplace — Case Study",
    "meta": "How GreaterHeight built and scaled a salon booking marketplace from MVP to 12,000 monthly active users in 18 months, processing ₦180M in GMV.",
    "og": "case-studies.jpg",
    "schema": article_schema("/case-studies/salon-booking", "Beauty-on-Demand Salon Booking Marketplace Case Study", "Salon booking marketplace from MVP to 12K users in 18 months."),
    "css": CS_CSS,
    "html": cs3_html,
    "aria": None,
})

# ═══════════════════════════════════════════════════════════════════════════════
# INDUSTRIES — shared CSS + 3 pages
# ═══════════════════════════════════════════════════════════════════════════════
IND_CSS = HERO_CSS + STAT_CSS + """
.challenge-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1.25rem;margin-top:1.5rem;}
.challenge-item{padding:1.5rem;background:#fff;border-radius:8px;border-left:4px solid var(--cr);border:1px solid var(--border);}
.challenge-item h3{font-size:.95rem;font-weight:700;color:var(--forest-deep);margin-bottom:.5rem;}
.challenge-item p{font-size:.85rem;color:var(--txt-2);line-height:1.6;margin:0;}
"""

def industry_page(slug, title, eyebrow, headline, lead, stats, challenges_title, challenges, services_title, services_items, cta_text, aria_href="/industries/"):
    challenges_html = "\n".join([
        f'<div class="challenge-item reveal"><h3>{c["title"]}</h3><p>{c["body"]}</p></div>'
        for c in challenges
    ])
    services_html = "\n".join([
        f'<div class="card reveal"><h3>{s["title"]}</h3><p>{s["body"]}</p></div>'
        for s in services_items
    ])
    stats_html = "\n".join([
        f'<div class="stat-box"><div class="stat-num">{s["num"]}</div><div class="stat-label">{s["label"]}</div></div>'
        for s in stats
    ])
    return f"""
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">{eyebrow}</div>
      <h1>{headline}</h1>
      <p class="hero-lead">{lead}</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/case-studies/" class="btn-secondary">See Case Studies</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stats-row reveal">{stats_html}</div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <h2>{challenges_title}</h2>
      <div class="challenge-grid">{challenges_html}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>{services_title}</h2>
      <div class="cards-grid">{services_html}</div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>{cta_text}</h2>
      <p>Tell us what you're building. We'll bring the team, the methodology, and the domain knowledge.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Get in Touch</a>
        <a href="/case-studies/" class="btn-secondary">Our Work</a>
      </div>
    </div>
  </section>
</main>
"""

# Oil & Gas
PAGES.append({
    "path": "/industries/oil-gas",
    "title": "Technology Solutions for Oil & Gas",
    "meta": "GreaterHeight Technologies delivers operational technology, data engineering, and enterprise software solutions for oil and gas operators across Nigeria and Africa.",
    "og": "industries.jpg",
    "schema": webpage_schema("/industries/oil-gas", "Technology Solutions for Oil & Gas", "Software engineering and data solutions for the oil and gas industry."),
    "css": IND_CSS,
    "html": industry_page(
        "oil-gas",
        "Oil &amp; Gas",
        "Industry — Oil &amp; Gas",
        "Technology That Keeps<br>Operations Running",
        "From upstream field operations to downstream trading and logistics, GreaterHeight builds the enterprise software, data pipelines, and operational technology that keeps oil and gas organisations productive, compliant, and competitive.",
        [
            {"num": "15+", "label": "Years of Enterprise IT Experience"},
            {"num": "99.9%", "label": "Uptime SLA for Mission-Critical Systems"},
            {"num": "40+", "label": "Engineers Across 8 Specialisations"},
            {"num": "ISO", "label": "27001-Aligned Security Practices"},
        ],
        "Industry Challenges We Address",
        [
            {"title": "Operational Data Silos", "body": "Disparate SCADA, ERP, and field data systems that cannot communicate — causing delays, errors, and blind spots in operations management."},
            {"title": "Regulatory Compliance", "body": "DPR and NUPRC reporting obligations, HSE documentation, and audit trails that require accurate, real-time data aggregation."},
            {"title": "Ageing Legacy Systems", "body": "Mission-critical operational systems built on outdated technology that cannot be replaced without risking production continuity."},
            {"title": "Remote Operations", "body": "Field operations in locations with unreliable connectivity, requiring offline-capable applications with reliable sync."},
            {"title": "Asset Management", "body": "Complex equipment lifecycles, maintenance schedules, and inspection records that need a single source of truth."},
            {"title": "Energy Transition Pressure", "body": "Increasing demand for ESG reporting, carbon tracking, and technology to support renewable energy diversification."},
        ],
        "How We Help Oil &amp; Gas Operators",
        [
            {"title": "Operational Technology Integration", "body": "Connecting SCADA, historian, and IoT sensor data into unified dashboards and analytics platforms for real-time operational visibility."},
            {"title": "Asset Management Systems", "body": "Custom EAM solutions tracking equipment lifecycle, predictive maintenance schedules, spare parts inventory, and inspection history."},
            {"title": "Regulatory Reporting Automation", "body": "Automated data pipelines that aggregate production, HSE, and financial data into DPR/NUPRC-compliant reports with audit trails."},
            {"title": "Field Operations Apps", "body": "Offline-capable mobile applications for inspection, maintenance, and incident reporting — built for low-connectivity field environments."},
            {"title": "Data Engineering &amp; Analytics", "body": "Data warehouses and BI dashboards that give operations managers a single view of production, logistics, and financial performance."},
            {"title": "Legacy Modernisation", "body": "Phased migration strategies that incrementally replace ageing core systems without disrupting production — zero big-bang risks."},
        ],
        "Building for the energy sector?",
        "/industries/",
    ),
    "aria": "/industries/",
})

# Public Sector
PAGES.append({
    "path": "/industries/public-sector",
    "title": "Technology Solutions for the Public Sector",
    "meta": "GreaterHeight Technologies builds citizen-facing digital services, e-government platforms, and data systems for Nigerian and African public sector organisations.",
    "og": "industries.jpg",
    "schema": webpage_schema("/industries/public-sector", "Technology Solutions for the Public Sector", "E-government and digital services for public sector organisations in Nigeria and Africa."),
    "css": IND_CSS,
    "html": industry_page(
        "public-sector",
        "Public Sector",
        "Industry — Public Sector",
        "Digital Government Services<br>That Serve Every Citizen",
        "GreaterHeight Technologies partners with federal ministries, state agencies, and local authorities to build citizen-facing digital services, interoperable data platforms, and administrative systems that improve governance and public service delivery.",
        [
            {"num": "10+", "label": "Government Engagements Delivered"},
            {"num": "1M+", "label": "Citizens Served Through Our Platforms"},
            {"num": "100%", "label": "Compliance With NITDA Data Guidelines"},
            {"num": "5", "label": "States Across the Niger Delta &amp; SW Nigeria"},
        ],
        "Public Sector Technology Challenges",
        [
            {"title": "Fragmented Citizen Records", "body": "Multiple agencies holding duplicate, inconsistent citizen data — preventing effective service delivery and benefit administration."},
            {"title": "Paper-Based Processes", "body": "Manual workflows for permits, licences, and registrations that create bottlenecks, corruption risks, and poor citizen experience."},
            {"title": "Procurement Complexity", "body": "FMFBNP procurement regulations and BPP requirements that demand transparent, auditable technology spending."},
            {"title": "Data Security", "body": "Sensitive citizen data requiring strict access controls, audit logs, and compliance with NDPR and NITDA data governance frameworks."},
            {"title": "Interoperability", "body": "Systems that cannot share data across ministries, departments, and agencies — duplicating effort and creating service gaps."},
            {"title": "Citizen Trust", "body": "History of failed government technology projects that have eroded public confidence in digital government services."},
        ],
        "Our Public Sector Capabilities",
        [
            {"title": "Citizen Portal Development", "body": "Self-service web and mobile portals for permits, licences, registrations, tax payments, and benefits — accessible on low-end devices."},
            {"title": "E-Government Platforms", "body": "End-to-end digitisation of government services — from application intake through workflow management, decision support, and certificate issuance."},
            {"title": "Identity &amp; Registry Systems", "body": "Secure citizen identity management, biometric integration, and enterprise registries with de-duplication and data quality controls."},
            {"title": "Interoperability Middleware", "body": "API gateways and integration layers that enable data sharing across ministries and agencies while respecting data sovereignty."},
            {"title": "Revenue Management Systems", "body": "Electronic billing, payment processing, and reconciliation for IGR — integrated with Remita and state treasury systems."},
            {"title": "Data Governance &amp; Analytics", "body": "NDPR-compliant data warehouses and dashboards that give policy makers real-time visibility of service delivery metrics."},
        ],
        "Working on a government technology programme?",
        "/industries/",
    ),
    "aria": "/industries/",
})

# Telecoms
PAGES.append({
    "path": "/industries/telecoms",
    "title": "Technology Solutions for Telecommunications",
    "meta": "GreaterHeight Technologies delivers BSS/OSS integration, subscriber management, network analytics, and digital transformation solutions for telecoms operators.",
    "og": "industries.jpg",
    "schema": webpage_schema("/industries/telecoms", "Technology Solutions for Telecommunications", "BSS/OSS integration and digital transformation for telecoms operators."),
    "css": IND_CSS,
    "html": industry_page(
        "telecoms",
        "Telecommunications",
        "Industry — Telecommunications",
        "Engineering for the Networks<br>That Connect Africa",
        "From BSS/OSS integration to subscriber analytics and VAS platform development, GreaterHeight Technologies builds and maintains the software systems that power Nigeria's leading telecommunications operators.",
        [
            {"num": "8+", "label": "Telecoms Engagements Delivered"},
            {"num": "50M+", "label": "Subscribers Touched by Our Systems"},
            {"num": "99.99%", "label": "Network Software Availability Target"},
            {"num": "24/7", "label": "On-Call Support for Critical Systems"},
        ],
        "Telecoms Technology Challenges",
        [
            {"title": "BSS/OSS Integration Complexity", "body": "Heterogeneous billing, provisioning, and network management systems from multiple vendors that need seamless orchestration."},
            {"title": "Subscriber Churn", "body": "High churn in a competitive market requiring real-time analytics, personalisation engines, and targeted retention programmes."},
            {"title": "VAS Revenue Diversification", "body": "Pressure to grow non-voice revenue through mobile money, content platforms, IoT connectivity, and enterprise data services."},
            {"title": "Network Analytics at Scale", "body": "Processing billions of CDRs, network KPIs, and subscriber events in near real-time to drive operational and commercial decisions."},
            {"title": "Fraud Prevention", "body": "Subscription fraud, SIM swap fraud, and roaming abuse costing operators millions annually — requiring real-time detection systems."},
            {"title": "Regulatory Compliance", "body": "NCC licensing, QoS measurement, subscriber registration, and lawful intercept obligations requiring robust data and audit capabilities."},
        ],
        "Our Telecoms Capabilities",
        [
            {"title": "BSS/OSS Integration", "body": "API-led integration of billing, mediation, provisioning, and network management systems — enabling seamless end-to-end subscriber lifecycle management."},
            {"title": "VAS Platform Development", "body": "Custom value-added service platforms — mobile content, SMS aggregation, MNO APIs, and digital financial services — built for telco-grade scale."},
            {"title": "Subscriber Analytics &amp; Churn", "body": "ML-driven churn prediction models, segment-based personalisation engines, and next-best-action recommendation systems."},
            {"title": "Revenue Assurance", "body": "Automated reconciliation between network, mediation, and billing systems to identify revenue leakage and reduce unbilled traffic."},
            {"title": "Fraud Management", "body": "Real-time fraud detection systems using rule engines and ML models trained on operator-specific fraud patterns."},
            {"title": "Self-Care &amp; Retail Apps", "body": "Customer-facing mobile apps, USSD self-service platforms, and retail agent management systems for subscriber engagement."},
        ],
        "Modernising your telecoms technology stack?",
        "/industries/",
    ),
    "aria": "/industries/",
})

# ═══════════════════════════════════════════════════════════════════════════════
# INSIGHTS PAGES
# ═══════════════════════════════════════════════════════════════════════════════
INS_ARTICLE_CSS = CS_CSS + """
.article-eyebrow{display:flex;gap:1rem;align-items:center;margin-bottom:1.5rem;flex-wrap:wrap;}
.tag-pill{display:inline-block;background:var(--bg-2);border:1px solid var(--border);color:var(--teal-mid);font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;padding:.25rem .75rem;border-radius:20px;}
.reading-time{font-size:.8rem;color:var(--txt-3);}
"""

# African Infrastructure article
ai_article_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Insight — Infrastructure &amp; Development</div>
      <h1>Building Africa's Digital Infrastructure:<br>What the Next Decade Demands</h1>
      <p class="hero-lead">Africa's digital economy cannot reach its potential on legacy infrastructure. Here is what needs to change — and what technology leaders can do right now to position their organisations for the decade ahead.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap article-layout">
      <div class="article-body reveal">
        <div class="article-eyebrow">
          <span class="tag-pill">Infrastructure</span>
          <span class="tag-pill">Strategy</span>
          <span class="reading-time">12 min read · Published January 2026</span>
        </div>

        <h2>The Infrastructure Gap Is a Technology Problem</h2>
        <p>Africa's infrastructure deficit is frequently framed as a finance problem — and it is. The continent requires an estimated $170 billion annually in infrastructure investment, against actual flows of less than $80 billion. But it is equally a technology problem. The infrastructure projects that do receive funding often fail to generate their expected economic returns because the software, data, and integration layers needed to make them productive are absent.</p>
        <p>A port that cannot exchange data with clearing agents in real time is not a modern port. A power grid that cannot dynamically reroute around failures is not a resilient grid. A hospital that cannot access patient records across its own network is not a functional health system. The physical infrastructure exists; the digital infrastructure does not.</p>

        <h2>Five Layers of Digital Infrastructure Africa Needs Now</h2>
        <h3>1. National Identity and Registry Infrastructure</h3>
        <p>Reliable digital identity is the foundation of every other digital service — financial inclusion, social protection, e-government, and health. Yet fewer than half of African countries have interoperable, biometrically-linked national identity systems that serve their full populations. The NIN programme in Nigeria is a significant step, but adoption rates, particularly among rural and older populations, remain insufficient for the system to deliver its full value.</p>

        <h3>2. Payment Infrastructure</h3>
        <p>Africa has made extraordinary progress in mobile payments — M-Pesa in Kenya, Mobile Money interoperability in Ghana, and the rapid expansion of Nigeria's NIBSS infrastructure are genuine achievements. But cross-border payment infrastructure remains fragmented and expensive. A trader in Lagos paying a supplier in Accra in 2026 still faces fees, delays, and correspondent banking friction that would be unacceptable in Europe. The Pan-African Payment and Settlement System (PAPSS) is the right answer — but its adoption is still nascent.</p>

        <h3>3. Data Centre and Cloud Infrastructure</h3>
        <p>Hyperscaler investment is accelerating — AWS, Azure, and Google Cloud now have regions in South Africa and have announced investments in West Africa. But the costs of cloud services in Africa remain significantly higher than in Europe and North America, and latency for applications serving users outside major cities is still a problem. Regional data centres and edge computing nodes are needed in secondary cities — not just Lagos, Nairobi, Johannesburg, and Cairo.</p>

        <h3>4. Connectivity Infrastructure</h3>
        <p>Last-mile connectivity remains the central challenge. Mobile broadband coverage has expanded significantly, but average internet speeds in sub-Saharan Africa lag far behind global averages, and rural areas continue to be severely underserved. The expansion of 5G in Nigerian cities is positive for urban applications, but the more urgent investment is in 4G coverage for the 60% of the population still outside reliable mobile broadband reach.</p>

        <h3>5. Talent Infrastructure</h3>
        <p>Africa produces fewer than 100,000 software engineers annually against a demand that is growing at over 20% per year. The gap is particularly severe in specialist areas — data engineering, security, embedded systems, and AI — where global demand is also at its highest. This is infrastructure too: the universities, vocational programmes, apprenticeships, and corporate academies that produce the builders of everything else.</p>

        <h2>What Technology Leaders Can Do</h2>
        <p>The infrastructure gap is a macro problem, but its solutions begin at the organisational level. Technology leaders in African businesses and public institutions can contribute directly:</p>
        <ul>
          <li><strong>Invest in internal skills development.</strong> Waiting for the talent market to solve itself is a losing strategy. Build internal academies, structured apprenticeships, and clear technical career ladders.</li>
          <li><strong>Build for interoperability from day one.</strong> Every new system your organisation builds should expose clean APIs, use open standards, and avoid proprietary lock-in that will make future integration expensive.</li>
          <li><strong>Champion local data infrastructure.</strong> Where the choice is available, process data locally. This builds the business case for regional data centre investment and keeps data under African regulatory jurisdiction.</li>
          <li><strong>Engage with industry bodies.</strong> CcHUB, NITDA, and similar bodies shape the policy environment. Technology leaders who participate in these conversations help set the conditions for better infrastructure investment.</li>
        </ul>

        <h2>The Opportunity</h2>
        <p>The same infrastructure gap that creates challenges also creates opportunity. The countries and organisations that build digital infrastructure now will capture disproportionate value from Africa's economic growth over the next 20 years. The window to build on relatively uncrowded ground — before dominant platforms establish the network effects that make competition difficult — is open now. It will not remain open indefinitely.</p>

        <blockquote>The question for African technology leaders is not whether to invest in digital infrastructure. It is how fast, and how strategically, to do so before the window closes.</blockquote>
      </div>

      <aside class="reveal">
        <div class="sidebar-box">
          <h3>Article Details</h3>
          <div class="sidebar-row"><span>Category</span><span>Infrastructure</span></div>
          <div class="sidebar-row"><span>Read Time</span><span>12 minutes</span></div>
          <div class="sidebar-row"><span>Published</span><span>Jan 2026</span></div>
          <div class="sidebar-row"><span>Author</span><span>GHT Insights</span></div>
        </div>
        <div class="sidebar-box">
          <h3>Related Services</h3>
          <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:.5rem;">
            <a href="/what-we-do/data/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Data Engineering</a>
            <a href="/what-we-do/enterprise/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Enterprise Technology</a>
            <a href="/services/it-consulting/" style="color:var(--cr);font-size:.88rem;font-weight:600;">IT Consulting</a>
          </div>
        </div>
        <div class="sidebar-box">
          <h3>More Insights</h3>
          <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:.5rem;">
            <a href="/insights/ai-prototypes-production/" style="color:var(--cr);font-size:.88rem;font-weight:600;">From AI Prototype to Production</a>
            <a href="/insights/slow-hiring-cost/" style="color:var(--cr);font-size:.88rem;font-weight:600;">The Hidden Cost of Slow Hiring</a>
            <a href="/insights/" style="color:var(--cr);font-size:.88rem;font-weight:600;">All Insights →</a>
          </div>
        </div>
      </aside>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Building infrastructure for your organisation?</h2>
      <p>We help African businesses and public institutions build the digital foundations that make everything else possible.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Talk to Our Team</a>
        <a href="/insights/" class="btn-secondary">More Insights</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/insights/african-infrastructure",
    "title": "Building Africa's Digital Infrastructure",
    "meta": "What Africa's digital infrastructure gap means for technology leaders — and the five layers that need investment in the next decade.",
    "og": "insights.jpg",
    "schema": article_schema("/insights/african-infrastructure", "Building Africa's Digital Infrastructure: What the Next Decade Demands", "Africa's digital infrastructure gap and what technology leaders can do now."),
    "css": INS_ARTICLE_CSS,
    "html": ai_article_html,
    "aria": None,
})

# AI Prototypes to Production
proto_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Insight — Artificial Intelligence</div>
      <h1>From AI Prototype to Production:<br>Why Most Fail and How to Succeed</h1>
      <p class="hero-lead">Over 80% of enterprise AI projects never make it to production. The bottleneck is rarely the model. Here is what the successful 20% do differently — and the engineering practices that separate a demo from a system your organisation can rely on.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap article-layout">
      <div class="article-body reveal">
        <div class="article-eyebrow">
          <span class="tag-pill">Artificial Intelligence</span>
          <span class="tag-pill">Engineering</span>
          <span class="reading-time">15 min read · Published March 2026</span>
        </div>

        <h2>The Prototype Trap</h2>
        <p>It is remarkably easy to build an AI prototype that impresses. A Jupyter notebook with 200 lines of Python, a pre-trained model from Hugging Face, a sample dataset, and two weeks of experimentation can produce something that looks transformative in a boardroom demo. The accuracy numbers are real. The speed is genuine. The stakeholders are excited.</p>
        <p>Then the engineering team tries to put it into production. And it falls apart.</p>
        <p>The model that worked on 10,000 training samples behaves differently on live data. The inference that took 200ms in the demo takes 4 seconds in the production environment. The input data that was clean in the sample is inconsistent in the real pipeline. The model's outputs need to be explainable for regulatory reasons, but the team built a black box. The retraining cadence was never defined. Nobody owns model monitoring.</p>

        <h2>The Six Failure Modes</h2>
        <h3>1. Data Pipeline Assumptions</h3>
        <p>Prototype data is usually prepared by a data scientist who made dozens of quiet decisions: dropped nulls, normalised distributions, removed outliers, encoded categoricals consistently. Production data arrives raw. The model that was trained on clean data receives inputs the pipeline was never built to handle — and either fails silently or returns nonsense confidently.</p>
        <p>The fix is to build the data pipeline as part of the model, not separately. Data validation, transformation, and anomaly detection must be versioned alongside the model itself.</p>

        <h3>2. Latency and Throughput Requirements</h3>
        <p>A model that runs in 200ms on a data scientist's MacBook Pro will not run in 200ms on the target infrastructure under production load. GPU-accelerated inference is not always available or affordable at scale. Transformer-based models with billions of parameters need careful optimisation — quantisation, distillation, caching, and batching — to meet production SLAs.</p>

        <h3>3. No Model Registry or Versioning</h3>
        <p>In a prototype, there is one model. In production, there are many: the current champion, the challenger being A/B tested, last month's version that some downstream systems still reference, and the experimental version being prepared for the next release. Without a model registry, tracking which version is running where — and rolling back when something goes wrong — is impossible.</p>

        <h3>4. Absent Monitoring and Drift Detection</h3>
        <p>Models degrade. The data distribution that existed when the model was trained will shift over time — markets change, user behaviour changes, the product itself changes. A model with no monitoring will silently become less accurate until someone notices that the downstream metrics have got worse. By then, significant value has been destroyed.</p>

        <h3>5. Explainability and Regulatory Requirements</h3>
        <p>In regulated industries — financial services, healthcare, public sector — decisions made by AI systems need to be explainable. "The model said so" is not an acceptable response to a customer dispute or a regulatory inquiry. This requirement must be built in from the start: techniques like SHAP values, LIME, or attention visualisation need to be part of the system architecture, not retrofitted afterwards.</p>

        <h3>6. No Clear Ownership</h3>
        <p>The final and most common failure mode: nobody owns the model in production. The data science team built it and considers their work done. The engineering team deployed it and considers it the data science team's problem. The business team is using its outputs without understanding its limitations. When something goes wrong — and it will — nobody knows who is responsible.</p>

        <h2>What Successful Production AI Looks Like</h2>
        <p>The organisations that successfully put AI into production share a common pattern: they treat AI systems as software systems, not experiments. That means:</p>
        <ul>
          <li>Defined SLAs for model accuracy, latency, and availability</li>
          <li>Automated retraining pipelines triggered by drift detection</li>
          <li>A/B testing infrastructure for model updates</li>
          <li>Feature stores that ensure consistent data between training and serving</li>
          <li>Model cards documenting intended use, limitations, and training data</li>
          <li>On-call rotation that includes model monitoring alerts</li>
        </ul>

        <blockquote>The difference between a prototype and a production system is not the model. It is everything around the model: the data pipeline, the monitoring, the deployment infrastructure, and the team structure.</blockquote>

        <h2>Practical Advice for Organisations Starting the Journey</h2>
        <p>If you are preparing to take an AI prototype into production, do three things before writing any infrastructure code:</p>
        <ul>
          <li><strong>Define success metrics in production terms,</strong> not model performance terms. Not "95% accuracy" but "fewer than 2% of credit applications incorrectly rejected, with a maximum 500ms decision latency at p99."</li>
          <li><strong>Map your data pipeline end-to-end.</strong> Every transformation from raw source data to model input needs to be documented, tested, and reproducible.</li>
          <li><strong>Assign ownership explicitly.</strong> Who owns model accuracy in production? Who gets paged if it degrades? Who approves a retraining run? Define this before go-live, not after.</li>
        </ul>
      </div>

      <aside class="reveal">
        <div class="sidebar-box">
          <h3>Article Details</h3>
          <div class="sidebar-row"><span>Category</span><span>AI Engineering</span></div>
          <div class="sidebar-row"><span>Read Time</span><span>15 minutes</span></div>
          <div class="sidebar-row"><span>Published</span><span>Mar 2026</span></div>
        </div>
        <div class="sidebar-box">
          <h3>Related Services</h3>
          <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:.5rem;">
            <a href="/what-we-do/ai/" style="color:var(--cr);font-size:.88rem;font-weight:600;">AI Engineering</a>
            <a href="/services/ai-engineering/" style="color:var(--cr);font-size:.88rem;font-weight:600;">AI Engineering Service</a>
            <a href="/what-we-do/data/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Data Engineering</a>
          </div>
        </div>
        <div class="sidebar-box">
          <h3>More Insights</h3>
          <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:.5rem;">
            <a href="/insights/african-infrastructure/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Africa's Digital Infrastructure</a>
            <a href="/insights/slow-hiring-cost/" style="color:var(--cr);font-size:.88rem;font-weight:600;">The Hidden Cost of Slow Hiring</a>
            <a href="/insights/" style="color:var(--cr);font-size:.88rem;font-weight:600;">All Insights →</a>
          </div>
        </div>
      </aside>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Have an AI prototype that needs to go to production?</h2>
      <p>Our AI engineering team has taken models from notebook to production — in fintech, healthcare, and enterprise operations.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Talk to Our Team</a>
        <a href="/what-we-do/ai/" class="btn-secondary">Our AI Practice</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/insights/ai-prototypes-production",
    "title": "From AI Prototype to Production",
    "meta": "Why over 80% of enterprise AI projects fail to reach production — and the engineering practices that separate a successful deployment from a failed demo.",
    "og": "insights.jpg",
    "schema": article_schema("/insights/ai-prototypes-production", "From AI Prototype to Production: Why Most Fail and How to Succeed", "Engineering practices for taking AI from prototype to reliable production system."),
    "css": INS_ARTICLE_CSS,
    "html": proto_html,
    "aria": None,
})

# Slow Hiring Cost article
slow_hiring_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Insight — Talent &amp; Hiring</div>
      <h1>The Hidden Cost of Slow Hiring<br>in Technology Teams</h1>
      <p class="hero-lead">Every open engineering role costs your organisation more than you think. We break down the full cost of a slow hiring process — and explain why the fastest solution is not always the most obvious one.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap article-layout">
      <div class="article-body reveal">
        <div class="article-eyebrow">
          <span class="tag-pill">Talent</span>
          <span class="tag-pill">Engineering Leadership</span>
          <span class="reading-time">8 min read · Published April 2026</span>
        </div>

        <h2>The Visible Cost vs the Real Cost</h2>
        <p>When an engineering role goes unfilled for three months, most finance teams see one line item: the recruiter fee not yet paid. The salary budget sits unspent. On paper, it looks like a saving.</p>
        <p>It is not. The real cost of an unfilled engineering role runs at two to three times the annual salary of the position, when you account for:</p>
        <ul>
          <li><strong>Lost velocity:</strong> Existing engineers absorb the work. Sprint capacity drops. Delivery timelines extend. Features slip.</li>
          <li><strong>Opportunity cost:</strong> The revenue, market position, or operational improvement that the role was hired to deliver is delayed or never realised.</li>
          <li><strong>Team morale:</strong> Consistently overloaded teams experience higher attrition. Each departing engineer restarts the problem at higher cost.</li>
          <li><strong>Hiring process cost:</strong> Every interview round has a cost — hiring manager time, technical assessment overhead, HR coordination.</li>
          <li><strong>Knowledge transfer tax:</strong> When a role finally fills after a long vacancy, the new hire's ramp-up takes 3–6 months. Productivity is not restored on day one.</li>
        </ul>

        <h2>Why Hiring Takes So Long</h2>
        <p>The average time-to-hire for senior software engineers in Nigeria's technology market is 68 days — and that is for companies with dedicated talent acquisition functions. For organisations without specialist tech recruiters, the median is over 90 days.</p>
        <p>The bottlenecks are consistent across organisations:</p>
        <ul>
          <li>Role definition that takes weeks to get approved by multiple stakeholders</li>
          <li>Job descriptions written by HR teams without engineering input — attracting the wrong candidates</li>
          <li>Interview processes with 4–6 stages, each requiring scheduling across busy calendars</li>
          <li>Compensation benchmarking that lags the market by 12–18 months</li>
          <li>Notice periods of 2–3 months at the target hire's current employer</li>
        </ul>

        <h2>The Three Faster Paths</h2>
        <h3>1. Staff Augmentation</h3>
        <p>For skills gaps that need to be filled in days, not months, staff augmentation provides pre-vetted engineers who can start within a week. The cost premium is real, but it is a fraction of the cost of a 90-day vacancy on a critical role.</p>

        <h3>2. Dedicated Development Centres</h3>
        <p>For organisations with recurring hiring needs across a consistent set of skills, a dedicated development centre — an in-country team managed by a technology partner — eliminates the hiring process entirely. The team is hired once, managed continuously, and scaled up or down based on project demand.</p>

        <h3>3. Delivery Pods</h3>
        <p>For discrete projects with a defined scope, a delivery pod provides a complete, self-managing team — engineers, a tech lead, and a delivery manager — without the overhead of permanent hiring. The team disengages when the project is delivered.</p>

        <h2>Calculating Your Hiring Cost</h2>
        <p>A simple model for quantifying the cost of an open senior engineering role:</p>
        <ul>
          <li>Monthly salary equivalent of unfilled role × vacancy months = direct salary opportunity cost</li>
          <li>Add 40% of that figure for lost velocity (conservative estimate based on team size)</li>
          <li>Add recruiter fee (typically 15–25% of annual salary)</li>
          <li>Add 3 months of partial productivity during ramp-up</li>
        </ul>
        <p>For a senior engineer at ₦8M annual salary, a 90-day vacancy costs approximately ₦4.5M–₦7M in total — before accounting for any opportunity cost from delayed delivery.</p>

        <blockquote>The question is not whether to pay for talent. It is whether to pay the visible cost of a contract engagement, or the invisible cost of a prolonged vacancy.</blockquote>
      </div>

      <aside class="reveal">
        <div class="sidebar-box">
          <h3>Article Details</h3>
          <div class="sidebar-row"><span>Category</span><span>Talent Strategy</span></div>
          <div class="sidebar-row"><span>Read Time</span><span>8 minutes</span></div>
          <div class="sidebar-row"><span>Published</span><span>Apr 2026</span></div>
        </div>
        <div class="sidebar-box">
          <h3>Related Services</h3>
          <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:.5rem;">
            <a href="/services/team-extension/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Team Extension</a>
            <a href="/services/delivery-pods/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Delivery Pods</a>
            <a href="/services/development-centres/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Development Centres</a>
          </div>
        </div>
        <div class="sidebar-box">
          <h3>More Insights</h3>
          <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:.5rem;">
            <a href="/insights/ai-prototypes-production/" style="color:var(--cr);font-size:.88rem;font-weight:600;">From AI Prototype to Production</a>
            <a href="/insights/african-infrastructure/" style="color:var(--cr);font-size:.88rem;font-weight:600;">Africa's Digital Infrastructure</a>
            <a href="/insights/" style="color:var(--cr);font-size:.88rem;font-weight:600;">All Insights →</a>
          </div>
        </div>
      </aside>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Dealing with unfilled engineering roles?</h2>
      <p>Our team extension and delivery pod services can close the gap in days, not months.</p>
      <div class="hero-cta-row">
        <a href="/services/team-extension/" class="btn-primary">Explore Team Extension</a>
        <a href="/contact/" class="btn-secondary">Talk to Us</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/insights/slow-hiring-cost",
    "title": "The Hidden Cost of Slow Hiring in Technology Teams",
    "meta": "Every open engineering role costs more than you think. We break down the full cost of a slow hiring process and the faster alternatives.",
    "og": "insights.jpg",
    "schema": article_schema("/insights/slow-hiring-cost", "The Hidden Cost of Slow Hiring in Technology Teams", "The real cost of unfilled engineering roles and faster alternatives."),
    "css": INS_ARTICLE_CSS,
    "html": slow_hiring_html,
    "aria": None,
})

# Events hub
events_css = HERO_CSS + """
.events-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem;margin-top:2rem;}
.event-card{background:#fff;border-radius:8px;border:1px solid var(--border);overflow:hidden;display:flex;flex-direction:column;}
.event-card-date{background:linear-gradient(135deg,var(--forest-deep),var(--teal));color:#fff;padding:1rem 1.5rem;display:flex;gap:1rem;align-items:center;}
.event-date-num{font-size:2rem;font-weight:900;line-height:1;}
.event-date-info{font-size:.8rem;line-height:1.5;}
.event-card-body{padding:1.5rem;flex:1;}
.event-card-body h3{font-size:1rem;font-weight:700;color:var(--forest-deep);margin-bottom:.5rem;}
.event-card-body p{font-size:.85rem;color:var(--txt-2);line-height:1.6;margin-bottom:1rem;}
.event-tag{display:inline-block;padding:.2rem .6rem;border-radius:12px;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;}
.event-tag.webinar{background:#e8f4f1;color:var(--teal-mid);}
.event-tag.conference{background:#fdf0f0;color:var(--cr);}
.event-tag.workshop{background:#fdf8ee;color:#8a6914;}
"""

events_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Events, News &amp; Technologies</div>
      <h1>Stay Informed. Stay Ahead.</h1>
      <p class="hero-lead">GreaterHeight Technologies hosts and participates in webinars, workshops, and industry events focused on engineering, AI, and technology strategy in Africa and beyond.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Upcoming Events</h2>
      <div class="events-grid reveal">
        <div class="event-card">
          <div class="event-card-date">
            <div class="event-date-num">15<br><span style="font-size:.8rem;font-weight:400;">Jan 2027</span></div>
            <div class="event-date-info">Online · 2:00 PM WAT<br>90 minutes</div>
          </div>
          <div class="event-card-body">
            <span class="event-tag webinar">Webinar</span>
            <h3 style="margin-top:.75rem;">Production AI: From Lab to Live in 90 Days</h3>
            <p>A practical walkthrough of the engineering decisions, infrastructure choices, and team structures that get AI models into production without the typical 18-month timelines.</p>
            <a href="/contact/" class="btn-primary" style="font-size:.8rem;padding:.6rem 1.4rem;">Register Interest</a>
          </div>
        </div>

        <div class="event-card">
          <div class="event-card-date">
            <div class="event-date-num">22<br><span style="font-size:.8rem;font-weight:400;">Feb 2027</span></div>
            <div class="event-date-info">Lagos, Nigeria<br>Full-day workshop</div>
          </div>
          <div class="event-card-body">
            <span class="event-tag workshop">Workshop</span>
            <h3 style="margin-top:.75rem;">Engineering Leadership Masterclass</h3>
            <p>A one-day intensive for CTOs, VPs of Engineering, and senior engineering leads — covering team design, delivery metrics, and technology strategy for scaling organisations.</p>
            <a href="/contact/" class="btn-primary" style="font-size:.8rem;padding:.6rem 1.4rem;">Register Interest</a>
          </div>
        </div>

        <div class="event-card">
          <div class="event-card-date">
            <div class="event-date-num">08<br><span style="font-size:.8rem;font-weight:400;">Mar 2027</span></div>
            <div class="event-date-info">Online · 3:00 PM WAT<br>60 minutes</div>
          </div>
          <div class="event-card-body">
            <span class="event-tag webinar">Webinar</span>
            <h3 style="margin-top:.75rem;">Data Infrastructure for African Enterprises</h3>
            <p>How to build a data platform that scales with your business — covering data warehouse architecture, pipeline design, and cost management for African cost structures.</p>
            <a href="/contact/" class="btn-primary" style="font-size:.8rem;padding:.6rem 1.4rem;">Register Interest</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <h2>Past Events &amp; Highlights</h2>
      <div class="events-grid reveal">
        <div class="event-card">
          <div class="event-card-date">
            <div class="event-date-num">Oct<br><span style="font-size:.8rem;font-weight:400;">2026</span></div>
            <div class="event-date-info">Tech Innovation Summit<br>Victoria Island, Lagos</div>
          </div>
          <div class="event-card-body">
            <span class="event-tag conference">Conference</span>
            <h3 style="margin-top:.75rem;">West Africa Tech Summit 2026</h3>
            <p>GreaterHeight delivered a keynote on "The Engineering Foundations of Africa's AI Economy" to an audience of 400+ technology leaders from across West Africa.</p>
          </div>
        </div>
        <div class="event-card">
          <div class="event-card-date">
            <div class="event-date-num">Jul<br><span style="font-size:.8rem;font-weight:400;">2026</span></div>
            <div class="event-date-info">Online · Recorded</div>
          </div>
          <div class="event-card-body">
            <span class="event-tag webinar">Webinar</span>
            <h3 style="margin-top:.75rem;">Scaling Engineering Teams in Nigeria</h3>
            <p>A discussion on the talent market, compensation benchmarks, and alternative models for building engineering capacity in the Nigerian market.</p>
            <a href="/insights/videos/" class="btn-secondary" style="font-size:.8rem;padding:.6rem 1.4rem;">Watch Recording</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Want us to speak at your event?</h2>
      <p>Our team presents on AI engineering, digital transformation, and technology strategy at conferences and corporate events across Africa.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Get in Touch</a>
        <a href="/insights/" class="btn-secondary">More Insights</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/insights/events",
    "title": "Events, News & Technologies",
    "meta": "GreaterHeight Technologies events — upcoming webinars, workshops, and conference appearances focused on AI, engineering, and technology strategy in Africa.",
    "og": "insights.jpg",
    "schema": webpage_schema("/insights/events", "Events, News & Technologies", "Upcoming and past events from GreaterHeight Technologies."),
    "css": events_css,
    "html": events_html,
    "aria": None,
})

# Videos hub
videos_css = HERO_CSS + """
.video-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem;margin-top:2rem;}
.video-card{background:#fff;border-radius:8px;border:1px solid var(--border);overflow:hidden;}
.video-thumb{position:relative;background:linear-gradient(135deg,var(--forest-deep),var(--teal));aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;}
.play-btn{width:56px;height:56px;background:rgba(255,255,255,.2);border-radius:50%;border:2px solid rgba(255,255,255,.6);display:flex;align-items:center;justify-content:center;color:#fff;transition:background .2s;}
.video-thumb:hover .play-btn{background:var(--cr);}
.play-btn svg{width:20px;height:20px;fill:currentColor;margin-left:3px;}
.video-card-body{padding:1.25rem;}
.video-card-body h3{font-size:.95rem;font-weight:700;color:var(--forest-deep);margin-bottom:.5rem;}
.video-card-body p{font-size:.83rem;color:var(--txt-2);line-height:1.6;margin:0;}
.video-meta{font-size:.75rem;color:var(--txt-3);margin-top:.5rem;}
"""

videos_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Videos &amp; Recordings</div>
      <h1>Learn From Our Engineers<br>and Strategists</h1>
      <p class="hero-lead">Video content from GreaterHeight Technologies — covering engineering practices, AI strategy, delivery methodology, and technology insights for African businesses.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Featured Videos</h2>
      <div class="video-grid reveal">
        <div class="video-card">
          <a href="https://www.youtube.com/@greaterheighttech" target="_blank" rel="noopener" class="video-thumb">
            <div class="play-btn"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
          </a>
          <div class="video-card-body">
            <h3>What is an AI-Augmented Engineering Team?</h3>
            <p>A walkthrough of how GreaterHeight structures teams with AI tooling embedded at every layer — from code review to test generation to documentation.</p>
            <div class="video-meta">28 min · Engineering Practice</div>
          </div>
        </div>

        <div class="video-card">
          <a href="https://www.youtube.com/@greaterheighttech" target="_blank" rel="noopener" class="video-thumb" style="background:linear-gradient(135deg,var(--wine),var(--cr));">
            <div class="play-btn"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
          </a>
          <div class="video-card-body">
            <h3>How We Run Discovery Sprints for Enterprise Clients</h3>
            <p>A behind-the-scenes look at our structured discovery methodology — from stakeholder interviews through to architecture decision records.</p>
            <div class="video-meta">35 min · Delivery Methodology</div>
          </div>
        </div>

        <div class="video-card">
          <a href="https://www.youtube.com/@greaterheighttech" target="_blank" rel="noopener" class="video-thumb" style="background:linear-gradient(135deg,var(--teal),var(--teal-glow));">
            <div class="play-btn"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
          </a>
          <div class="video-card-body">
            <h3>Data Engineering Fundamentals for Business Leaders</h3>
            <p>Not a technical tutorial — a business-focused explanation of data warehouses, pipelines, and analytics stacks, designed for decision-makers.</p>
            <div class="video-meta">22 min · Data Strategy</div>
          </div>
        </div>

        <div class="video-card">
          <a href="https://www.youtube.com/@greaterheighttech" target="_blank" rel="noopener" class="video-thumb" style="background:linear-gradient(135deg,var(--forest),var(--forest-deep));">
            <div class="play-btn"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
          </a>
          <div class="video-card-body">
            <h3>Building in Nigeria: The Case for African Engineering Talent</h3>
            <p>Why the global technology industry is increasingly looking to Nigeria for engineering capacity — and what Nigerian engineers bring to global teams.</p>
            <div class="video-meta">40 min · Industry · Why Nigeria</div>
          </div>
        </div>

        <div class="video-card">
          <a href="https://www.youtube.com/@greaterheighttech" target="_blank" rel="noopener" class="video-thumb" style="background:linear-gradient(135deg,var(--cr-mid),var(--wine));">
            <div class="play-btn"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
          </a>
          <div class="video-card-body">
            <h3>Scaling Engineering Teams Without Hiring: Three Models</h3>
            <p>Staff augmentation, delivery pods, and dedicated development centres — when each model is the right choice and how to transition between them.</p>
            <div class="video-meta">30 min · Talent Strategy</div>
          </div>
        </div>

        <div class="video-card">
          <a href="https://www.youtube.com/@greaterheighttech" target="_blank" rel="noopener" class="video-thumb" style="background:linear-gradient(135deg,var(--teal-mid),var(--forest));">
            <div class="play-btn"><svg viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg></div>
          </a>
          <div class="video-card-body">
            <h3>Webinar Replay: Production AI in 90 Days</h3>
            <p>Recording of our January 2026 webinar on the engineering decisions that get AI models from prototype to production in under 90 days.</p>
            <div class="video-meta">90 min · Webinar Replay</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Subscribe for new content</h2>
      <p>New videos drop every month — engineering deep-dives, strategy talks, and client stories from the GreaterHeight team.</p>
      <div class="hero-cta-row">
        <a href="https://www.youtube.com/@greaterheighttech" target="_blank" rel="noopener" class="btn-primary">Subscribe on YouTube</a>
        <a href="/insights/" class="btn-secondary">All Insights</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/insights/videos",
    "title": "Video Articles for Learning",
    "meta": "Video content from GreaterHeight Technologies — engineering practices, AI strategy, delivery methodology, and technology insights for African businesses.",
    "og": "insights.jpg",
    "schema": webpage_schema("/insights/videos", "Video Articles for Learning", "Videos from GreaterHeight Technologies on AI, engineering, and technology strategy."),
    "css": videos_css,
    "html": videos_html,
    "aria": None,
})

# ═══════════════════════════════════════════════════════════════════════════════
# SERVICES PAGES
# ═══════════════════════════════════════════════════════════════════════════════
SVC_CSS = HERO_CSS + STAT_CSS

# Services hub
svc_hub_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Our Services</div>
      <h1>How We Engage:<br>Five Delivery Models</h1>
      <p class="hero-lead">Every organisation has different needs, timelines, and budgets. GreaterHeight Technologies offers five distinct engagement models — from a single embedded engineer to a full delivery pod — so you get exactly the capacity you need, when you need it.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cards-grid reveal">
        <a href="/services/ai-engineering/" style="text-decoration:none;" class="card">
          <div class="card-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg></div>
          <h3>AI Engineering Service</h3>
          <p>Dedicated AI engineers and data scientists who build, deploy, and maintain production ML systems inside your existing technology team.</p>
        </a>
        <a href="/services/delivery-pods/" style="text-decoration:none;" class="card">
          <div class="card-icon"><svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg></div>
          <h3>Delivery Pods</h3>
          <p>Self-managing, cross-functional teams — engineers, tech lead, delivery manager — deployed against a defined scope and timeline.</p>
        </a>
        <a href="/services/development-centres/" style="text-decoration:none;" class="card">
          <div class="card-icon"><svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
          <h3>Development Centres</h3>
          <p>Your own offshore engineering team, fully managed, with dedicated infrastructure and a permanent bench of skilled engineers.</p>
        </a>
        <a href="/services/it-consulting/" style="text-decoration:none;" class="card">
          <div class="card-icon"><svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
          <h3>IT Consulting</h3>
          <p>Strategic technology advisory — architecture review, technology selection, digital transformation roadmaps, and CTO-as-a-Service.</p>
        </a>
        <a href="/services/team-extension/" style="text-decoration:none;" class="card">
          <div class="card-icon"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg></div>
          <h3>Team Extension</h3>
          <p>Pre-vetted engineers embedded into your team within days — covering skill gaps, sprint velocity needs, and project peaks without permanent headcount.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <h2>Choosing the Right Model</h2>
      <p class="lead-p">Not sure which engagement model fits your situation? Here is a quick guide:</p>
      <div style="margin-top:2rem;display:grid;gap:1rem;">
        <div class="card reveal" style="display:grid;grid-template-columns:auto 1fr;gap:1.5rem;align-items:start;">
          <div style="background:var(--cr);color:#fff;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0;">1</div>
          <div><h3>Need a specific skill, fast?</h3><p style="margin:0;">Team Extension — a single engineer or small group embedded within days, working directly in your team, on your tools.</p></div>
        </div>
        <div class="card reveal" style="display:grid;grid-template-columns:auto 1fr;gap:1.5rem;align-items:start;">
          <div style="background:var(--cr);color:#fff;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0;">2</div>
          <div><h3>Have a project with a clear scope?</h3><p style="margin:0;">Delivery Pods — a complete team that owns the delivery end-to-end, from architecture through to deployment and handover.</p></div>
        </div>
        <div class="card reveal" style="display:grid;grid-template-columns:auto 1fr;gap:1.5rem;align-items:start;">
          <div style="background:var(--cr);color:#fff;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0;">3</div>
          <div><h3>Need ongoing engineering capacity?</h3><p style="margin:0;">Development Centres — your own permanent offshore team with stable costs, managed processes, and no recurring recruitment overhead.</p></div>
        </div>
        <div class="card reveal" style="display:grid;grid-template-columns:auto 1fr;gap:1.5rem;align-items:start;">
          <div style="background:var(--cr);color:#fff;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0;">4</div>
          <div><h3>Trying to decide what to build?</h3><p style="margin:0;">IT Consulting — strategic advisory to help you make the right technology decisions before committing engineering resources.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Not sure which model fits?</h2>
      <p>Tell us what you're trying to achieve. We'll recommend the right engagement structure for your situation.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/how-we-do-it/" class="btn-secondary">Our Methodology</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/services",
    "title": "Services & Engagement Models",
    "meta": "GreaterHeight Technologies delivers technology through five engagement models: Team Extension, Delivery Pods, Development Centres, IT Consulting, and AI Engineering.",
    "og": "services.jpg",
    "schema": webpage_schema("/services", "Services & Engagement Models", "Five technology engagement models from GreaterHeight Technologies."),
    "css": SVC_CSS,
    "html": svc_hub_html,
    "aria": None,
})

def service_page(url, title, eyebrow, headline, lead, stats, what_is, how_it_works_items, benefits_items, cta_title, cta_body):
    how_items_html = "\n".join([
        f'<div class="card reveal"><h3>{s["title"]}</h3><p>{s["body"]}</p></div>'
        for s in how_it_works_items
    ])
    benefits_html = "\n".join([
        f'<li style="padding:.6rem 0;border-bottom:1px solid var(--border);"><strong style="color:var(--forest-deep);">{b["title"]}:</strong> <span style="color:var(--txt-2);">{b["body"]}</span></li>'
        for b in benefits_items
    ])
    stats_html = "\n".join([
        f'<div class="stat-box"><div class="stat-num">{s["num"]}</div><div class="stat-label">{s["label"]}</div></div>'
        for s in stats
    ])
    return f"""
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">{eyebrow}</div>
      <h1>{headline}</h1>
      <p class="hero-lead">{lead}</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Get Started</a>
        <a href="/services/" class="btn-secondary">All Services</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stats-row reveal">{stats_html}</div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap two-col reveal">
      <div>
        <h2>What Is {title}?</h2>
        {what_is}
      </div>
      <div>
        <ul style="list-style:none;padding:0;margin:0;">{benefits_html}</ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>How It Works</h2>
      <div class="cards-grid">{how_items_html}</div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>{cta_title}</h2>
      <p>{cta_body}</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/case-studies/" class="btn-secondary">See Our Work</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/services/ai-engineering",
    "title": "AI Engineering Service",
    "meta": "GreaterHeight's AI Engineering Service embeds dedicated AI engineers and data scientists into your team to build, deploy, and maintain production ML systems.",
    "og": "services.jpg",
    "schema": webpage_schema("/services/ai-engineering", "AI Engineering Service", "Dedicated AI engineers embedded into your team for production ML system development."),
    "css": SVC_CSS,
    "html": service_page(
        "/services/ai-engineering", "AI Engineering",
        "Service — AI Engineering",
        "Production-Ready AI Engineering,<br>Embedded in Your Team",
        "Specialist AI engineers and data scientists who work alongside your existing team to build, deploy, and maintain AI systems that perform reliably in production — not just in demos.",
        [
            {"num": "50+", "label": "AI Models Deployed to Production"},
            {"num": "87%", "label": "Average Triage Accuracy (Healthcare AI)"},
            {"num": "90", "label": "Days from Prototype to Go-Live"},
            {"num": "24/7", "label": "Model Monitoring &amp; Alerting"},
        ],
        "<p>The AI Engineering Service places dedicated ML engineers, data scientists, and MLOps specialists inside your team. They bring the production engineering discipline that transforms a proof-of-concept into a system your business can rely on — with proper data pipelines, model versioning, drift monitoring, and retraining cadences.</p><p>Unlike a consultancy engagement, this model integrates your engineers directly into your team's rituals: standups, sprint planning, code review, and retrospectives. The knowledge transfer is built in.</p>",
        [
            {"title": "Team Matching", "body": "We profile your stack, your domain, and your engineering culture, then match engineers with the right background in ML, data science, or MLOps."},
            {"title": "Embedding & Onboarding", "body": "Engineers join your team's rituals within days. We manage timezone alignment, tooling access, and communication norms."},
            {"title": "Build & Deploy", "body": "From feature engineering through model training, evaluation, and deployment — following CI/CD and infrastructure-as-code practices."},
            {"title": "Monitor & Maintain", "body": "Production monitoring with drift detection alerts, automated retraining pipelines, and regular model performance reviews."},
        ],
        [
            {"title": "No permanent headcount", "body": "Scale AI capacity without permanent hires, benefits overhead, or long-term salary commitments."},
            {"title": "Production-ready engineers", "body": "Every engineer has shipped AI systems to production — not just notebooks and demos."},
            {"title": "Knowledge transfer included", "body": "Our engineers document their decisions, run internal tech talks, and train your team as they build."},
            {"title": "Flexible scale", "body": "Add or reduce capacity month-by-month as project phases change."},
        ],
        "Ready to put AI into production?",
        "Our AI engineers are ready to embed with your team. Tell us what you're building and we'll match you with the right people.",
    ),
    "aria": None,
})

PAGES.append({
    "path": "/services/delivery-pods",
    "title": "Delivery Pods",
    "meta": "GreaterHeight Delivery Pods are self-managing, cross-functional engineering teams deployed against a defined scope — from architecture through to production deployment.",
    "og": "services.jpg",
    "schema": webpage_schema("/services/delivery-pods", "Delivery Pods", "Self-managing cross-functional engineering teams for defined software delivery."),
    "css": SVC_CSS,
    "html": service_page(
        "/services/delivery-pods", "Delivery Pods",
        "Service — Delivery Pods",
        "Complete Engineering Teams<br>That Own the Delivery",
        "A Delivery Pod is a self-managing, cross-functional team — engineers, tech lead, and delivery manager — deployed against a defined scope, timeline, and quality standard. You manage the outcome. We manage the delivery.",
        [
            {"num": "50+", "label": "Pods Delivered to Production"},
            {"num": "94%", "label": "On-Time Delivery Rate"},
            {"num": "2 weeks", "label": "Average Pod Mobilisation Time"},
            {"num": "100%", "label": "Dedicated Delivery Managers Per Pod"},
        ],
        "<p>A Delivery Pod removes the overhead of team management from your internal leadership. Each pod is staffed with engineers matched to your tech stack, led by a technical lead who makes day-to-day architecture decisions, and managed by a dedicated delivery manager who runs sprints, communicates progress, and escalates blockers.</p><p>You receive weekly sprint reports, bi-weekly stakeholder demos, and a full handover package at project close — including documentation, runbooks, and a knowledge transfer session for your internal team.</p>",
        [
            {"title": "Scoping & Kickoff", "body": "A structured kickoff process defines the technical scope, non-functional requirements, delivery milestones, and communication cadence."},
            {"title": "Sprint Delivery", "body": "Two-week sprints with planning, daily standups, mid-sprint check-ins, and sprint reviews open to your stakeholders."},
            {"title": "Quality Gates", "body": "Mandatory code review, automated testing, security scanning, and performance benchmarking at each milestone."},
            {"title": "Handover & Transition", "body": "Full documentation, runbooks, monitoring setup, and a knowledge transfer session before the pod disengages."},
        ],
        [
            {"title": "Fixed scope, predictable cost", "body": "Clear milestones and budgets — no scope creep, no surprise invoices."},
            {"title": "No management overhead", "body": "You don't manage the team — the pod's tech lead and delivery manager handle that."},
            {"title": "Proven quality process", "body": "Every pod follows GreaterHeight's structured delivery methodology with built-in quality gates."},
            {"title": "Knowledge transferred on exit", "body": "Your team inherits a well-documented, well-tested system they can maintain and extend."},
        ],
        "Have a project that needs a team?",
        "Tell us the scope and timeline. We'll propose a pod structure and a fixed-price delivery plan.",
    ),
    "aria": None,
})

PAGES.append({
    "path": "/services/development-centres",
    "title": "Development Centres",
    "meta": "GreaterHeight Development Centres give you a permanent, managed offshore engineering team in Lagos — with dedicated infrastructure and stable costs, without the recruitment overhead.",
    "og": "services.jpg",
    "schema": webpage_schema("/services/development-centres", "Development Centres", "Permanent managed offshore engineering teams in Lagos for sustained software delivery."),
    "css": SVC_CSS,
    "html": service_page(
        "/services/development-centres", "Development Centres",
        "Service — Development Centres",
        "Your Own Engineering Team<br>in Lagos, Fully Managed",
        "A GreaterHeight Development Centre gives you a permanent bench of dedicated engineers operating in Lagos — with stable monthly costs, no recruitment overhead, and GreaterHeight managing the HR, infrastructure, and culture.",
        [
            {"num": "10+", "label": "Active Development Centres"},
            {"num": "5–50", "label": "Engineer Range Per Centre"},
            {"num": "2 months", "label": "Average Set-Up Time"},
            {"num": "40%", "label": "Average Cost Saving vs Direct Hire"},
        ],
        "<p>A Development Centre is different from staff augmentation. Instead of placing individual engineers with you, we build and manage a dedicated team that operates as a functional extension of your engineering organisation — with its own management structure, rituals, and infrastructure, all in Lagos.</p><p>Your lead engineers set the technical direction. GreaterHeight handles everything else: hiring, HR, payroll, office space, equipment, and the cultural environment that keeps engineers productive and retained.</p>",
        [
            {"title": "Requirements & Sizing", "body": "We work with you to define the team structure, skill requirements, and engagement model — then design a centre configuration to match."},
            {"title": "Hiring & Onboarding", "body": "GreaterHeight recruits against your bar, using our established talent network and technical interview process, with your sign-off on final hires."},
            {"title": "Infrastructure & Set-Up", "body": "Office space, equipment, security setup, and tooling access configured to your standards within 60 days of contract signature."},
            {"title": "Ongoing Management", "body": "Monthly performance reviews, quarterly calibrations, and an embedded GreaterHeight delivery lead who manages the day-to-day."},
        ],
        [
            {"title": "Lower cost than direct hire", "body": "No employer taxes, office lease, or equipment depreciation. One monthly invoice, all-in."},
            {"title": "Your team, your culture", "body": "Engineers are dedicated to you — not shared across multiple clients, not rotated off projects."},
            {"title": "Talent stability", "body": "GreaterHeight's retention-focused culture and structured career development keep engineers in place longer than in-house models."},
            {"title": "Scalable", "body": "Add engineers as your roadmap grows — without restarting a recruitment process from scratch."},
        ],
        "Ready to build a permanent engineering presence in Lagos?",
        "We'll walk you through the model, the costs, and the typical timeline for getting a development centre operational.",
    ),
    "aria": None,
})

PAGES.append({
    "path": "/services/it-consulting",
    "title": "IT Consulting",
    "meta": "GreaterHeight IT Consulting provides strategic technology advisory — architecture review, technology selection, digital transformation roadmaps, and CTO-as-a-Service for African enterprises.",
    "og": "services.jpg",
    "schema": webpage_schema("/services/it-consulting", "IT Consulting", "Strategic technology advisory and CTO-as-a-Service for African enterprises."),
    "css": SVC_CSS,
    "html": service_page(
        "/services/it-consulting", "IT Consulting",
        "Service — IT Consulting",
        "Technology Strategy That<br>Leads to Better Decisions",
        "GreaterHeight's IT Consulting practice works with CEOs, CTOs, and boards to make the right technology decisions — from architecture review and vendor selection to full digital transformation roadmaps and fractional CTO engagements.",
        [
            {"num": "60+", "label": "Consulting Engagements Delivered"},
            {"num": "15+", "label": "Years Advising C-Suite Technology Leaders"},
            {"num": "8", "label": "Industry Verticals Covered"},
            {"num": "90-day", "label": "Quick-Start Roadmap Available"},
        ],
        "<p>Technology consulting at GreaterHeight is not about generating slide decks. It is about helping you make better technology decisions — faster, with more confidence, and with an honest assessment of the trade-offs involved.</p><p>Our consultants bring practitioner experience: they have built production systems, managed engineering teams, and navigated technology vendor relationships. They advise from that experience, not from frameworks alone.</p>",
        [
            {"title": "Architecture Review", "body": "Independent assessment of your existing technology stack — identifying risks, technical debt, scalability bottlenecks, and security gaps."},
            {"title": "Technology Roadmapping", "body": "12–36 month technology roadmaps aligned to your business strategy — prioritised by value, feasibility, and dependency."},
            {"title": "Vendor Selection", "body": "Structured evaluation of technology vendors, platforms, and tools — covering commercial terms, technical fit, and long-term risk."},
            {"title": "CTO-as-a-Service", "body": "Fractional CTO engagement for organisations without a full-time technology leader — available from 1 day per week to full-time."},
        ],
        [
            {"title": "Practitioner-led advice", "body": "Our consultants have built what they advise on. No untested recommendations."},
            {"title": "Independent perspective", "body": "We have no vendor relationships that bias our recommendations. Our only interest is your outcome."},
            {"title": "Deliverable-focused", "body": "Every engagement produces concrete outputs: a report, a roadmap, a decision framework — not just a presentation."},
            {"title": "Implementation-ready", "body": "Our recommendations come with GreaterHeight engineers ready to execute — no handover gap."},
        ],
        "Ready for strategic technology clarity?",
        "Whether you are preparing for a major platform decision, planning a digital transformation, or need a trusted technology partner at board level — we are ready to engage.",
    ),
    "aria": None,
})

PAGES.append({
    "path": "/services/team-extension",
    "title": "Team Extension",
    "meta": "GreaterHeight Team Extension places pre-vetted engineers inside your existing team within days — covering skill gaps, sprint velocity needs, and project peaks without permanent headcount.",
    "og": "services.jpg",
    "schema": webpage_schema("/services/team-extension", "Team Extension", "Pre-vetted engineers embedded in your team within days for immediate capacity."),
    "css": SVC_CSS,
    "html": service_page(
        "/services/team-extension", "Team Extension",
        "Service — Team Extension",
        "Pre-Vetted Engineers,<br>In Your Team Within Days",
        "When you need engineering capacity quickly — for a skill gap, a sprint velocity problem, or a project peak — Team Extension places pre-vetted GreaterHeight engineers directly inside your existing team within days, not months.",
        [
            {"num": "72hrs", "label": "Average Time to First CV"},
            {"num": "1 week", "label": "Typical Time to Embedding"},
            {"num": "95%", "label": "Satisfaction Rate at 90-Day Mark"},
            {"num": "Month", "label": "Minimum Engagement Duration"},
        ],
        "<p>Team Extension is the fastest way to close a skills gap without committing to permanent headcount. Engineers embed directly into your existing team — using your tools, joining your standups, participating in your code reviews, and operating under your tech lead's direction.</p><p>GreaterHeight manages the contractual relationship, payroll, and HR. You manage the engineer's day-to-day work. It is the simplest possible model: extra hands that work exactly like your own team.</p>",
        [
            {"title": "Requirements Brief", "body": "You share the skills needed, the tech stack, the timeline, and the team culture. We match against our bench within 48 hours."},
            {"title": "CV Review & Selection", "body": "We present 2–3 pre-vetted candidates. You review CVs and conduct a brief technical interview before making a selection."},
            {"title": "Embedding & Onboarding", "body": "The engineer joins within days — getting access to your tools, meeting the team, and attending their first standup."},
            {"title": "Active Engagement", "body": "The engineer works under your tech lead's direction. We provide monthly check-ins and handle any performance or HR issues."},
        ],
        [
            {"title": "Fast", "body": "First CVs within 72 hours. Engineers typically start within a week of contract signature."},
            {"title": "Pre-vetted", "body": "Every engineer has passed GreaterHeight's technical assessment and reference check process — no surprise mismatches."},
            {"title": "Flexible terms", "body": "Month-by-month contracts with 30 days notice — scale up, scale down, or extend with no long-term commitment."},
            {"title": "Seamless integration", "body": "Engineers embed into your team's culture and tools from day one. No separate processes or reporting overhead."},
        ],
        "Need engineers this week?",
        "Tell us the skills and tech stack you need. We will have candidates for you within 72 hours.",
    ),
    "aria": None,
})

# ═══════════════════════════════════════════════════════════════════════════════
# WHAT WE DO HUB PAGES
# ═══════════════════════════════════════════════════════════════════════════════
WWD_CSS = HERO_CSS + """
.sub-pages-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1.5rem;margin-top:2rem;}
.sub-page-card{background:#fff;border-radius:8px;border:1px solid var(--border);overflow:hidden;text-decoration:none;color:inherit;display:flex;flex-direction:column;transition:box-shadow .2s,transform .2s;}
.sub-page-card:hover{box-shadow:0 8px 28px rgba(0,0,0,.1);transform:translateY(-3px);}
.sub-page-card-top{padding:1.5rem 1.5rem 1rem;flex:1;}
.sub-page-card-top h3{font-size:1rem;font-weight:700;color:var(--forest-deep);margin-bottom:.5rem;}
.sub-page-card-top p{font-size:.85rem;color:var(--txt-2);line-height:1.6;margin:0;}
.sub-page-card-link{padding:.85rem 1.5rem;background:var(--bg-2);font-size:.8rem;font-weight:700;color:var(--cr);border-top:1px solid var(--border);}
"""

def wwd_hub(url, title, eyebrow, headline, lead, intro_p, sub_pages, cta_title, cta_body):
    sub_html = "\n".join([
        f'''<a href="{s["href"]}" class="sub-page-card reveal">
  <div class="sub-page-card-top">
    <h3>{s["title"]}</h3>
    <p>{s["body"]}</p>
  </div>
  <div class="sub-page-card-link">Learn more →</div>
</a>'''
        for s in sub_pages
    ])
    return f"""
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">{eyebrow}</div>
      <h1>{headline}</h1>
      <p class="hero-lead">{lead}</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start a Project</a>
        <a href="/case-studies/" class="btn-secondary">Our Work</a>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap two-col reveal">
      <div>
        <h2>What We Do in {title}</h2>
        {intro_p}
      </div>
      <div class="cards-grid" style="margin-top:0;">
        <div class="card">
          <h3>Production-First</h3>
          <p>Everything we build is designed for production from the first day of design — not retrofitted at the end.</p>
        </div>
        <div class="card">
          <h3>Embedded Teams</h3>
          <p>Our engineers work inside your team's processes, tools, and culture — not in a separate orbit.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Capabilities in {title}</h2>
      <div class="sub-pages-grid">{sub_html}</div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>{cta_title}</h2>
      <p>{cta_body}</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Get in Touch</a>
        <a href="/how-we-do-it/" class="btn-secondary">Our Methodology</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/what-we-do/ai",
    "title": "Artificial Intelligence & Machine Learning",
    "meta": "GreaterHeight's AI practice builds production-ready ML systems, AI agents, predictive analytics, and conversational AI for African enterprises.",
    "og": "what-we-do.jpg",
    "schema": webpage_schema("/what-we-do/ai", "Artificial Intelligence & Machine Learning", "Production AI and ML engineering for African enterprises."),
    "css": WWD_CSS,
    "html": wwd_hub(
        "/what-we-do/ai", "Artificial Intelligence",
        "What We Do — AI &amp; Machine Learning",
        "AI Systems That Perform<br>in the Real World",
        "We build, deploy, and maintain artificial intelligence and machine learning systems that run in production — not just in demos. Our AI practice covers the full spectrum from strategy and prototyping through to MLOps and ongoing model management.",
        "<p>GreaterHeight's AI engineers are practitioners, not theorists. Every system we design is shaped by the constraints of the production environment: data quality, latency requirements, explainability obligations, and the operational realities of African infrastructure.</p><p>We work across NLP, computer vision, predictive analytics, recommendation systems, and AI agents — always with production reliability as the first design constraint.</p>",
        [
            {"href": "/what-we-do/ai/consulting/", "title": "AI Consulting & Strategy", "body": "AI readiness assessments, use-case discovery, ROI modelling, and technology roadmaps for organisations beginning their AI journey."},
            {"href": "/what-we-do/ai/agents-automation/", "title": "AI Agents & Automation", "body": "Autonomous agents, workflow automation, and intelligent process automation built on LLMs and decision models."},
            {"href": "/what-we-do/ai/data-science/", "title": "Data Science & Analytics", "body": "Predictive models, statistical analysis, and data-driven decision systems designed to operate at production scale."},
            {"href": "/what-we-do/ai/model-deployment/", "title": "Model Deployment & MLOps", "body": "CI/CD pipelines for ML models, model registries, drift monitoring, and automated retraining infrastructure."},
            {"href": "/what-we-do/ai/natural-language/", "title": "Natural Language Processing", "body": "Text classification, named entity recognition, sentiment analysis, and LLM-powered applications for business workflows."},
        ],
        "Building an AI system?",
        "Our AI engineers have shipped production ML systems across healthcare, fintech, and enterprise operations. Tell us what you're trying to build.",
    ),
    "aria": "/what-we-do/ai/",
})

PAGES.append({
    "path": "/what-we-do/data",
    "title": "Data Engineering & Analytics",
    "meta": "GreaterHeight's Data practice builds data warehouses, analytics pipelines, cloud data platforms, and BI solutions for African enterprises.",
    "og": "what-we-do.jpg",
    "schema": webpage_schema("/what-we-do/data", "Data Engineering & Analytics", "Data warehouses, pipelines, and analytics for African enterprises."),
    "css": WWD_CSS,
    "html": wwd_hub(
        "/what-we-do/data", "Data",
        "What We Do — Data Engineering",
        "Data Infrastructure That<br>Answers Real Business Questions",
        "We build the data foundations that give organisations reliable, timely, and trustworthy access to their own information — from ingestion pipelines and data warehouses through to analytics platforms and self-service BI.",
        "<p>Most data problems are not analytics problems — they are infrastructure problems. Data that is not flowing reliably, that is duplicated across systems, that takes three days to reconcile, or that nobody trusts, cannot be used to make decisions.</p><p>GreaterHeight's data engineers build the infrastructure that solves that first: clean ingestion, reliable transformation, governed storage, and analytics-ready serving layers. Then we build the BI and analytics capabilities on top.</p>",
        [
            {"href": "/what-we-do/data/engineering/", "title": "Data Engineering", "body": "ETL/ELT pipelines, real-time streaming, data quality frameworks, and orchestration with Airflow, dbt, and Kafka."},
            {"href": "/what-we-do/data/cloud-solutions/", "title": "Cloud Data Platforms", "body": "Cloud-native data warehouses on AWS, Azure, and GCP — architected for African cost structures and data residency requirements."},
            {"href": "/what-we-do/data/analytics/", "title": "Analytics & BI", "body": "Self-service dashboards, executive reporting, and embedded analytics using Power BI, Metabase, and custom solutions."},
            {"href": "/what-we-do/data/governance/", "title": "Data Governance", "body": "NDPR-compliant data catalogues, lineage tracking, access controls, and data quality monitoring frameworks."},
        ],
        "Building your data infrastructure?",
        "Tell us where the data bottlenecks are. We will design the architecture and build the pipelines.",
    ),
    "aria": "/what-we-do/data/",
})

PAGES.append({
    "path": "/what-we-do/engineering",
    "title": "Software Engineering",
    "meta": "GreaterHeight's Software Engineering practice builds custom software, web and mobile applications, APIs, and cross-platform solutions for African enterprises.",
    "og": "what-we-do.jpg",
    "schema": webpage_schema("/what-we-do/engineering", "Software Engineering", "Custom software, web, mobile, and API engineering for African enterprises."),
    "css": WWD_CSS,
    "html": wwd_hub(
        "/what-we-do/engineering", "Software Engineering",
        "What We Do — Software Engineering",
        "Software Built to Perform,<br>Maintained to Last",
        "We design and build custom software, web applications, mobile apps, APIs, and platform integrations — using the right technology for each problem, with engineering discipline that makes the resulting systems easy to operate, evolve, and hand over.",
        "<p>Software engineering at GreaterHeight starts with understanding the problem, not selecting a framework. We define the requirements, design the architecture, build iteratively in sprints, and hand over systems that your team can maintain without a dependency on us.</p><p>Our engineering teams cover the full stack — frontend, backend, mobile, API, cloud infrastructure, and DevOps — with deep specialisation in the domains our clients operate in.</p>",
        [
            {"href": "/what-we-do/engineering/custom-software/", "title": "Custom Software Development", "body": "Bespoke software products built from scratch — from product specification through architecture, build, testing, and deployment."},
            {"href": "/what-we-do/engineering/web-application/", "title": "Web Application Development", "body": "Progressive web apps, SaaS platforms, enterprise portals, and content-rich websites with performance-first front-end engineering."},
            {"href": "/what-we-do/engineering/mobile-app/", "title": "Mobile App Development", "body": "iOS, Android, and cross-platform mobile applications built with React Native or Flutter — to production quality and app store standards."},
            {"href": "/what-we-do/engineering/cross-platform/", "title": "Cross-Platform Development", "body": "Single codebases that run on web, iOS, and Android — without compromising the native experience on any platform."},
            {"href": "/what-we-do/engineering/api-integration/", "title": "API & Integration", "body": "RESTful and GraphQL APIs, third-party integrations, event-driven architectures, and microservices decomposition."},
        ],
        "Need a software team?",
        "Tell us what you are building. We will scope it, propose an approach, and assemble the right team.",
    ),
    "aria": "/what-we-do/engineering/",
})

PAGES.append({
    "path": "/what-we-do/enterprise",
    "title": "Enterprise Technology",
    "meta": "GreaterHeight's Enterprise practice delivers digital transformation, IoT, blockchain, legacy modernisation, and IT strategy for large organisations.",
    "og": "what-we-do.jpg",
    "schema": webpage_schema("/what-we-do/enterprise", "Enterprise Technology", "Digital transformation, IoT, blockchain, and legacy modernisation for enterprises."),
    "css": WWD_CSS,
    "html": wwd_hub(
        "/what-we-do/enterprise", "Enterprise Technology",
        "What We Do — Enterprise Technology",
        "Enterprise-Scale Technology<br>for Complex Organisations",
        "We work with large organisations navigating digital transformation, operational modernisation, and strategic technology programmes — bringing engineering capability, programme management discipline, and deep domain knowledge to the most complex engagements.",
        "<p>Enterprise technology programmes fail for three reasons: unclear requirements, underestimated complexity, and insufficient engineering capacity. GreaterHeight addresses all three: a structured discovery process that surfaces requirements before a line of code is written, architecture design that accounts for the full complexity, and delivery pods that provide the engineering capacity to execute.</p>",
        [
            {"href": "/what-we-do/enterprise/digital-transformation/", "title": "Digital Transformation", "body": "End-to-end digital transformation programmes — from strategy and operating model design through technology implementation and change management."},
            {"href": "/what-we-do/enterprise/iot/", "title": "Internet of Things (IoT)", "body": "Connected device architectures, sensor data platforms, real-time operational dashboards, and predictive maintenance systems."},
            {"href": "/what-we-do/enterprise/blockchain/", "title": "Blockchain Solutions", "body": "Smart contract development, enterprise blockchain platforms, tokenisation systems, and distributed ledger applications for regulated industries."},
            {"href": "/what-we-do/enterprise/legacy-modernisation/", "title": "Legacy Modernisation", "body": "Phased migration strategies that incrementally replace ageing core systems — without disrupting production operations or losing institutional knowledge."},
            {"href": "/what-we-do/enterprise/it-strategy/", "title": "IT Strategy", "body": "Technology strategy development, enterprise architecture, vendor selection, and board-level technology advisory."},
            {"href": "/what-we-do/enterprise/consulting/", "title": "IT Consulting", "body": "Specialist consulting across ERP implementations, system integration, and technology programme delivery."},
        ],
        "Planning an enterprise technology programme?",
        "Our enterprise practice has delivered complex programmes across banking, telecoms, healthcare, and the public sector. Tell us about your challenge.",
    ),
    "aria": "/what-we-do/enterprise/",
})

PAGES.append({
    "path": "/what-we-do/marketing",
    "title": "Digital Marketing",
    "meta": "GreaterHeight's Digital Marketing practice covers SEO, PPC, content, social media, display advertising, lead generation, CRO, PR, and online reputation management.",
    "og": "what-we-do.jpg",
    "schema": webpage_schema("/what-we-do/marketing", "Digital Marketing", "Full-spectrum digital marketing services from GreaterHeight Technologies."),
    "css": WWD_CSS,
    "html": wwd_hub(
        "/what-we-do/marketing", "Digital Marketing",
        "What We Do — Digital Marketing",
        "Digital Marketing That<br>Drives Measurable Results",
        "GreaterHeight Technologies combines technology precision with marketing expertise — delivering performance marketing, content, SEO, and brand-building programmes that generate measurable pipeline and revenue for our clients.",
        "<p>Marketing in a digital-first world is a technology problem as much as a creative one. Tracking, attribution, automation, A/B testing, and audience segmentation all require engineering capability. GreaterHeight's marketing practice sits inside a technology company for exactly this reason: we build the tools that make the campaigns perform, not just the campaigns.</p>",
        [
            {"href": "/what-we-do/marketing/seo/", "title": "Search Engine Optimisation", "body": "Technical SEO, content strategy, and link building — designed to generate organic search traffic that converts."},
            {"href": "/what-we-do/marketing/ppc/", "title": "Pay-Per-Click (PPC)", "body": "Google Ads, Meta Ads, and LinkedIn Ads campaigns managed with rigorous testing frameworks and clear ROAS targets."},
            {"href": "/what-we-do/marketing/content/", "title": "Content Development", "body": "Long-form content, thought leadership, and editorial programmes that build authority and generate organic leads."},
            {"href": "/what-we-do/marketing/social-media/", "title": "Social Media Marketing", "body": "Platform-specific strategy, community management, and paid social programmes for B2B and B2C audiences."},
            {"href": "/what-we-do/marketing/cro/", "title": "Conversion Rate Optimisation", "body": "A/B testing, funnel analysis, landing page optimisation, and UX improvements to maximise conversion from existing traffic."},
            {"href": "/what-we-do/marketing/display/", "title": "Display Advertising", "body": "Programmatic display, retargeting, and brand awareness campaigns across the premium African and global digital media landscape."},
            {"href": "/what-we-do/marketing/lead-gen/", "title": "Lead Generation", "body": "Multi-channel lead generation campaigns for B2B technology, professional services, and enterprise sales pipelines."},
            {"href": "/what-we-do/marketing/online-reputation/", "title": "Online Reputation Management", "body": "Brand monitoring, review management, and strategic content to build and protect digital reputation."},
            {"href": "/what-we-do/marketing/pr/", "title": "Digital PR", "body": "Media relations, press release distribution, and digital PR programmes that build authority and generate high-quality backlinks."},
        ],
        "Looking for marketing that actually converts?",
        "We build the technology and run the campaigns. Tell us your growth objective.",
    ),
    "aria": "/what-we-do/marketing/",
})

# ═══════════════════════════════════════════════════════════════════════════════
# MARKETING SUB-PAGES (5)
# ═══════════════════════════════════════════════════════════════════════════════
MKT_CSS = HERO_CSS + STAT_CSS

def marketing_page(url, title, eyebrow, headline, lead, stats, what_it_is, how_items, why_items, cta_title):
    how_html = "\n".join([f'<div class="card reveal"><h3>{h["title"]}</h3><p>{h["body"]}</p></div>' for h in how_items])
    why_html = "\n".join([f'<li style="padding:.6rem 0;border-bottom:1px solid var(--border);"><strong style="color:var(--forest-deep);">{w["title"]}:</strong> <span style="color:var(--txt-2);">{w["body"]}</span></li>' for w in why_items])
    stats_html = "\n".join([f'<div class="stat-box"><div class="stat-num">{s["num"]}</div><div class="stat-label">{s["label"]}</div></div>' for s in stats])
    return f"""
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">{eyebrow}</div>
      <h1>{headline}</h1>
      <p class="hero-lead">{lead}</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Get Started</a>
        <a href="/what-we-do/marketing/" class="btn-secondary">All Marketing Services</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stats-row reveal">{stats_html}</div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap two-col reveal">
      <div>
        <h2>What Is {title}?</h2>
        {what_it_is}
      </div>
      <div>
        <ul style="list-style:none;padding:0;margin:0;">{why_html}</ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Our Approach</h2>
      <div class="cards-grid">{how_html}</div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>{cta_title}</h2>
      <p>Tell us your objective. We'll build the right programme for your audience, budget, and timeline.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/what-we-do/marketing/" class="btn-secondary">All Marketing Services</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/what-we-do/marketing/cro",
    "title": "Conversion Rate Optimisation (CRO)",
    "meta": "GreaterHeight's CRO service uses A/B testing, funnel analysis, and UX improvements to increase the percentage of website visitors who convert to leads or customers.",
    "og": "marketing.jpg",
    "schema": webpage_schema("/what-we-do/marketing/cro", "Conversion Rate Optimisation", "A/B testing and funnel optimisation to increase conversion from existing traffic."),
    "css": MKT_CSS,
    "html": marketing_page(
        "/what-we-do/marketing/cro", "Conversion Rate Optimisation",
        "Digital Marketing — CRO",
        "Turn More Visitors Into<br>Customers",
        "Conversion Rate Optimisation is the systematic process of increasing the percentage of your website visitors who take the desired action — sign up, contact, buy, or download. We use data, testing, and UX expertise to find and fix the leaks in your funnel.",
        [
            {"num": "34%", "label": "Average Conversion Uplift"},
            {"num": "2-week", "label": "First Test Cycle"},
            {"num": "A/B + MVT", "label": "Testing Methodology"},
            {"num": "Zero", "label": "Assumptions — Everything Is Tested"},
        ],
        "<p>CRO is not about redesigning your website. It is about understanding why visitors are not converting — and removing those barriers systematically. Every change we make is based on data: heatmaps, session recordings, funnel analysis, and user research. And every change is tested before it is deployed permanently.</p>",
        [
            {"title": "Conversion Audit", "body": "A deep dive into your analytics, heatmaps, and user recordings to identify where visitors are dropping out and why."},
            {"title": "Hypothesis Development", "body": "Data-driven hypotheses ranked by potential impact and ease of implementation — giving you a prioritised testing roadmap."},
            {"title": "A/B Testing", "body": "Rigorous A/B and multivariate tests run with statistical significance thresholds to ensure results are reliable, not random."},
            {"title": "Implementation & Monitoring", "body": "Winning variants implemented permanently, results documented, and ongoing monitoring to ensure gains are retained."},
        ],
        [
            {"title": "Data-driven, not opinion-driven", "body": "Every hypothesis is based on behavioural data — not what we think looks better."},
            {"title": "Statistical rigour", "body": "Tests run to statistical significance before any conclusion is drawn. No premature wins declared."},
            {"title": "Full-funnel view", "body": "We optimise the entire journey — from ad click through landing page, sign-up, onboarding, and first purchase."},
            {"title": "Sustainable results", "body": "Changes are tested, documented, and embedded — not fragile tweaks that revert with the next redesign."},
        ],
        "Ready to convert more of your existing traffic?",
    ),
    "aria": "/what-we-do/marketing/",
})

PAGES.append({
    "path": "/what-we-do/marketing/display",
    "title": "Display Advertising Campaigns",
    "meta": "GreaterHeight's Display Advertising service manages programmatic display, retargeting, and brand awareness campaigns across premium African and global digital media.",
    "og": "marketing.jpg",
    "schema": webpage_schema("/what-we-do/marketing/display", "Display Advertising Campaigns", "Programmatic display, retargeting, and brand campaigns across digital media."),
    "css": MKT_CSS,
    "html": marketing_page(
        "/what-we-do/marketing/display", "Display Advertising",
        "Digital Marketing — Display Advertising",
        "Display Campaigns That Build<br>Brand and Drive Results",
        "Programmatic display advertising, retargeting, and brand awareness campaigns — planned, executed, and optimised to deliver measurable reach, frequency, and conversion across Africa's premium digital media landscape and globally.",
        [
            {"num": "50M+", "label": "Monthly Impressions Managed"},
            {"num": "3.2×", "label": "Average ROAS on Retargeting"},
            {"num": "GDN + DSP", "label": "Media Platforms"},
            {"num": "Real-time", "label": "Bid Optimisation"},
        ],
        "<p>Display advertising in 2026 is not about banner blindness — it is about precision targeting, compelling creative, and intelligent bidding. Our display campaigns combine audience data, creative testing, and programmatic optimisation to deliver brand objectives and performance goals simultaneously.</p>",
        [
            {"title": "Audience Strategy", "body": "First-party data activation, lookalike modelling, and contextual targeting to reach the right audience segments at scale."},
            {"title": "Creative Development", "body": "Responsive display ads, HTML5 rich media, and video pre-roll — tested across formats to identify the highest-performing creative."},
            {"title": "Media Planning & Buying", "body": "Programmatic buying across Google Display Network, premium publishers, and African-specific digital media networks."},
            {"title": "Optimisation & Reporting", "body": "Daily bid adjustments, weekly creative refresh cycles, and transparent reporting tied to your business objectives."},
        ],
        [
            {"title": "Full-funnel capability", "body": "Prospecting campaigns for brand awareness and retargeting campaigns for conversion — managed as a unified programme."},
            {"title": "African media expertise", "body": "We know which publishers reach Nigerian, Ghanaian, Kenyan, and South African audiences — and at what cost."},
            {"title": "Creative-led", "body": "Great display is creative-led. Our in-house creative team builds and tests display assets continuously."},
            {"title": "Transparent", "body": "You see every impression, every click, every conversion. No black boxes."},
        ],
        "Looking to scale your display programme?",
    ),
    "aria": "/what-we-do/marketing/",
})

PAGES.append({
    "path": "/what-we-do/marketing/lead-gen",
    "title": "Lead Generation Campaigns",
    "meta": "GreaterHeight's Lead Generation service delivers multi-channel B2B lead generation campaigns for technology, professional services, and enterprise sales pipelines.",
    "og": "marketing.jpg",
    "schema": webpage_schema("/what-we-do/marketing/lead-gen", "Lead Generation Campaigns", "Multi-channel B2B lead generation for technology and enterprise pipelines."),
    "css": MKT_CSS,
    "html": marketing_page(
        "/what-we-do/marketing/lead-gen", "Lead Generation",
        "Digital Marketing — Lead Generation",
        "Qualified Leads for Your<br>Enterprise Sales Pipeline",
        "Multi-channel lead generation campaigns that deliver sales-ready prospects to your pipeline — combining content marketing, LinkedIn outreach, SEO, PPC, and marketing automation to generate and nurture B2B demand.",
        [
            {"num": "2.4×", "label": "Average Pipeline Value Increase"},
            {"num": "SAL", "label": "Sales-Accepted Lead Qualification"},
            {"num": "CRM", "label": "Direct Integration to Your Pipeline"},
            {"num": "90-day", "label": "Quick-Start Programme"},
        ],
        "<p>Lead generation for enterprise technology and professional services requires a different approach to consumer lead gen. The sales cycle is longer, the buying committee is larger, and the content that earns trust is more demanding to produce. Our B2B lead generation programmes are built for this environment.</p>",
        [
            {"title": "Audience & ICP Definition", "body": "We define your ideal customer profile, build target account lists, and segment by buying stage to focus effort where conversion probability is highest."},
            {"title": "Content & Lead Magnets", "body": "High-value content — white papers, calculators, audit frameworks, templates — that earns contact details from decision-makers."},
            {"title": "Multi-Channel Distribution", "body": "LinkedIn paid, email outreach, SEO-optimised long-form content, and retargeting running in coordination to build frequency and trust."},
            {"title": "Lead Scoring & Handover", "body": "Marketing automation that scores leads by engagement and intent — handing sales-ready leads to your team at the right moment."},
        ],
        [
            {"title": "B2B-first", "body": "Our methodology is designed for long-cycle enterprise sales — not consumer lead gen repackaged."},
            {"title": "Quality over quantity", "body": "We optimise for sales-accepted lead rate, not raw form submissions. Your sales team's time is too valuable for unqualified leads."},
            {"title": "CRM-integrated", "body": "Leads flow directly to your CRM — Salesforce, HubSpot, Zoho — with full source attribution."},
            {"title": "Content included", "body": "We build the content that generates the leads — white papers, case studies, calculators — not just the distribution."},
        ],
        "Struggling to fill your enterprise pipeline?",
    ),
    "aria": "/what-we-do/marketing/",
})

PAGES.append({
    "path": "/what-we-do/marketing/online-reputation",
    "title": "Online Reputation Management",
    "meta": "GreaterHeight's Online Reputation Management service monitors, manages, and improves your brand's digital presence across reviews, social media, and search results.",
    "og": "marketing.jpg",
    "schema": webpage_schema("/what-we-do/marketing/online-reputation", "Online Reputation Management", "Brand monitoring, review management, and digital reputation for African businesses."),
    "css": MKT_CSS,
    "html": marketing_page(
        "/what-we-do/marketing/online-reputation", "Online Reputation Management",
        "Digital Marketing — Reputation Management",
        "Protect and Build Your<br>Brand's Online Reputation",
        "Your online reputation influences every sales conversation, every partnership discussion, and every hiring decision. We monitor, manage, and strategically improve what people find when they search for your brand — across reviews, social media, news, and search results.",
        [
            {"num": "24/7", "label": "Brand Monitoring"},
            {"num": "4.2★", "label": "Average Review Rating Achieved"},
            {"num": "P1 SERP", "label": "Positive Content Placement Target"},
            {"num": "48hrs", "label": "Crisis Response Activation"},
        ],
        "<p>Online reputation management is not PR spin — it is systematic, long-term brand stewardship across the digital channels where your audience forms opinions. It includes monitoring for brand mentions in real time, managing review responses with professionalism, suppressing negative content through strategic positive content creation, and building a credible, consistent brand narrative across search and social.</p>",
        [
            {"title": "Reputation Audit", "body": "A comprehensive audit of your current online presence — search results, review platforms, social mentions, and news coverage."},
            {"title": "Review Management", "body": "Response frameworks, review solicitation programmes, and conflict resolution protocols for Google, Trustpilot, and industry-specific platforms."},
            {"title": "Content Strategy", "body": "Strategic content — press coverage, thought leadership, case studies, and testimonials — that builds positive search equity over time."},
            {"title": "Monitoring & Alerting", "body": "Real-time brand monitoring with escalation protocols for negative sentiment spikes, potential crises, and competitor activity."},
        ],
        [
            {"title": "Proactive, not reactive", "body": "We build positive reputation before a crisis, not just respond when something goes wrong."},
            {"title": "Search-first", "body": "What ranks on page one matters most. Our content strategy is designed to own the SERP for your brand name."},
            {"title": "Crisis-ready", "body": "Response playbooks and activation procedures ready before you need them."},
            {"title": "Long-term focus", "body": "Reputation is built over months and years — not in a single campaign. Our programmes are designed for sustained improvement."},
        ],
        "Need to protect or rebuild your brand's online reputation?",
    ),
    "aria": "/what-we-do/marketing/",
})

PAGES.append({
    "path": "/what-we-do/marketing/pr",
    "title": "Digital PR",
    "meta": "GreaterHeight's Digital PR service delivers media relations, press release distribution, and digital PR programmes that build authority and generate high-quality backlinks.",
    "og": "marketing.jpg",
    "schema": webpage_schema("/what-we-do/marketing/pr", "Digital PR", "Media relations and digital PR for authority building and link acquisition."),
    "css": MKT_CSS,
    "html": marketing_page(
        "/what-we-do/marketing/pr", "Digital PR",
        "Digital Marketing — Digital PR",
        "Earn Media Coverage That<br>Builds Authority",
        "Digital PR combines the brand-building power of traditional media relations with the SEO benefit of high-quality editorial backlinks — positioning your brand in the publications your target audience trusts, and earning the domain authority that moves your website up the rankings.",
        [
            {"num": "50+", "label": "Media Placements Per Year"},
            {"num": "DR 50+", "label": "Average Domain Rating of Placements"},
            {"num": "Tech + Finance + Health", "label": "Media Verticals Covered"},
            {"num": "Nigeria + Global", "label": "Media Reach"},
        ],
        "<p>Digital PR is different from traditional PR in one important respect: the coverage it generates has a measurable, lasting value in search. A placement in TechCabal, BusinessDay, or The Guardian builds brand credibility — and the backlink from that placement improves your domain authority for months and years afterwards.</p><p>Our Digital PR programmes are built to generate both brand exposure and SEO value simultaneously — with stories, data, and angles engineered to earn coverage from journalists who care about their audience.</p>",
        [
            {"title": "Story Development", "body": "Identifying the data, angles, and narratives that journalists in your target publications will want to cover — then crafting them into pitchable stories."},
            {"title": "Media Relations", "body": "Established relationships with technology, finance, and business journalists across Nigeria, Africa, and global publications."},
            {"title": "Press Release Distribution", "body": "Targeted press release distribution to relevant journalists and editors — not spray-and-pray wire services."},
            {"title": "Coverage Tracking", "body": "Real-time monitoring of coverage and backlinks, with monthly reports on domain authority impact and brand mention sentiment."},
        ],
        [
            {"title": "Editorial-quality content", "body": "Coverage comes from journalists choosing to cover you — not advertorial placements disguised as editorial."},
            {"title": "SEO-integrated", "body": "Link acquisition strategy aligned with your SEO keyword and domain authority targets."},
            {"title": "Nigerian media expertise", "body": "We know TechCabal, Nairametrics, BusinessDay, Punch Tech, and the journalists who cover the African technology story."},
            {"title": "Measurable outcomes", "body": "Coverage volume, domain rating of placements, and estimated search impact are tracked and reported monthly."},
        ],
        "Ready to earn media coverage that builds lasting authority?",
    ),
    "aria": "/what-we-do/marketing/",
})

# ═══════════════════════════════════════════════════════════════════════════════
# ENTERPRISE SUB-PAGE: Blockchain
# ═══════════════════════════════════════════════════════════════════════════════
blockchain_css = HERO_CSS + STAT_CSS

blockchain_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">What We Do — Enterprise Technology</div>
      <h1>Blockchain Solutions for<br>Regulated African Industries</h1>
      <p class="hero-lead">Smart contracts, enterprise blockchain platforms, tokenisation systems, and distributed ledger applications — built for the compliance, performance, and operational realities of African financial services, public sector, and supply chain.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start a Blockchain Project</a>
        <a href="/what-we-do/enterprise/" class="btn-secondary">Enterprise Services</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stats-row reveal">
        <div class="stat-box"><div class="stat-num">15+</div><div class="stat-label">Blockchain Engagements</div></div>
        <div class="stat-box"><div class="stat-num">3</div><div class="stat-label">Blockchain Platforms (Ethereum, Hyperledger, Solana)</div></div>
        <div class="stat-box"><div class="stat-num">CBN</div><div class="stat-label">eNaira-Compatible Development</div></div>
        <div class="stat-box"><div class="stat-num">SEC</div><div class="stat-label">Nigeria Digital Asset Framework Aware</div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap two-col reveal">
      <div>
        <h2>Blockchain for Enterprise, Not Speculation</h2>
        <p>GreaterHeight's blockchain practice focuses on enterprise use cases where distributed ledger technology solves a genuine business problem: supply chain provenance, cross-border payments, identity verification, land registry, and document authentication.</p>
        <p>We work with private and consortium blockchains for most enterprise clients — where performance, privacy, and regulatory compliance matter more than decentralisation for its own sake. We also build on public chains where the use case demands it.</p>
        <p>Every engagement starts with a critical question: does this problem actually need a blockchain? If a traditional database with strong access controls and audit logging solves it better, we say so.</p>
      </div>
      <div class="cards-grid" style="margin-top:0;">
        <div class="card">
          <h3>Smart Contracts</h3>
          <p>Solidity, Rust, and Go smart contracts — audited, tested, and deployed on Ethereum, Hyperledger Fabric, or Solana.</p>
        </div>
        <div class="card">
          <h3>Enterprise Chains</h3>
          <p>Private and consortium blockchain networks built on Hyperledger Fabric — with the performance and privacy controls enterprise clients require.</p>
        </div>
        <div class="card">
          <h3>Tokenisation</h3>
          <p>Asset tokenisation systems for real estate, securities, and commodities — built to CBN and SEC Nigeria regulatory frameworks.</p>
        </div>
        <div class="card">
          <h3>DeFi & Payments</h3>
          <p>Cross-border payment systems, stablecoin integrations, and DeFi protocol development for regulated financial services.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Blockchain Use Cases We've Built</h2>
      <div class="cards-grid reveal">
        <div class="card">
          <h3>Supply Chain Provenance</h3>
          <p>End-to-end product tracking systems for FMCG manufacturers — giving retailers and consumers verifiable provenance from farm to shelf.</p>
        </div>
        <div class="card">
          <h3>Cross-Border Payments</h3>
          <p>Low-cost, near-real-time cross-border payment rails for microfinance banks and remittance operators using blockchain settlement.</p>
        </div>
        <div class="card">
          <h3>Document Verification</h3>
          <p>Tamper-proof document issuance and verification systems for academic credentials, land titles, and regulatory certificates.</p>
        </div>
        <div class="card">
          <h3>Smart Contract Automation</h3>
          <p>Automated contract execution for trade finance, insurance payouts, and procurement — eliminating manual reconciliation and fraud risk.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Exploring a blockchain use case?</h2>
      <p>We'll give you an honest assessment of whether blockchain is the right solution — and build it if it is.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/what-we-do/enterprise/" class="btn-secondary">Enterprise Services</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/what-we-do/enterprise/blockchain",
    "title": "Blockchain Solutions",
    "meta": "GreaterHeight builds enterprise blockchain platforms, smart contracts, tokenisation systems, and distributed ledger applications for African regulated industries.",
    "og": "what-we-do.jpg",
    "schema": webpage_schema("/what-we-do/enterprise/blockchain", "Blockchain Solutions", "Enterprise blockchain platforms and smart contracts for African regulated industries."),
    "css": blockchain_css,
    "html": blockchain_html,
    "aria": "/what-we-do/enterprise/",
})

# ═══════════════════════════════════════════════════════════════════════════════
# PRODUCTS HUB
# ═══════════════════════════════════════════════════════════════════════════════
products_css = HERO_CSS + """
.product-showcase{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.75rem;margin-top:2rem;}
.product-card{background:#fff;border-radius:12px;border:1px solid var(--border);overflow:hidden;display:flex;flex-direction:column;transition:box-shadow .2s,transform .2s;}
.product-card:hover{box-shadow:0 10px 36px rgba(0,0,0,.12);transform:translateY(-4px);}
.product-card-header{padding:2rem 2rem 1.5rem;}
.product-logo-area{margin-bottom:1.2rem;}
.product-logo-area span{font-size:1.5rem;font-weight:900;color:var(--forest-deep);}
.product-card-header h3{font-size:1.1rem;font-weight:700;color:var(--forest-deep);margin-bottom:.5rem;}
.product-card-header p{font-size:.88rem;color:var(--txt-2);line-height:1.6;margin:0;}
.product-card-footer{margin-top:auto;padding:1rem 2rem 1.5rem;border-top:1px solid var(--border);display:flex;gap:.75rem;flex-wrap:wrap;}
.prod-tag{display:inline-block;background:var(--bg-2);color:var(--teal-mid);font-size:.72rem;font-weight:700;padding:.25rem .65rem;border-radius:12px;text-transform:uppercase;letter-spacing:.07em;}
"""

products_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Our Products</div>
      <h1>Software Products Built<br>for the African Market</h1>
      <p class="hero-lead">Beyond client services, GreaterHeight Technologies builds and maintains its own portfolio of software products — addressing real gaps in the African enterprise, education, and consumer markets.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Our Product Portfolio</h2>
      <div class="product-showcase reveal">

        <div class="product-card">
          <div class="product-card-header">
            <div class="product-logo-area"><span style="color:var(--cr);">Digital</span><span>Siwes</span></div>
            <h3>DigitalSiwes</h3>
            <p>A digital platform for managing SIWES (Students Industrial Work Experience Scheme) placements, supervisor assignments, logbook submissions, and institutional reporting — replacing paper-based processes for Nigerian universities and polytechnics.</p>
          </div>
          <div class="product-card-footer">
            <span class="prod-tag">EdTech</span>
            <span class="prod-tag">Nigeria</span>
            <a href="/products/digitalsiwes/" style="font-size:.82rem;font-weight:700;color:var(--cr);margin-left:auto;">Learn More →</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-card-header">
            <div class="product-logo-area"><span style="color:var(--teal-mid);">Search</span><span>Artisans</span></div>
            <h3>SearchArtisans</h3>
            <p>A marketplace platform connecting skilled artisans — electricians, plumbers, carpenters, welders — with homeowners and businesses across Nigeria. Verified profiles, transparent pricing, and real-time booking.</p>
          </div>
          <div class="product-card-footer">
            <span class="prod-tag">Marketplace</span>
            <span class="prod-tag">Consumer</span>
            <a href="/products/searchartisans/" style="font-size:.82rem;font-weight:700;color:var(--cr);margin-left:auto;">Learn More →</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-card-header">
            <div class="product-logo-area"><span style="color:var(--forest-deep);">eCert</span><span style="color:var(--cr);">Man</span></div>
            <h3>eCertMan</h3>
            <p>A certificate management platform for educational institutions — digital issuance, blockchain-verified authentication, and instant verification for employers and academic institutions worldwide.</p>
          </div>
          <div class="product-card-footer">
            <span class="prod-tag">EdTech</span>
            <span class="prod-tag">Blockchain</span>
            <a href="/products/ecertman/" style="font-size:.82rem;font-weight:700;color:var(--cr);margin-left:auto;">Learn More →</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-card-header">
            <div class="product-logo-area"><span style="color:var(--cr);">Matrimony</span><span style="color:var(--gold);">Roll</span></div>
            <h3>MatrimonyRoll</h3>
            <p>A culturally-aware matrimonial platform built for Nigerian and diaspora users — with family verification features, ethnic and religious preference matching, and diaspora search functionality.</p>
          </div>
          <div class="product-card-footer">
            <span class="prod-tag">Consumer</span>
            <span class="prod-tag">Social</span>
            <a href="/products/matrimonyroll/" style="font-size:.82rem;font-weight:700;color:var(--cr);margin-left:auto;">Learn More →</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-card-header">
            <div class="product-logo-area"><span style="color:var(--forest-deep);">GreaterHeight</span></div>
            <h3>GreaterHeight Academy</h3>
            <p>A technology training platform offering structured courses in software development, data engineering, cloud computing, and AI — built for working professionals and graduates in the Nigerian technology ecosystem.</p>
          </div>
          <div class="product-card-footer">
            <span class="prod-tag">EdTech</span>
            <span class="prod-tag">Training</span>
            <a href="/products/greaterheight-academy/" style="font-size:.82rem;font-weight:700;color:var(--cr);margin-left:auto;">Learn More →</a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap two-col reveal">
      <div>
        <h2>Why We Build Products</h2>
        <p>Client services and products reinforce each other at GreaterHeight. Our product work gives our engineers hands-on experience with the full product lifecycle — from idea and design through to growth, support, and maintenance. That experience makes them better engineers on client projects.</p>
        <p>It also gives us direct insight into the African technology market: what users actually need, what they will pay for, and where the existing solutions fall short. This market insight shapes the advice we give our consulting clients.</p>
      </div>
      <div>
        <div class="card">
          <h3>Solving Real Problems</h3>
          <p>Each product addresses a gap we identified through our work — SIWES management, artisan discovery, certificate fraud, diaspora matrimony.</p>
        </div>
        <div class="card" style="margin-top:1rem;">
          <h3>Built on Our Own Standards</h3>
          <p>Our products are built to the same engineering standards we apply to client work — the same code review, testing, and deployment processes.</p>
        </div>
        <div class="card" style="margin-top:1rem;">
          <h3>Open to Partnership</h3>
          <p>We are open to white-label arrangements, reseller partnerships, and institutional licensing for all five products.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Interested in one of our products?</h2>
      <p>Whether you want a demo, a white-label arrangement, or a partnership discussion — we are open to the conversation.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Get in Touch</a>
        <a href="/services/" class="btn-secondary">Our Services</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/products",
    "title": "Our Products",
    "meta": "GreaterHeight Technologies' product portfolio — DigitalSiwes, SearchArtisans, eCertMan, MatrimonyRoll, and GreaterHeight Academy, built for the African market.",
    "og": "products.jpg",
    "schema": webpage_schema("/products", "Our Products", "Software products by GreaterHeight Technologies for the African market."),
    "css": products_css,
    "html": products_html,
    "aria": None,
})

# ═══════════════════════════════════════════════════════════════════════════════
# WHY NIGERIA
# ═══════════════════════════════════════════════════════════════════════════════
wn_css = HERO_CSS + STAT_CSS + """
.why-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin-top:2rem;}
.why-item{padding:2rem;background:#fff;border-radius:8px;border:1px solid var(--border);border-top:4px solid var(--teal-glow);}
.why-item h3{font-size:1.05rem;font-weight:700;color:var(--forest-deep);margin-bottom:.7rem;}
.why-item p{font-size:.88rem;color:var(--txt-2);line-height:1.7;margin:0;}
"""

wn_html = """
<main>
  <section class="page-hero">
    <div class="wrap">
      <div class="eyebrow">Why Nigeria</div>
      <h1>Nigeria: Africa's Technology<br>Engineering Hub</h1>
      <p class="hero-lead">Why are global technology companies, startups, and enterprises increasingly building their engineering teams in Nigeria? The answer is talent, scale, time zones, and cost — but it is more nuanced than any single factor.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Build Your Team Here</a>
        <a href="/services/development-centres/" class="btn-secondary">Our Development Centres</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stats-row reveal">
        <div class="stat-box"><div class="stat-num">220M+</div><div class="stat-label">Population — Africa's Largest</div></div>
        <div class="stat-box"><div class="stat-num">50K+</div><div class="stat-label">New Software Engineers Annually</div></div>
        <div class="stat-box"><div class="stat-num">GMT+1</div><div class="stat-label">Compatible with European Working Hours</div></div>
        <div class="stat-box"><div class="stat-num">#1</div><div class="stat-label">African Country for VC Investment in Tech</div></div>
        <div class="stat-box"><div class="stat-num">40%</div><div class="stat-label">Typical Cost Saving vs UK / US Teams</div></div>
        <div class="stat-box"><div class="stat-num">English</div><div class="stat-label">Official Language — Zero Translation Overhead</div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="wrap">
      <h2>Six Reasons Global Companies Build in Nigeria</h2>
      <div class="why-grid reveal">
        <div class="why-item">
          <h3>1. Depth of Engineering Talent</h3>
          <p>Nigeria produces over 50,000 software engineering graduates annually — a talent pool that is growing at over 20% per year. The University of Lagos, Covenant University, Obafemi Awolowo University, and dozens of private technology institutes produce engineering graduates at a scale that few African countries can match. The ecosystem is deepened by a thriving self-taught developer community and dozens of coding bootcamps producing industry-ready engineers.</p>
        </div>
        <div class="why-item">
          <h3>2. English-Language Proficiency</h3>
          <p>Nigeria's official language is English. This is not a minor detail: it eliminates the communication overhead, documentation challenges, and cultural friction that make engineering teams in non-English-speaking countries significantly harder to manage. Nigerian engineers communicate fluently in written and spoken English — in code reviews, Slack, Confluence, and stakeholder meetings.</p>
        </div>
        <div class="why-item">
          <h3>3. Time Zone Compatibility</h3>
          <p>Nigeria operates on West Africa Time (WAT, GMT+1) — one hour ahead of the UK and within two hours of most European business hours. This makes real-time collaboration with European clients natural, without the asynchronous friction that affects teams in Asia. It also provides meaningful overlap with the East Coast of the United States during afternoon working hours.</p>
        </div>
        <div class="why-item">
          <h3>4. Cost-Effectiveness</h3>
          <p>Comparable engineering talent in Nigeria costs 40–60% less than equivalent talent in the UK, US, or Western Europe — without the quality compromise that characterised offshore engineering 15 years ago. The gap is narrowing as the market matures, but it remains significant for companies looking to extend their engineering capacity without proportionally extending their cost base.</p>
        </div>
        <div class="why-item">
          <h3>5. A Thriving Technology Ecosystem</h3>
          <p>Lagos is home to the most active technology startup ecosystem in Africa — with hundreds of funded startups, multiple co-working and incubation spaces, and a venture capital community that invested over $1 billion in Nigerian startups in recent years. This environment breeds engineers with startup experience: comfortable with ambiguity, ownership-oriented, and accustomed to building production systems under real-world constraints.</p>
        </div>
        <div class="why-item">
          <h3>6. Market Proximity</h3>
          <p>For companies building products for African markets — the fastest-growing consumer markets in the world — there is no substitute for having engineers who live and operate in those markets. Nigerian engineers building fintech for Nigerian users bring the domain knowledge, cultural context, and product instinct that engineers working from London or New York simply cannot replicate.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap two-col reveal">
      <div>
        <h2>The Honest Trade-offs</h2>
        <p>We believe in honest assessments. Building an engineering team in Nigeria offers significant advantages — but it also requires deliberate effort in a few areas:</p>
        <ul style="margin-top:1rem;padding-left:1.5rem;line-height:2;color:var(--txt-2);">
          <li><strong>Infrastructure reliability:</strong> Power and internet reliability in Lagos requires engineering teams to invest in backup infrastructure. GreaterHeight's development centres are fully equipped with redundant power and connectivity.</li>
          <li><strong>Talent retention:</strong> High-performing Nigerian engineers receive competing offers frequently. Competitive compensation, clear career paths, and a strong culture are non-negotiable for retention.</li>
          <li><strong>Onboarding time:</strong> As with any international team, onboarding takes deliberate investment in the first 30–60 days. The return on that investment is significant.</li>
        </ul>
        <p>GreaterHeight's development centre model is specifically designed to manage these trade-offs — with the infrastructure, HR, and cultural investment already in place.</p>
      </div>
      <div>
        <div class="card">
          <h3>GreaterHeight's Role</h3>
          <p>We serve as the bridge between global ambition and Nigerian execution. Our development centres give international clients access to Nigeria's talent pool without the complexity of setting up an independent subsidiary, navigating Nigerian employment law, or managing infrastructure from overseas.</p>
        </div>
        <div class="card" style="margin-top:1rem;">
          <h3>Built Here, Trusted Globally</h3>
          <p>Our track record of shipping production systems for clients in the UK, US, and across Africa demonstrates what Nigerian engineering teams can deliver when properly structured, managed, and supported.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-band reveal">
    <div class="wrap">
      <h2>Ready to build your team in Nigeria?</h2>
      <p>GreaterHeight can establish your development centre, place engineers with your team, or deliver your project end-to-end from Lagos.</p>
      <div class="hero-cta-row">
        <a href="/contact/" class="btn-primary">Start the Conversation</a>
        <a href="/services/development-centres/" class="btn-secondary">Our Development Centres</a>
      </div>
    </div>
  </section>
</main>
"""

PAGES.append({
    "path": "/why-nigeria",
    "title": "Why Nigeria? Africa's Technology Engineering Hub",
    "meta": "Why global companies build engineering teams in Nigeria — talent depth, English proficiency, time zone compatibility, cost-effectiveness, and ecosystem maturity.",
    "og": "why-nigeria.jpg",
    "schema": webpage_schema("/why-nigeria", "Why Nigeria? Africa's Technology Engineering Hub", "Six reasons global companies build engineering teams in Nigeria."),
    "css": wn_css,
    "html": wn_html,
    "aria": None,
})


# ═══════════════════════════════════════════════════════════════════════════════
# GENERATE ALL PAGES
# ═══════════════════════════════════════════════════════════════════════════════
created = []
errors = []

for page in PAGES:
    url = page["path"]
    # Build the directory
    page_dir = ROOT + url
    os.makedirs(page_dir, exist_ok=True)

    try:
        html = build_page(
            url_path=url,
            title=page["title"],
            meta_desc=page["meta"],
            og_image=page["og"],
            schema_json=page["schema"],
            page_css=page["css"],
            page_html=page["html"],
            aria_current_href=page.get("aria"),
        )
        out_path = f"{page_dir}/index.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        size = os.path.getsize(out_path)
        created.append(f"  ✓ {url}/index.html ({size:,} bytes)")
    except Exception as e:
        errors.append(f"  ✗ {url}: {e}")

print(f"\nGenerated {len(created)} pages:\n")
print("\n".join(created))
if errors:
    print(f"\nErrors ({len(errors)}):\n")
    print("\n".join(errors))
