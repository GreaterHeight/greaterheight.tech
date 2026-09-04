# GreaterHeight Technologies — v8 Production Hardening

## Completed
- Absolute canonical URLs for all HTML pages.
- Open Graph and Twitter metadata on all pages.
- Branded 1200×630 default social image.
- Favicon PNG variants.
- Absolute sitemap URLs; 404 excluded.
- robots.txt references the canonical sitemap.
- llms.txt added.
- Improved image alt text and async decoding.
- Removed bogus client-logo self-navigation links.
- Removed unused ecoico font declaration.
- Production CSS/JS renamed to v8.
- 404 marked noindex, nofollow.
- Print stylesheet and additional focus states.
- Contact form no longer falsely claims that a message was sent; it remains a client-side form until a real endpoint is configured.

## Deployment note
The static site is intentionally backend-free. Before accepting real contact submissions, configure the form to use a trusted server-side or serverless endpoint and add the endpoint to the deployment security policy.

## Security headers
Recommended at the hosting layer: Content-Security-Policy, Referrer-Policy, X-Content-Type-Options, Permissions-Policy, and an appropriate Strict-Transport-Security policy after HTTPS is confirmed.
