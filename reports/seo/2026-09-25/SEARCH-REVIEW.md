# Technical search review — DeMoreto — 25 September 2026

## Status and scope

Locally verified. No deployment, Git push, DNS change or Search Console mutation performed. The live site still uses the previous one-page design. The redesign's public URL returns 404. Its local preview remains noindex,follow. Visible content and design were preserved: all 137 body-markup hashes match the pre-change snapshot.

Review followed the blueprint's search-discovery-plan.md and SEARCH-REVIEW-template.md. Target audience: people seeking art conservation/restoration in Madrid and Antonio G. Ariza's original paintings. Desired outcome: relevant enquiries to the studio, not impressions alone.

## Production evidence from Search Console

Property: sc-domain:demoreto.com; observed in the user's authenticated session on 25 September 2026.

- Indexing report (updated September 21): 1 indexed URL; 2 redirect URLs and 1 alternate with a proper canonical. These exclusions do not, by themselves, indicate defects.
- Homepage inspection: URL is on Google; last crawl September 23 at 04:33:13 as Googlebot smartphone; crawl and indexing allowed; successful fetch; both declared and selected canonical are https://demoreto.com/.
- Sitemap https://demoreto.com/sitemap.xml: Success, 1 discovered page; submitted May 21, last read May 28. URL Inspection separately reports no referring sitemap; this does not negate the successful sitemap report or indexed status.
- Performance: Web (text), all countries/devices, June 23–September 22, 2026: 1 click, 29 impressions, CTR 3.4%, average position 31.2. Four visible query rows; these do not account for every impression. Sample too small for causal/ranking conclusions.
- The property's beta Generative AI features report exists: same date range, 3 impressions, all attributed to the homepage. This is Google-specific evidence, not proof of ChatGPT visibility; do not add this to Web totals without checking overlap.
- Core Web Vitals (updated September 23): insufficient usage data over the last 90 days for both desktop and mobile. This is unavailable evidence, not a pass or failure.

Direct public HTTP checks: HTTPS root, robots.txt and sitemap.xml return 200; HTTP and www converge on the HTTPS apex; nonexistent route and /new-design/ return 404. See live-http.json. Python's local CA configuration failed; system curl verified TLS successfully without disabling verification.

## Implemented technical changes

- Unique page metadata for the main landing, collections, studio, contact, paintings and restoration stories. Homepage search title: Restauración de arte en Madrid | DeMoreto. Visible heading stays unchanged.
- Self-referencing canonical URLs without query parameters. Preview canonicals stay in /new-design/; the separate launch build consistently uses root URLs.
- Open Graph/Twitter title, description and original page image; language es, locale es_ES, theme color.
- Factual JSON-LD: WebSite, WebPage, ProfessionalService, Person, BreadcrumbList and VisualArtwork where applicable. No invented dates, prices, dimensions, reviews or promises of rich results. Existing incorrect assumptions about social identity are avoided by using the supplied studio Instagram profile.
- Preview retains noindex; follow allows linked-resource discovery. No robots.txt block that would conceal noindex.
- Explicit launch builder creates a separate root-site artifact, with 39 canonical sitemap URLs and primary image entries. Raw archive records remain available with noindex,follow. The archive index, 17 curated stories and all 16 paintings are indexable alongside homepage/studio/contact/collections.
- Conservative archive policy: source records can duplicate curated stories and 19 have no captions. This is not a permanent requirement: individually reviewed, useful archive records can later be promoted. No content was deleted.
- Launch robots.txt allows crawling, including Googlebot, Bingbot and OAI-SearchBot via the wildcard rule. Existing training-crawler policy is unchanged.
- Launch llms.txt lists public canonical pages as an informational aid only.

## Verification

prepare-search-release.py produced a separate release in /private/tmp/demoreto-seo-release-final-20260925. It does not publish or overwrite the live repository root.

verify-search-release.py checked 137 pages, 39 sitemap entries, 98 excluded archive records, canonical consistency, parseable JSON-LD, one H1 per page, unique indexable descriptions, local asset/link resolution, all preview exclusions and unchanged body markup. Zero errors. Existing archive/media verification also passed. No dependency changes.

## Remaining launch steps

1. Publish the approved redesign at https://demoreto.com/ using the prepared root build. Preserve the homepage URL, HTTPS and www redirects. Existing production has one canonical page, so no indexed path migration is currently evidenced. url-mapping.tsv records preview-to-root mapping, not an assertion that redirects are already installed.
2. Publish its sitemap.xml and robots.txt atomically with the pages. Do not submit the candidate sitemap before those URLs return 200. Exclude/remove preview duplicates or keep their noindex if retained. GitHub Pages does not implement arbitrary server redirects from a _redirects file.
3. Validate homepage, one restoration, one painting, studio and contact with live URL Inspection; resubmit the existing sitemap URL and request homepage indexing after deployment. The current live sitemap is already accepted, so resubmission of unchanged old content was unnecessary today.
4. Run production PageSpeed Insights and structured-data validation on deployed URLs. Current local checks are not field Core Web Vitals or Google rich-result validation. Preserve the requested intro design; its 1.5-second minimum and up-to-4-second duration are a perceived-performance tradeoff to measure, not a proven ranking penalty.
5. Check crawl/index/canonical adoption after Google recrawls. Compare impressions, clicks and qualified enquiries only after sufficient exposure; annotate launch date and avoid attributing every change to metadata. Owner: site operator/Manuel. Trigger: launch and subsequent crawl, no automation scheduled.

## Other recommendations without design changes

- Verify the actual Google Business Profile and consistent public business details for local discovery. This was outside the provided account and not edited.
- The legacy homepage contains obsolete Universal Analytics UA tags; the redesign contains none. Choose a valid measurement setup if enquiry attribution is wanted; no tracking or consent changes were introduced.
- Bing Webmaster Tools was not connected. Submit the live sitemap there after launch if access is available.
- Crawl permission is verified from robots.txt, not from provider-specific crawler logs. Citation/inclusion and ranking are not guaranteed.

## Official guidance checked

- Google AI features: https://developers.google.com/search/docs/appearance/ai-features
- Google generative AI optimization: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google sitemap guidance: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- OpenAI crawler controls: https://developers.openai.com/api/docs/bots

Google requires no special AI schema/file and ignores llms.txt for ranking. OpenAI distinguishes OAI-SearchBot (search discovery) from GPTBot (training). Technical eligibility enables discovery but cannot promise ranking or citations.
