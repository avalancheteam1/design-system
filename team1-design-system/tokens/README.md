# Design tokens

`design-tokens.json` is canonical. `design-tokens.css` is a convenience export for global web foundations.

The CSS export includes the complete spacing, radius, z-index, responsive, typography, status, focus, shadow, hover, and motion foundations. Breakpoint custom properties are documentation values for use inside media-query authoring; CSS custom properties cannot themselves be used as media-query conditions in standard CSS.

The source guide names Ava Red as “primary text” for headings/emphasis in both themes. Tokens keep that exact role as `textBrand` and separately name `textHighContrast` for readable white/dark copy. The high-contrast name is a derived accessibility semantic, not a replacement brand color; test the actual text size, weight, and background before release.

Use `global` for new work. Values under `profiles` are controlled exceptions and must stay within the named medium. In particular, the current presentation master contains inherited type and red values that are not global Team1 tokens.

The `retired` map exists for migration and linting. Never treat its values as a usable palette. Status error is `#dc2626`; do not use brand red `#E6212F` as an error color.

`profiles.eventDisplay.headlineLineHeight` is a derived 0.90 starting point for short stacked Kanit Medium event headlines. Multiply font size by this value for manual baseline placement. It is deliberately excluded from the global CSS foundations; it does not govern body copy or inherited presentation layouts. See the [social guidance](../references/social-and-content.md#event-headline-leading--derived-recommendation) for scope and optical checks.

`profiles.imageTitleSangeeth` records the designer's Kanit Semibold 600, 0.77 line height and `-0.04em` tracking for titles inside images. Use it only when adopting that compact image-title treatment, then inspect the final render. It overrides the 0.90 event-display starting point in that scope and is excluded from the global CSS export. See the [image-title guidance](../references/social-and-content.md#kanit-titles-inside-images--designer-treatment).

No font files are included. Verify font licenses, installed weights, target-language glyph coverage, fallback behavior, contrast, zoom, and reduced-motion behavior in the final medium.
