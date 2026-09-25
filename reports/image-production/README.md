# DeMoreto — emblem, artwork settings and contact revision

Delivered 25 September 2026 with the built-in image generation tool. No API/CLI fallback or new dependencies were used.

## Assets

- Original engraved D/M emblem with acanthus, brush and conservation spatula: `new-design/assets/brand/demoreto-emblem.png`; transparent, lossless web derivative `.webp`.
- Sixteen generated installation settings: `new-design/assets/contexts/{artwork-slug}.png`, with `.webp` versions used by the website.
- Each painting has one dedicated setting. Doble A/B and Tanguy 1/2 have multi-work gallery views, with the page's painting dominant.
- The prompt set and paths for all 17 generated assets are recorded in `generations.json`.

All outputs were visually reviewed against the supplied artwork references. Generated settings are illustrative and are not pixel-identical reproductions or evidence of actual installations. Original artwork photographs remain the authoritative full-work and detail images. Site captions identify AI visualizations and explain that the room, framing and scale are illustrative; physical artwork dimensions have not been supplied.

## Website changes

The shared generator embeds the emblem across all 136 pages and replaces all sixteen room-image placeholders with zoomable settings. Existing source paintings and restoration evidence were not edited.

The Contacto form has been removed. Visitors can open an email draft with a direct mailto link or copy the address to use webmail. Painting enquiries retain their title in the email subject. Nothing is sent automatically, no form text needs to be entered before opening email, and no third-party form service is configured.

GitHub Pages serves static HTML/CSS/JavaScript; server-side message delivery would need an external endpoint. Official source: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

## Checks

All sixteen context images loaded on their respective artwork pages. No placeholders remained. Context zoom, email subject propagation, copy-to-clipboard, desktop header and mobile contact layout were verified. Browser check results: `checks.json`.

Local review: http://localhost:8765/new-design/
The revision has not been pushed or deployed.
