# DeMoreto Post-Review Verification

Date: 2026-05-21
Repository: `manuariza/demoreto.com`
Local URL: `http://127.0.0.1:4174/`
Production URL: `https://demoreto.com/`

## Git Diff Review

Changed file categories:

- HTML/content: `index.html`
- CSS/layout: `style.css`, `css/font-awesome.min.css`
- Images/assets: optimized hero, section, about, and Open Graph image variants under `img/`
- SEO/crawl files: `robots.txt`, `sitemap.xml`, `llms.txt`, `humans.txt`
- Reports: Markdown audit summaries under `reports/`
- Repo hygiene: `.gitignore` for bulky generated Lighthouse/PSI/validation artifacts

Post-review risk fixes:

- Removed an unused generated `img/bg-img/2-section-800.jpg` variant that was not referenced.
- Restored the hero text-box sizing that produced the stronger mobile LCP result while keeping the optimized responsive hero image.
- Preserved the existing Google Analytics configuration and did not remove analytics.
- Kept `jquery`, `plugins.js`, and `active.js`; `active.js` uses the plugin stack for ClassyNav, sticky navigation, scroll-up, and related behavior.
- Replaced the footer `document.write()` copyright year with a static fallback plus a small DOM update.
- Fixed the footer wordmark accessible-name mismatch.
- Added `.gitignore` entries so large raw Lighthouse/PSI HTML/JSON artifacts stay local; concise Markdown reports are intended to be committed.

## Final Lighthouse

Local Lighthouse CLI, Chrome for Testing, static `http-server`.

| Route | Device | Performance | Accessibility | Best Practices | SEO | FCP | LCP | TBT | CLS | Speed Index |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `/` | Mobile | 91 | 100 | 100 | 100 | 2.1 s | 3.2 s | 10 ms | 0 | 2.3 s |
| `/` | Desktop | 100 | 100 | 100 | 100 | 0.5 s | 0.7 s | 0 ms | 0 | 0.5 s |

Mobile did not improve beyond the previously reported 92. The kept final run is 91; repeated local mobile Lighthouse runs showed LCP variance around the hero image render delay. I did not make riskier CSS or script rewrites just to chase one point.

## Remaining Blockers

- Mobile Performance is still constrained by render-blocking site/nav CSS, remaining legacy `jquery`/`plugins.js`, Google Analytics, and local `http-server` not serving text compression like production/CDN hosting normally should.
- Removing `jquery`/`plugins.js` was not safe: navigation and page behavior depend on the legacy plugin layer.
- Critical CSS extraction was left unchanged because the site is static and the current CSS organization is safer and more durable than brittle inline critical CSS.
- Raw Lighthouse HTML/JSON reports are intentionally ignored to keep the repository clean.

## SEO and Discoverability Validation

Passed:

- `robots.txt` points to `https://demoreto.com/sitemap.xml`
- `sitemap.xml` contains the canonical production homepage URL only
- canonical URL is `https://demoreto.com/`
- Open Graph image URL is absolute
- Twitter card is `summary_large_image`
- JSON-LD parses and contains truthful `WebSite`, `WebPage`, `Person`, and `ProfessionalService` entities
- `html lang="es"`
- exactly one `h1`
- no accidental `noindex` or `nofollow`
- `llms.txt` is factual and clearly marked as experimental/non-guaranteed

## Visual and Functional Smoke Test

Playwright Chromium was used after the in-app browser became unavailable mid-check. Results:

- Mobile `390x844`, tablet `768x1024`, and desktop `1280x900` rendered with no horizontal overflow.
- Hero image rendered correctly with no broken images.
- Mobile menu toggled open.
- `Contacto` navigation scrolled to `#contact`.
- Map iframe remained lazy-loaded and titled.
- Footer/social links had accessible labels.
- Console warnings/errors: none.
- Failed local asset requests: none.

## Verification Commands

- `git diff --check`
- `npx -y html-validate index.html`
- `xmllint --noout sitemap.xml`
- Node JSON-LD and SEO invariant checks
- local crawl/status check for `/`, `/robots.txt`, `/sitemap.xml`, `/llms.txt`, `/humans.txt`, key CSS/JS/image assets
- Playwright Chromium responsive smoke test
- Lighthouse CLI mobile and desktop final pass

## Deployment Safety

Safe to deploy after commit. Production PageSpeed Insights should be rerun after deployment because the local server does not mirror GitHub Pages/CDN compression and cache behavior.
