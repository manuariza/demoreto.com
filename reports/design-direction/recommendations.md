> Historical design recommendation. The full implementation now supersedes the limited prototype scope below; see [build-review.md](build-review.md).

**DeMoreto: recommended design and content direction**

Prepared 25 September 2026 from the existing DeMoreto site, the local design corpus, the five references selected by the client, the Antonio Art folder, and a limited public inspection of Instagram. This is a design recommendation and content plan; the redesigned website has not been implemented.

Franco Maria Ricci should become the main reference for the whole site: a classical editorial identity, a clearly ordered catalogue, large artwork images, and generous individual work pages. ARTWORLD, ARTU, Wallpaper Projects, and Maëlan Le Meur should contribute specific behaviours within that identity.

The proposed positioning is a conservation studio led by Antonio G. Ariza, with a substantial, distinct collection of his original paintings. The visitor should always be able to tell whether Antonio created a work or restored it. Both deserve beautiful presentation, but their evidence, captions, and page narratives differ.

**What was checked.** All five references exist in the local corpus. Their archived design descriptions were compared with live pages. Live captures include the FMR home and Erté book page, ARTWORLD's Marc Hibbert page, ARTU's Taptap product page, Wallpaper Projects' Emma Scully Gallery project, and the Maëlan landing sequence. The FMR loader was captured while visible. ARTWORLD's left information column remained in position while the image sequence advanced horizontally. Initial Maëlan captures were still loading; the later settled captures show its oversized moving typographic composition. Desktop observations do not establish mobile behaviour or complete accessibility compliance.

The assets contain 16 full-work JPEG photographs and 20 square crops. The public Instagram view exposed 12 post/reel links; one full restoration caption was saved. The public view displayed sign-in prompts. This is not a complete Instagram media archive, and the number 12 is not a verified total for the account.

| Reference | Role in DeMoreto | Specific elements to adapt | Limits of the adaptation |
|---|---|---|---|
| [Franco Maria Ricci](https://www.francomariaricci.com/en) | Main visual system, homepage, catalogue, object pages | Classical display serif; orderly divisions; a large image beside compact editorial copy; selected-work shelves; room for several images on each object page; short grid introduction | Preserve DeMoreto's own identity. Replace sales categories with relevant curatorial labels. Create original introductory imagery instead of borrowing the publisher's emblems. |
| [ARTWORLD artist page](https://artworld.agency/artists/marc-hibbert-copycopy) | Relationship between metadata and artwork | Quiet, persistent information column; artwork receives most of the available width; easy access to biography or enquiry | Use a shorter, more readable information column. Prefer ordinary vertical scrolling for the main DeMoreto sequence. On mobile, place information in the normal document flow. |
| [ARTU product page](https://artu.works/item/taptap) | Facts and image presentation on individual works | A clear work title; technical information organized into rows; alternation between complete object, details, and contextual images | Use only verified artwork data. A 360° viewer requires genuine multi-angle imagery and adds little to these flat paintings. Commerce controls are unnecessary until a sales requirement is established. |
| [Wallpaper Projects project page](https://wallpaperprojects.com/blogs/projects/cast-iron-emma-scully-gallery) | Calm contextual photography and image pacing | Warm neutral setting; large installation image; smaller complementary image; generous space between views | Keep a regular page structure. Room images supplement the complete painting. Avoid treating an artwork as a repeating wallpaper texture. |
| [Maëlan Le Meur](https://maelanlemeur.com/) | One or two expressive text passages | Large words moving gently with scroll; section transitions driven by typography | Apply movement to a brief statement or chapter title. Keep body copy, credentials, project facts, and contact information stable. |

The recommendation is deliberately hierarchical. A visitor should recognize one DeMoreto website across every page, rather than recognize the source reference each time the layout changes.

**The classical character should come from typography, proportion, and editing.** A pale paper background, near-black text, thin rules, a restrained antique-gold accent, and a high-contrast serif can connect historical painting with Antonio's contemporary work. The paintings should supply almost all of the colour. The gold is most useful in dividers and occasional large details; small functional text needs strong contrast.

Use one coherent display serif and one quiet supporting typeface. A Bodoni/Didone character is the appropriate starting point for titles, but the final typeface needs readable small sizes and a valid web licence. The corpus's font names and numeric tokens are reference evidence, not a requirement to reuse proprietary font files. Headlines can have classical character while paragraphs remain comfortable to read. Avoid distressed paper overlays, decorative faux ageing, excessive gold, and tiny museum labels that become difficult to read.

Use clear, sharp image edges, consistent captions, and aligned text columns. Give a painting space without enlarging every block into a full-screen section. A work's title, authorship, and the next action should remain easy to find. This is especially important on the restoration pages, where the visitor is assessing professional competence.

**The proposed navigation is simple:** Restauración · Obra de Antonio · El estudio · Contacto. Spanish should be the default because the existing business content is Spanish and the studio is in Madrid. An English edition can use the same page structure after the Spanish content is verified. Antonio's original artwork should have a clearly visible route from the homepage and the main navigation.

An eventual client preview can use `/new-design/` for the landing page, `/new-design/restauracion/` for its project index, `/new-design/restauracion/[proyecto]/` for a case study, `/new-design/obra/` for original paintings, `/new-design/obra/[pieza]/` for a painting, and corresponding studio/contact pages. These are proposed routes, not published pages. Preview pages should stay out of the production sitemap and use noindex while under review.

**The homepage should establish the studio and then guide the visitor through a small number of well-edited chapters.**

| Sequence | Content and presentation | Purpose |
|---|---|---|
| 1. Opening | DeMoreto, a concise restoration positioning line, Madrid, and one commanding image. Use FMR's relationship between a narrow text area and a much larger image. | Establish what the business does before the visitor interprets the images. |
| 2. Selected restorations | Three strong projects in a regular catalogue row with title, object type, and a concise intervention description. | Make expertise visible immediately. |
| 3. Antonio and the studio | Portrait or genuine studio photograph, a short biography, and a small number of verified credentials. | Explain whose judgement the client is trusting. |
| 4. Original paintings | A distinct introduction to Obra de Antonio, followed by four to six selected complete works. | Give the artist's practice a substantial place while keeping authorship clear. |
| 5. Material and process | A brief typographic passage with texture details or genuine restoration documentation. | Provide the expressive moment inspired by Maëlan, without slowing down practical reading. |
| 6. Enquiry | Clear ways to discuss a restoration or ask about an original painting; verified location and contact details. | Turn interest into a useful conversation. |

The opening should ideally feature an actual restored work or the studio at work. If an original painting is used as the initial visual, label it explicitly as Antonio's own work. Do not let a historical work in the restoration collection appear to be his original creation.

The FMR bestsellers pattern translates well into “Restauraciones seleccionadas” and “Obras seleccionadas.” There is no need to invent bestsellers, prices, editions, availability, or rankings. Initially curated order is more useful than elaborate filtering. Three strong examples with complete stories are more convincing than many unfinished project pages.

**The opening grid can become a distinctive DeMoreto detail.** The captured FMR introduction confirms the grid of changing graphic motifs the client noticed. DeMoreto could use nine or twelve small fragments from Antonio's paintings, alternating with original studio-related marks if suitable assets exist. The current square crops are good candidates for this moment.

Treat this as a brief entrance gesture, ideally around half a second to one second on the first visit, with a direct transition into the landing image. It should never impose a minimum wait after the page is ready. If loading is genuinely slow, keep the page usable and use local image placeholders rather than hold the visitor in an indefinite animation. Returning navigation should be immediate. Reduced-motion preferences should receive a static or skipped introduction.

The grid should use lightweight thumbnails and should not require downloading the full painting files. An elegant introduction loses its value if it delays viewing the art or obstructs a visitor arriving directly at a project page.

**The original-artwork catalogue should respect the actual collection.** The sixteen full-work photographs are varied: atmospheric landscape-like compositions, strong red or green passages, tall textured works, and unusually wide panoramas. The source filenames identify the pieces, but their final capitalization, accents, and numbering should be confirmed with Antonio. In particular, a filename ending in “1” or “2” should not automatically be interpreted as a version, series number, or duplicate.

The default gallery should be a calm two- or three-column catalogue with complete images contained inside generously spaced cells. Consistent caption baselines and a regular rhythm will give it the order the client prefers. The panoramic works can occupy a dedicated full-width row. Avoid a dense, irregular masonry arrangement that makes the visitor work to understand the collection.

“Agar,” “Algas,” and “Coral” are approximately six times as wide as they are high. Their source heights are only 816–876 pixels despite their large widths. They are excellent for long catalogue plates or contextual placement above a console, but poor candidates for deep artificial zoom or tall hero crops. Works such as “Nubes,” “La ola,” and “Chapel” offer more balanced starting compositions. “Marte,” “Barcelo,” and the “Doble” files need portrait presentations. These are visual observations and provisional filename references, not confirmed artistic series or physical dimensions.

The 20 square crops are a useful detail library, but their generic filenames do not reliably identify the parent painting. Some also have a similar colour palette to one another. Before assigning them to individual pages, map each crop to its full work and verify the match. A 3000 × 3000 export is not by itself evidence of 3000 pixels of original detail; avoid promising more enlargement than the source supports.

**Each painting should have a real object page.** On a wide screen, allocate roughly one quarter of the page to quiet information and three quarters to imagery, adapted from the relationship observed in ARTWORLD. Keep the FMR type, rules, and spacing throughout. A complete, uncropped painting comes first. Then show a deliberate image sequence: an overall view, one or two genuine texture details, and a contextual room or gallery view when available.

The information column can contain the title, Antonio's name, confirmed year, medium, physical dimensions, a short description, and an enquiry link. Missing information should remain an editorial task or be omitted from the client-facing page. Do not fabricate technique, provenance, exhibition history, price, or availability to make the template appear complete. “Consultar sobre esta obra” works well while sales arrangements remain unspecified.

For long image sequences, keep a compact version of the title and enquiry visible; a full biography does not need to occupy a persistent sidebar. On mobile, show the title, the complete painting, the essential facts, and then the image sequence in a normal vertical flow. An optional fullscreen viewer should provide zoom, clear close controls, keyboard operation, and captions. It must not replace ordinary page navigation.

**Restoration pages need a different reading sequence.** They should answer what the object is, what condition it was in, what Antonio investigated, what work he performed, and what the documented outcome was. They can retain the same classical visual system while behaving like illustrated conservation case studies.

| Original painting page | Restoration case-study page |
|---|---|
| Authorship: Antonio G. Ariza | Original artist or attribution, if known; restoration credit to Antonio/DeMoreto |
| Primary image: full artwork | Primary image: documented overall view with a clearly stated condition/stage |
| Sequence: complete work → details → setting | Sequence: initial condition → investigation → intervention → result |
| Metadata: title, medium, size, year | Metadata: object, artist/attribution, period, support/material, scope of work, intervention date if confirmed |
| Main purpose: appreciate the work and enquire | Main purpose: understand the studio's judgement, process, and experience |
| Optional generated context, clearly described as a visualization | Actual documentary evidence throughout |

A typical restoration page can open with a short summary and an overall image, then move through “Estado inicial,” “Estudio,” “Intervención,” and “Resultado.” A modest table of contents may stay visible on desktop for a long case. A brief video can demonstrate a documented process, with a poster, playback controls, and explanatory caption.

Use before/after sliders only when the source photographs depict the same area with sufficiently similar angle, scale, and lighting. Otherwise, a labeled pair of images is more honest and often more readable. If Instagram supplies only a precomposed before/after collage, preserve it as a labeled comparison or request the two original files; do not create an apparently precise slider from incompatible crops.

Captions should state what each photograph shows. Where attribution is uncertain, preserve the wording “atribuido a,” “taller de,” or equivalent in the source. A work's creation year, the date of treatment, and the date of its Instagram post are different fields.

**A real pilot case is already identifiable.** The public [3 March 2023 Instagram post about “Virgen de Tómalos”](https://www.instagram.com/moreto_restauracion/p/CpUxKd9j7q6/) identifies the work as 1756, O/L, 200 × 140 cm. Antonio's caption describes extensive surface deposits, insect-related damage, canvas deformation, tears and holes, and earlier improvised patches. It also explains that part of the surface alteration was irreversible. That makes it a strong candidate for a case about diagnosis, treatment decisions, and the limits of intervention.

The website could turn this into a concise introduction followed by photographs of the whole work, its surface, damaged areas, the reverse, and the documented result. The caption refers to several images, but the complete carousel has not been downloaded or verified in this research. The original artist and actual intervention date are not established by the captured caption. This is a candidate story, not a completed case study.

**Instagram should become a source archive from which we edit projects.** It should not dictate the website's structure. One object can appear in several posts, and one carousel can contain different treatment stages. Group by restored object/project, retain the original posts as source records, and then create an editorial sequence that a visitor can understand. Preserve the original Spanish caption alongside the edited website text so claims remain traceable.

The public inspection found twelve exposed links and a sign-in prompt when browsing. A public scraper may obtain some current media, but this run does not establish access to the entire account history, every carousel child, or all videos. No complete image/video archive has been created.

**The recommended collection method is an account-owner export.** Meta places its information-download tools in Accounts Center; see [Meta's explanation](https://about.fb.com/news/2023/10/manage-your-information-across-apps/) and the [Instagram export help page](https://help.instagram.com/181231772500920). The help page itself returned a rate-limit response during this research. Exact labels vary between account/app versions, so “Export your information” may appear as “Download your information.”

1. Sign in to the `moreto_restauracion` account in Instagram.
2. Open Settings → Accounts Center → Your information and permissions → Export/Download your information.
3. Create an export for this Instagram profile and choose export/download to the device.
4. Select all available content categories relevant to this project: posts, reels/videos, and archived stories if wanted and offered. Avoid sending private-message or security data with the website assets.
5. Set the date range to All time, the format to JSON, and media quality to the highest available option.
6. Request the export and download every archive part when Meta makes it available. Keep the original ZIP files unchanged.
7. Provide the content export for ingestion. We can build a local visual index, preserve captions and timestamps, link carousel children to their posts, and identify missing files.

This is the strongest starting point, but the contents must still be verified. An export cannot recover deleted or expired material that Meta no longer retains, and the highest available export quality is not a guarantee of the original camera files. For the few restoration cases selected as homepage features, ask Antonio for original photographs if the Instagram versions cannot support the required display size.

An authenticated API integration may be useful later for eligible professional accounts and ongoing updates. It requires account authorization and setup; it is not a public download of any arbitrary profile and should not be confused with a complete historical backup. Meta's [official Instagram API collection](https://www.postman.com/meta/instagram/overview) is the starting reference. For this redesign, a verified export is a more direct first step. No scraping package, dependency, or package-manager setting has been installed or changed.

The import should record post ID or source identifier, permalink where available, publication date, raw caption, ordered media items, image dimensions, video duration, local filename, and download/validation status. It should distinguish cover thumbnails from original carousel items and video files. Preserve the raw export outside the published website directory, create a separate edited content collection, and publish only selected assets.

Completion should mean that every exported post has a record; each listed media file exists and opens; carousel order is preserved; video files play; caption text and Spanish characters remain intact; and missing entries are reported. A folder of cover images is not a complete archive. We should reconcile counts with the account or owner, while allowing for profile-count differences caused by archived or separately listed content.

**Generated room imagery belongs after the page compositions are approved.** The source paintings already provide enough material to build the catalogue and detail pages. Use those real images now. Reserve placeholders only for views we do not yet have, such as a painting in a room, a gallery installation, or a new studio photograph.

For each future contextual image, specify the exact painting, the intended page and slot, aspect ratio, physical scale if known, wall material, lighting direction, framing treatment, camera distance, and surrounding furniture. A small consistent family of settings will feel more credible than sixteen unrelated decorative interiors. Suitable directions include a quiet white gallery, a restrained Madrid interior with warm plaster and dark wood, and a close oblique view that explains the work's material presence.

The painting itself must remain faithful to the supplied photograph. Image generation can change brushwork, marks, edges, and colour even when instructed not to, so the finished result needs comparison against the source. For exact fidelity, generate the environment and place the original painting image into that environment as a controlled final step. A contextual visualization should be captioned as such and should not imply an exhibition, installation, or sale that did not occur. Restoration evidence must remain documentary; generated before/after results would undermine the purpose of those pages.

For the first client preview, I would produce only two or three contextual views after approving one painting page. This tests the visual direction before creating images for the wider collection.

**Motion should reinforce the sequence.** Use the short grid introduction, gentle image reveals, and one expressive statement inspired by Maëlan. A possible draft line is “Conservar la materia. Comprender su historia.” Antonio should approve any statement that represents his practice. Keep normal scrolling, readable text, clear focus states, and a static reduced-motion version. Avoid animating every paragraph or requiring visitors to wait for content to become readable.

**Image quality needs an explicit delivery strategy.** The sixteen source photographs total roughly 144.5 MiB. Those originals should stay intact, with separate web derivatives sized for their actual use. Catalogue thumbnails, large page images, texture details, and fullscreen views need different resolutions. Load the first important image promptly and defer the rest of a long gallery. Reserve each image's space to prevent page jumps. Test texture fidelity after compression; smooth-looking files can erase precisely the material detail this website should communicate. Keep colour handling consistent and avoid a site-wide filter over the art.

**The biography and contact details need reconciliation before publication.** The current website states an Art History degree from Universidad Complutense de Madrid, conservation/restoration training, professional memberships, and a research focus on nineteenth-century Spanish painting. These support the recommended scholarly tone, but current memberships, advisory roles, and the status of the Rafael Tegeo catalogue project should be checked with Antonio. The existing wording describes that publication as forthcoming; it should not be carried into the redesign without confirmation.

Instagram lists Calle de Moreto, 28014 Madrid; the current website lists Calle de Españoleto, 28010 Madrid. Neither should silently replace the other. Confirm the current studio address, telephone, enquiry email, and preferred public name. Also replace the outdated Instagram link in the current site with the client-confirmed account during implementation.

**The practical sequence is content first, then a small complete prototype, then expansion.**

1. Obtain the Instagram content export; inventory media and captions; confirm the current biography and contact information.
2. Map the existing crops to their parent paintings and confirm titles and available artwork facts. Choose a small set of restoration cases with sufficient documentation.
3. Build the homepage, artwork index, one fully developed painting page, restoration index, one fully developed restoration case, and the studio/contact content under `/new-design/`.
4. Review those pages on desktop and mobile using real source images. Validate that the visitor understands authorship, finds the restoration service, can inspect details, and can enquire easily.
5. Define the exact missing image slots and create the small first batch of room/gallery visualizations. Review painting fidelity and consistency with the site.
6. Expand the remaining artwork and restoration records using the approved templates, verify captions and image order, then complete client review before production replacement.

The first client preview should demonstrate the full experience through a few finished pages. Unverified facts should be visible in an internal content checklist, while the public-facing draft uses only substantiated information. Pending contextual images should have a purposeful reserved slot in the prototype; generic placeholder images should not compete with the real art already available.

**Files supporting this recommendation:** [full-work contact sheet](/Users/manuariza/Sites/demoreto.com/reports/design-direction/full-artwork-contact-sheet.jpg), [detail-crop contact sheet](/Users/manuariza/Sites/demoreto.com/reports/design-direction/crops-contact-sheet.jpg), [asset inventory](/Users/manuariza/Sites/demoreto.com/reports/design-direction/artwork-assets.csv), [limited public Instagram index](/Users/manuariza/Sites/demoreto.com/reports/design-direction/instagram-public-index.json), and [sample source caption](/Users/manuariza/Sites/demoreto.com/reports/design-direction/instagram-sample-caption.json). The reference captures are in `reference-captures/`.

The local corpus records used are `franco-maria-ricci-editore--6120469b`, `wallpaper-projects--0a2bcda6`, `artu--d1941450`, `maelan-le-meur--ea0d7b5a`, and `artworld--bab94db1`, under `/Users/manuariza/Sites/design-corpus/refero-library/styles/`. Their DESIGN.extended.md, design-system.json, and media files provide a stable source for later implementation. Live interaction findings supplement those archived summaries; they should take precedence when an archived description omits a detail page or describes an earlier state.
