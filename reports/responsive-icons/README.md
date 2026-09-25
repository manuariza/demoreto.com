# Responsive icon correction

Replaced platform-dependent Unicode arrows, menu and play symbols with inline SVG icons using currentColor. Icons are decorative (aria-hidden, non-focusable); link and button labels remain accessible. Removed two decorative emoji from displayed Instagram text; original source records remain intact.

Fixed the portrait's intrinsic minimum width causing a 20px horizontal overflow at the iPad landscape breakpoint. Preserved the existing editorial design, colors, type, artwork selection and portrait.

63 route/viewport checks passed: home, artwork catalog, restoration catalog, Sunset 3, Florero, contact and studio at widths 320, 375, 390, 412, 430, 768, 820, 1180 and 1440. Screenshots cover small phones, iPhone/Android-size screens, iPad portrait/landscape and desktop. Menu open/close verified on phone widths. No horizontal overflow, target Unicode symbols or JavaScript errors remained. Static text audit covered all 274 production and preview pages.

Testing uses isolated Chromium responsive emulation, not physical iOS/Android hardware or Safari/WebKit. SVG rendering removes reliance on platform emoji fonts. See checks.json and screenshots.

The build now reuses committed artwork metadata and derivatives if the external original-art folder is absent, so routine site updates remain reproducible.
