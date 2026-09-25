# DeMoreto production launch — 25 September 2026

## Rollback checkpoint

Annotated Git tag: `before-redesign-2026-09-25`.
Previous live commit: `4a1f115d2d2c02b994f56cbc4a7de030940ffbee`.
The tag was pushed before changing the production site. The previous design and all its tracked files remain retrievable from this tag and Git history.

## Published build

GitHub Pages source: `master`, repository root. Custom domain: `demoreto.com`, HTTPS enforced.
The approved preview was exported to root URLs, with 137 HTML pages, 39 indexable sitemap URLs, 98 noindex source records and 391 referenced assets. Preview remains available at `/new-design/` with noindex. Main pages use index,follow,max-image-preview:large. Canonicals and internal URLs point to the production root.

Includes the approved portrait, Tanguy 1 / Chapel / Sunset 3 featured paintings, six-engraving intro, DM favicon, direct contact email, full restoration archive and generated artwork room views. Source assets, generation prompts, curation and build scripts are retained in the repository. No new dependencies.

## Pre-push verification

- Release verifier: all page canonicals, sitemap membership, JSON-LD parsing, one H1, local links/assets, preview exclusions and body equality against the approved preview passed.
- Chromium at 1440px and 390px: home, Chapel, Florero, studio and contact loaded without script/HTTP errors or horizontal overflow. Image zoom and updated portrait passed.
- Production-root intro loaded and exited successfully.
- The prior SEO review describes the prelaunch baseline; this release supersedes its 'not deployed' state once Pages reports this commit built.

## Recovery

To view the previous version without affecting production: create a separate checkout/worktree at `before-redesign-2026-09-25`.
To roll back this launch while preserving history: revert the launch commit and push the revert to `master`; GitHub Pages will redeploy it. Avoid force-pushing or resetting the published branch.

## Rebuild

`python3 scripts/build-new-design.py` refreshes the preview (requires Pillow, the original Antonio Art folder and ffmpeg for missing video posters).
`python3 scripts/prepare-search-release.py /tmp/a-new-empty-release-folder` exports an isolated production tree.
`python3 scripts/verify-search-release.py /tmp/a-new-empty-release-folder` validates it against the current approved preview.
Copy that tree into the repository root, inspect the changes, commit and push. The script alone does not deploy.
