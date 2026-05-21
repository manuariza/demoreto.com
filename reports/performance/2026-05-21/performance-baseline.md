# Performance Baseline - 2026-05-21

## Scope

- Repository: `/Users/manuariza/Sites/demoreto.com`
- Production site: `https://demoreto.com/`
- Public routes discovered: `/` only. Navigation is in-page anchors: `#home`, `#about`, `#contact`.
- PageSpeed Insights API: attempted for mobile and desktop. The unauthenticated API returned `429 RESOURCE_EXHAUSTED`, so production Lighthouse CLI was used as the fallback.

## Stack Discovery

- Framework: no application framework detected.
- Build system: none detected. The site is a static GitHub Pages-style HTML/CSS/JS site.
- Routing model: single `index.html` page with anchor sections.
- Rendering mode: static HTML, no SSR/ISR/build-time rendering.
- Image handling: manually referenced local JPEG/PNG assets. Hero and section images are CSS background images.
- Font loading: remote Google Fonts imported from `style.css`; local Font Awesome/icon fonts loaded through CSS.
- CSS strategy: root `style.css` imports Bootstrap, navigation, carousel, animation, popup, and Font Awesome CSS through CSS `@import`.
- JavaScript: jQuery 2.2.4, Bootstrap, Popper, bundled plugins, and `js/active.js`.
- Analytics/third-party scripts: Google Analytics/gtag is loaded asynchronously, but the script ID and configured ID differ (`UA-136088881-1` vs `UA-115459133-1`).
- Sitemap/robots: no `robots.txt` or `sitemap.xml` in repository or production.
- Metadata: minimal title and viewport; empty meta description; no canonical, Open Graph, Twitter Card, theme color, or structured data.
- Deployment assumptions: `CNAME` points GitHub Pages at `demoreto.com`.

## Baseline Commands

- Existing build/test/lint commands: none found because there is no `package.json` or framework config.
- HTML validation baseline: `npx -y html-validate index.html`
- Production audits: Lighthouse CLI against `https://demoreto.com/`
- Local audits: `npx -y http-server /Users/manuariza/Sites/demoreto.com -p 4174 -c-1 --silent`, then Lighthouse CLI against `http://127.0.0.1:4174/`
- Browser engine: Playwright cached Google Chrome for Testing, not the installed Chrome app.

## Baseline Scores

| Environment | Strategy | Performance | Accessibility | Best Practices | SEO | FCP | LCP | CLS | TBT | Speed Index | TTFB |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Production Lighthouse | Mobile | 61 | 77 | 100 | 90 | 2.5 s | 20.9 s | 0 | 410 ms | 10.5 s | 200 ms |
| Production Lighthouse | Desktop | 76 | 76 | 100 | 90 | 0.7 s | 5.2 s | 0 | 0 ms | 1.2 s | 150 ms |
| Local Lighthouse | Mobile | 54 | 77 | 100 | 90 | 4.5 s | 27.2 s | 0 | 400 ms | 13.1 s | 0 ms |
| Local Lighthouse | Desktop | 75 | 76 | 100 | 90 | 0.9 s | 5.4 s | 0 | 20 ms | 1.5 s | 0 ms |

INP was not available from Lighthouse lab runs. PageSpeed field data was unavailable because the API request was quota blocked.

## Key Findings

- LCP element: the CSS background hero image `img/bg-img/1.jpg` on `.slide-bg-img`.
- LCP blocker: `img/bg-img/1.jpg` is 2.4 MB as a 1920x1288 JPEG and is discovered late through inline CSS background loading.
- Image opportunities: Lighthouse estimates roughly 3.1 MB savings from modern image formats and roughly 2.3 MB from optimized images across `1.jpg`, `2.jpg`, and `3.jpg`.
- Render-blocking resources: `style.css` chains multiple CSS `@import` files; jQuery, Bootstrap, and plugins are parser-blocking at the end of the document.
- Unused JavaScript: gtag/analytics and `js/plugins/plugins.js` dominate unused JS. Mobile production showed about 163 KiB estimated unused JS savings.
- Unused CSS: Bootstrap is mostly unused; production showed about 20 KiB estimated savings in the Lighthouse compressed transfer context.
- Font loading: Google Fonts and Font Awesome lack an explicit `font-display` strategy.
- Third-party impact: Google Tag Manager/Analytics, Google Maps, and Google Fonts add transfer and connection overhead. Google Maps is below the fold but loaded immediately through an iframe.
- Accessibility failures: low-contrast gray text, skipped heading levels, and icon-only social links without accessible names.
- SEO failure: empty meta description. Missing canonical/social metadata and structured data are outside the basic Lighthouse SEO score but important for search/AI discoverability.

## Raw Artifacts

- `pagespeed-production-home-mobile.json` and `pagespeed-production-home-desktop.json`: PageSpeed API quota errors.
- `pagespeed-production-summary.json`: PageSpeed API error summary plus production Lighthouse fallback summary.
- `lighthouse-production-home-mobile.report.json/html`
- `lighthouse-production-home-desktop.report.json/html`
- `lighthouse-local-home-mobile.report.json/html`
- `lighthouse-local-home-desktop.report.json/html`
- `lighthouse-local-summary.json`
- `lighthouse-production-summary.json`

## Safe Improvement Priorities

1. Add crawl/indexing essentials: `robots.txt`, `sitemap.xml`, canonical metadata, meta description, Open Graph/Twitter metadata, and structured data.
2. Replace the LCP background-image pattern with an eager, fetch-prioritized `<picture>`/`img` hero so the browser discovers the hero image immediately.
3. Generate optimized AVIF/WebP/JPEG image variants for the large background images.
4. Lazy-load the below-the-fold map iframe and non-critical background sections.
5. Add `defer` to local scripts and reduce unnecessary JS execution where safe.
6. Improve contrast, heading hierarchy, link names, iframe title, and semantic landmarks.
