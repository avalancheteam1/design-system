# Event headline leading review

`event-headline-leading-before-after.png` compares the actual square-cover title treatment at the same scale: before above the red divider, revised below it. It contains only rendered Kanit text and a comparison divider; no font programs, event photograph or third-party logo is embedded.

Requester feedback on 21 September 2026 asked for a slight reduction in line height. At 132 px type, the baseline interval changes from 138 px (about 1.05) to 118.8 px (0.90). The story uses the same derived token: 103 px type × 0.90 = 92.7 px, down from 108 px. The subtitle follows the second line, retaining its existing offset.

Both final PNG exports (1600 × 1600 and 1080 × 1920) were visually inspected after rendering from the actual Kanit Medium/Light outlines. Text is unclipped, lines do not collide, and the original art, logo and public copy are unchanged. The full event artwork remains in the event workspace; this repository carries only the typography proof.

This is scoped event-cover guidance, not an official global typography change. No release version or tag is changed.

## 2.2.0 image-title proof

`kanit-image-title-2.2-comparison.png` compares the same two-line phrase in Kanit Semibold at 112 px. The left panel uses 90% line height and default tracking; the right uses Sangeeth's 77% line height and −4% tracking. The right panel was inspected at its 1600 × 660 px export size: neither line is clipped, the lines do not collide, and the text remains readable. This proof tests the documented title treatment, not a universal safe setting for every word, script, editor, or crop. Final artwork still needs its own visual check.

The proof was rendered using a temporary Kanit Semibold file from the Google Fonts `ofl/kanit` source; no font binary is committed or included in the portable package.

## 3.0.0 web design system preview

`v3/` holds screenshots of the 3.0.0 preview (`team1-design-system/preview`), captured with Playwright (Chromium) at 1440 px from the production build on 20 November 2026:

- `preview-dark-1440.png` and `preview-light-1440.png`: every token and component in both themes. States in the button, form, card and tab specimens are pinned with a preview-only `data-preview-state` attribute so all of them are visible at once.
- `contact-button-states.png`: the primary button in real browser states (mouse hover, mouse down, keyboard Tab focus, disabled, loading) in dark, light and dark with `prefers-reduced-motion: reduce`. Under reduced motion the button does not scale; hover and pressed step to red 600 and red 700.
- `contact-cards.png`: glow and quiet cards at rest and under real hover in the same three modes.
- `dialog-dark-1440.png`, `select-open-light-1440.png`: open overlay states.
- `preview-dark-390.png`: the page at 390 px (2×). The document does not scroll horizontally at 390 px; only the button-state matrix scrolls inside its own container.

Each image was inspected for overflow, clipped text, focus visibility and glow strength before release. The fonts were loaded from development-only npm packages; no font binary is committed. Contrast figures are in `team1-design-system/tokens/CONTRAST.md`.
