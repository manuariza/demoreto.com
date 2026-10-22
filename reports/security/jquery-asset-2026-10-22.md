# Correct the vendored jQuery filename

Dependabot alerts #2 (GHSA-rmxg-73gg-4p98) and #6 (GHSA-6c3j-c64m-qhgq)
identify `js/jquery/jquery-2.2.4.min.js` as jQuery 2.2.4. The existing file
actually contains jQuery 3.7.1, byte-for-byte identical to the official minified
distribution at https://code.jquery.com/jquery-3.7.1.min.js .

Rename that asset to `js/jquery/jquery-3.7.1.min.js`. SHA-256 remains
`fc9a93dd241f6b045cbff0481cf4e1901becd0e12fb45166a8f17f95823f0b1a`.
No library version, file contents, dependency manifest or lockfile changes.

No current source references the old filename; the current website uses its own
`site.js` and does not load jQuery. No script reference or public page therefore
needs editing. The site has image galleries and email contact links rather than
the former template's slider/contact form.

Validation: the existing release verifier passed all 137 published pages and
sitemap entries, with unchanged visible bodies and no broken local links.
Playwright checks confirmed mobile menu navigation, gallery image opening and
closing, image loading, focus return, and contact-address copying. No email or
contact message was sent. Confirm live asset bytes, Pages publication and the two
alert states after merging; do not dismiss an alert as a substitute for checking.
