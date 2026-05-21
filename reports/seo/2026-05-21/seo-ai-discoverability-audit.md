# SEO and AI Discoverability Audit - 2026-05-21

## Scope

- Production site: `https://demoreto.com/`
- Public pages discovered: `/`
- Important sections: `#home`, `#about`, `#contact`
- Production status checks saved to `status-baseline.csv`.
- HTML validation baseline saved to `html-validate-baseline.txt`.

## Crawlability and Indexability

- `https://demoreto.com/` returns `200`.
- `http://demoreto.com/` redirects to `https://demoreto.com/`.
- `https://www.demoreto.com/` redirects to `https://demoreto.com/`.
- `https://demoreto.com/index.html` returns `200`, creating a duplicate URL risk unless canonicalized.
- `https://demoreto.com/robots.txt` returns `404`.
- `https://demoreto.com/sitemap.xml` returns `404`.
- No `noindex`/`nofollow` directives were found.
- Critical page text is present in static HTML, not client-side-only content.
- Internal links cover the visible single-page sections.

## Metadata

- Title exists but is generic: `DeMoreto`.
- Meta description exists but is empty.
- No canonical tag.
- Viewport tag exists.
- Favicon exists.
- `html lang` is currently `en`, but the visible content is Spanish.
- No Open Graph metadata.
- No Twitter/X Card metadata.
- No theme color.
- No hreflang. The site appears Spanish-only, so hreflang is not required.

## Structured Data

- No JSON-LD structured data detected.
- Appropriate additions:
  - `WebSite`
  - `Person` for Antonio G. Ariza, because the page presents an individual professional/restorer.
  - `ProfessionalService` or `LocalBusiness` only if kept factual and consistent with visible contact/location content.
  - `WebPage`
- Not appropriate:
  - `FAQPage`, because no visible FAQ exists.
  - Fake reviews, fake organization claims, or unverifiable awards.

## Content Quality

- Homepage clearly names the brand and discipline, but search snippets have little metadata context because the description is empty.
- The about section includes useful, crawlable professional credentials.
- Contact details are crawlable, though the email is intentionally obfuscated with spaces.
- Heading hierarchy needs improvement: the hero subtitle uses `h4` after the main heading, and contact subtitle uses `h6`.
- No visible meaningful `<img>` elements require alt text because major visuals are CSS backgrounds; however, converting the hero to an image will need descriptive alt text.
- Icon-only Instagram/LinkedIn links need accessible labels.
- The content is lean but not spammy. No low-value SEO pages should be added just to increase page count.

## AI/Search Assistant Readiness

- Strengths:
  - Static, crawlable HTML.
  - Clear professional biography section.
  - Public contact/location/social links.
- Weaknesses:
  - Empty meta description and generic title make summaries less accurate.
  - Missing structured data makes entity extraction harder.
  - Missing `robots.txt` and `sitemap.xml` remove useful crawl hints.
  - No concise machine-readable site map or page descriptions for assistants.
  - `html lang="en"` conflicts with Spanish content.
- Recommended safe additions:
  - Accurate Spanish title and description.
  - JSON-LD with factual person/service details.
  - `robots.txt` and canonical `sitemap.xml`.
  - Optional `llms.txt` as a harmless curated map of important public URLs, clearly labeled experimental.

## Accessibility Issues Relevant to SEO

- Low contrast text in contact/footer areas.
- Heading order failures.
- Icon-only social links without text alternatives.
- Google Maps iframe lacks a `title`.
- Deprecated `align` attribute and inline styles reduce maintainability.

## Implementation Priorities

1. Add metadata, canonical URL, social tags, correct language, and structured data.
2. Add `robots.txt`, `sitemap.xml`, optional `llms.txt`, and optional `humans.txt`.
3. Improve semantic landmarks and accessible names without changing visual branding.
4. Keep content people-first; do not add keyword-stuffed or hidden content.
5. Re-run local Lighthouse and HTML validation after changes, then rerun PageSpeed Insights on production after deployment.
