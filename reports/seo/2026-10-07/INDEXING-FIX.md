# Search indexing repair — 7 October 2026

## Diagnosis and change

Search Console's report (last updated 4 October) showed 35 URLs excluded by noindex, 31 discovered but not yet indexed, two redirects and one alternate canonical. All 35 noindex examples were individual public `/archivo/` records. The September launch intentionally excluded all 98 original archive records, while allowing 39 main/curated pages. The archive records contain original public studio notes and/or photographic sequences and are now eligible for search alongside the main pages.

- Removed noindex from all 98 production archive records.
- Expanded the canonical sitemap from 39 to 137 URLs, retaining primary images.
- Improved archive descriptions to use the original note or an accurate photographic-documentation description rather than navigation and boilerplate.
- Updated the release exporter and verifier so a rebuild preserves the production indexing policy. All 137 `/new-design/` previews remain noindex and outside the production sitemap.
- Preserved historical launch evidence: the release tools no longer overwrite the September reports.
- No dependencies, package managers, design or visible body content changed.

## Verification

`python3 scripts/verify-search-release.py .` passes: 137 pages, 137 sitemap URLs, 98 indexable archive records, 137 excluded previews, unchanged visible bodies and no errors. A separate export and verification also pass; its sitemap URL set matches production.

GitHub Pages successfully built implementation commit `e2eb2d2e6bdef0172b1ec61b8948ef75fadde417`. Direct HTTPS checks of every production sitemap URL passed (137/137): HTTP 200, no redirect, expected self canonical, no robots meta or X-Robots-Tag indexing block. See `live-validation.json`.

The HTTP homepage variants redirect permanently to `https://demoreto.com/`. `/index.html` correctly declares `/` as its canonical. Those three Search Console exclusions are expected; changing them to force separate indexing would create duplicate homepage URLs. The preview remains noindex. See `live-routing.json`.

## Search Console actions

On 7 October, through the signed-in Search Console browser:

- Noindex issue (35 URLs): Validation Started.
- Discovered, currently not indexed (31 URLs): Validation Started.
- Expanded `https://demoreto.com/sitemap.xml`: Sitemap submitted successfully. The table still showed 39 discovered URLs from its last read on 1 October; that is historical data, while the live sitemap already contains 137.

- Google live URL test for `https://demoreto.com/archivo/Bu3mI6eHfoB/`: URL is available to Google; Page can be indexed; one valid Breadcrumbs item. This verifies the new page fetched by Google, whereas the stored index inspection still reflects the 4 October noindex crawl.

- Indexing request for that archive URL accepted: Google confirmed it was added to a priority crawl queue.

## Google processing

Website eligibility is verified; Google still controls recrawling and indexing. Validation requests and a sitemap submission do not guarantee every URL will be indexed, especially photographic records with little text. Search Console's historical counts will persist until Google refreshes its reports.
