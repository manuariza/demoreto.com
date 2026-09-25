# DeMoreto — new website, ready for design review

Built 25 September 2026. Local preview: http://localhost:8765/new-design/

## Delivered

- 136 generated HTML pages under `/new-design/`.
- Homepage, restoration catalogue, all 16 original paintings and their individual pages, studio biography, contact page, searchable publication archive.
- 16 edited restoration/studio stories, including Virgen de Tómalos, Juan de Anchieta, Ricardo Balaca, Francisco Díaz Carreño, and sculpture/paper conservation.
- 98 individual archive pages, preserving the original publication texts and ordered media. The two El Cid posts are also combined in an edited project.
- Artwork zoom, keyboard-accessible dialogs, mobile navigation, restoration filters, archive search, direct email enquiries and copy-address contact, native video playback and actual video thumbnails.
- FMR-inspired split opening, classical typography, thin catalogue rules, short fragment-grid introduction. ARTWORLD-inspired information columns, ARTU-style facts, quiet image sequences, and restrained moving typography.
- Web derivatives of all paintings; 16 genuine close detail crops. Originals in Downloads were left intact.

## Instagram coverage

The public profile was paginated using its normal Show more control and optional dialog Close buttons. The final timeline response returned `has_next_page: false`.

- Discovered: **98 unique public feed posts**.
- Archived: **98 / 98**.
- Media: **249 images + 26 videos = 275 files**.
- Original posts without a caption: **19**. These remain represented, with their media.
- Publication dates: **2019-01-01 through 2023-03-03**.
- Every declared carousel count reconciled with the saved media. Every image decoded; every video passed a duration probe. Each media file has a SHA-256 digest in the manifest.

This establishes coverage of the publicly listed feed retrieved on the inspection date. It does not claim access to deleted/private posts, private account information, or expired stories. No login credentials were used.

Files: `reports/content-archive/instagram.json`, `all-public-links.json`, `pagination-evidence.json`, `verification.json`. Downloaded media is in `new-design/assets/restoration/`. The manifest preserves the studio's captions, source links, publication timestamps, ordered files, counts, sizes, and checksums. Unrelated comments and full browser payloads were removed from that manifest.

## Validation

- All generated local asset and page links resolve.
- No image decode failures or video metadata failures.
- Desktop 1440px and mobile 390px: no horizontal overflow, missing loaded images, or browser script errors on the representative page types.
- Mobile menu and Escape, zoom dialog and Escape, sculpture filtering, archive search, artwork enquiry context, and video loading passed browser checks.
- Reduced-motion users skip the introduction and scroll-driven text movement.
- All review pages include `noindex,nofollow`; the production sitemap and current homepage are unchanged.

## Remaining review items

- Updated: all 16 room/gallery slots now contain generated visualizations. See `reports/image-production/README.md` for prompts, assets and checks.
- Painting names retain their source filename wording; year, medium, physical dimensions, prices and availability were not invented.
- Current studio address and telephone need reconciliation. The existing site and Instagram disagree, so the new site gives Madrid and the existing email address.
- Current memberships/advisory roles and the status of the Tegeo catalogue were not presented as current facts without confirmation.
- Attribution and technical facts on restoration pages follow Antonio's posts; the preserved archive is source material, not an independently fact-checked art-history catalogue.
- This build is available locally. It has **not been pushed or deployed to demoreto.com**.

## Maintenance

No dependencies or package-manager configuration were changed.

- Rebuild HTML and image derivatives: `python3 scripts/build-new-design.py` (uses existing Pillow and ffmpeg).
- Verify files, media and archive reconciliation: `python3 scripts/verify-new-design.py`.
- Serve locally: `python3 -m http.server 8765 --bind 127.0.0.1`.
- The archive scripts use the existing local Playwright installation and bundled Chromium, with an isolated browser profile. They do not install packages.

The original site remains at the repository root. The new design is self-contained under `new-design/`; its navigation is rooted at `/new-design/`.
