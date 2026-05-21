# Performance Final Report - 2026-05-21

## Summary

Implemented safe static-site performance improvements focused on LCP, render-blocking resources, image weight, script loading, and accessibility/SEO Lighthouse failures.

Production was not redeployed from this environment, so final production PageSpeed Insights and production Lighthouse must be rerun after deployment. The table below compares local production-server Lighthouse before and after the changes.

## Before vs After - Local Lighthouse

| Strategy | Performance | Accessibility | Best Practices | SEO | FCP | LCP | CLS | TBT | Speed Index | TTFB |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mobile baseline | 54 | 77 | 100 | 90 | 4.5 s | 27.2 s | 0 | 400 ms | 4.5 s | 0 ms |
| Mobile final | 92 | 100 | 100 | 100 | 2.1 s | 3.2 s | 0 | 0 ms | 2.2 s | 0 ms |
| Desktop baseline | 75 | 76 | 100 | 90 | 0.9 s | 5.4 s | 0 | 20 ms | 0.9 s | 0 ms |
| Desktop final | 100 | 100 | 100 | 100 | 0.5 s | 0.7 s | 0 | 0 ms | 0.9 s | 0 ms |

## Production Baseline

| Strategy | Performance | Accessibility | Best Practices | SEO | FCP | LCP | CLS | TBT | Speed Index | TTFB |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mobile production baseline | 61 | 77 | 100 | 90 | 2.5 s | 20.9 s | 0 | 410 ms | 10.5 s | 200 ms |
| Desktop production baseline | 76 | 76 | 100 | 90 | 0.7 s | 5.2 s | 0 | 0 ms | 1.2 s | 150 ms |

The PageSpeed Insights API returned unauthenticated quota errors (`429 RESOURCE_EXHAUSTED`), so production PageSpeed field data was unavailable.

## Improvements Made

- Replaced the LCP CSS background image with a browser-discoverable `<picture>`/`img` using AVIF, WebP, and optimized JPEG variants.
- Added `fetchpriority="high"` and image preload for the hero asset.
- Generated optimized responsive image assets for hero, section background, about background, and Open Graph image.
- Removed CSS `@import` chaining and unused blocking CSS dependencies.
- Replaced full Bootstrap CSS with the small grid/flex utility subset used by this page.
- Removed unused Bootstrap/Popper JavaScript from the page.
- Deferred remaining local scripts.
- Lazy-loaded the Google Maps iframe.
- Added `font-display: swap` to the local Font Awesome font face.
- Fixed the Analytics tag ID mismatch so the page no longer requests two UA IDs.

## Remaining Blockers to 100/100

Mobile Performance is 92 locally. Remaining constraints:

- `style.css` and `css/classy-nav.css` are still render-blocking because they protect first-paint layout and mobile navigation stability.
- Legacy jQuery and `js/plugins/plugins.js` still ship unused code, mostly to preserve the existing mobile nav/sticky/scroll behavior safely.
- Google Analytics remains a third-party script.
- The local `http-server` does not gzip text assets, while GitHub Pages production normally serves compressed text assets. Production after deploy may score differently.
- Google Maps is lazy-loaded, but the iframe can still be requested by Lighthouse because it sits within the page and is considered near enough to the viewport under some lab conditions.

## Verification

- `npx -y html-validate index.html` passed.
- JSON-LD parsed successfully with `JSON.parse`.
- `xmllint --noout sitemap.xml` passed.
- Local `robots.txt`, `sitemap.xml`, `llms.txt`, and `humans.txt` returned `200`.
- Browser smoke test loaded `http://127.0.0.1:4174/`, clicked `Contacto`, verified the contact section, checked mobile viewport, and reported no console warnings/errors.
- Final Lighthouse reports saved:
  - `lighthouse-local-home-mobile-final.report.json/html`
  - `lighthouse-local-home-desktop-final.report.json/html`

## Deployment Notes

- Deploy these static files to GitHub Pages as usual.
- After deploy, rerun PageSpeed Insights and Lighthouse against `https://demoreto.com/`.
- Production scores may differ from local because of GitHub Pages CDN, compression, cache headers, and third-party script timing.
