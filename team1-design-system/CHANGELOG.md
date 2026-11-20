# Changelog

## 3.0.0 — 2026-11-20

Major release. Adds the Team1 web and product design system on top of the brand book: one token source that generates CSS variables and a Tailwind 4 theme, shadcn-compatible React components, a shadcn registry, a visual preview and a contrast audit. The web rules follow Giacomo Barbieri's decisions of 2026-11-20 (Q1–Q13), taken after a review of the live Team1 sites. Presentation templates, identity assets, chapter vectors and the print/social/video rules are unchanged unless listed below.

### Breaking changes

- **Web typography:** body and UI text on websites and product UI move from Kanit Light to **Inter** (Light 300 for long-form text at 16 px and above, Regular 400 for UI text at 14 px and below). Headings stay Kanit Medium 500. JetBrains Mono is added for metadata and code. `--team1-font-body` now resolves to Inter. Print, social and document body text stays Kanit Light 300; decks keep their inherited Inter rules.
- **Radius scale:** web radii are now `full` 9999 px, `sm` 12 px and `lg` 20 px, plus `xs` 6 px for nested small parts. The 2.x radii 4, 8, 10 and 16 px (`label`, `control`, `large`, `projectLogo`) are retired. Cards move from 12 to 20 px. The `global.radius` group is removed from the tokens; use `web.radius`.
- **Button shape:** all buttons are pills (2.x used 8 px controls).
- **Hover, pressed and focus states:** primary hover is scale 1.03 + red glow, pressed is scale 0.98, disabled is 40 % opacity. With `prefers-reduced-motion: reduce`, hover and pressed become colour steps (red 600 / red 700) with no scale. Focus is a 2 px solid outline at 2 px offset (white on dark, `#161617` on light). `--team1-focus-ring` is now a colour, not a box-shadow.
- **Retired reds:** `#E84142` must be replaced with `#E6212F` on Team1 web properties (it stays valid only inside the inherited presentation master). `#FF394A` remains retired, including in glow shadows. The 2.x hover `#E02D3D` is retired.
- **Red text roles:** `global.color.dark.textBrand` changes from `#E6212F` to `#EC5A64` and `global.color.light.textBrand` from `#E6212F` to `#D11725`, so red text passes AA 4.5:1 on black, `#161617` and the light surfaces.
- **Red is the only UI accent:** Ava Blue, Secondary Blue, info blue and featured purple are no longer web UI colours (they remain identity/data-visualisation tokens). Information alerts are neutral.
- **Aeonik** is no longer a web or product typeface. It stays a controlled alternative for video captions, chapter marks and approved print.
- **Theme selection:** dark remains the default. `data-theme="light|dark"` (or `.light`/`.dark`) is the explicit switch; the OS `prefers-color-scheme: light` applies only when no explicit choice exists.

### Added

- `web` token group in `tokens/design-tokens.json` (W3C DTCG format): Inter/Kanit/JetBrains Mono roles and weights, radius, full dark and light theme roles (surfaces, translucent borders, input border, text roles, status text, focus, shadows), focus, button/card state and control-height tokens.
- Red 50–950 scale (`global.color.brand.scale`, Ava Red = 500).
- `scripts/build_tokens.py` (standard library) generating `tokens/design-tokens.css` and the new `tokens/tailwind-theme.css` (Tailwind 4 `@theme` with reset namespaces, `@theme inline` runtime roles, `theme-light` variant, `container-page`/`meta`/`focus-ring` utilities, base typography and focus). `--check` fails when generated files are stale.
- shadcn-compatible CSS aliases (`--background`, `--primary`, `--ring`, `--radius` …) so existing shadcn components pick up Team1 values.
- React components in `components/` (shadcn new-york API, Radix, `class-variance-authority`, Lucide): Button (primary, secondary, ghost, destructive, link; sm/default/lg/icon; loading), Input, Textarea, Label, Select, Checkbox, Switch, Badge, Card (glow and quiet, interactive), Tabs, Dialog, Tooltip, Table, Alert, plus Logo, SiteHeader, SiteFooter and ThemeToggle; `lib/utils.ts` and `lib/theme.ts`.
- `registry.json` for the shadcn CLI (`npm run registry:build`).
- `preview/`: a Vite preview of every token and component in both themes and all states, used for the QA screenshots in `docs/qa/v3/`.
- `scripts/contrast_audit.py` and the generated `tokens/CONTRAST.md` covering every token text/background pair and the 3:1 field-boundary and focus checks.
- `references/web-core-and-migration.md`: principles, the locked core versus the chapter/campaign extension layer, and per-site migration notes for www, hub, cascade, events, india, turkiye, seedsprint and members.
- Root `package.json`, `package-lock.json` and `tsconfig.json` for the optional Node tooling (typecheck, preview, registry). The portable skill still needs no network or Node to be used.
- Deprecated aliases for every 2.x CSS variable name, mapped onto 3.0.0 values, scheduled for removal in 4.0.0.

### Changed

- `references/digital-and-web.md` rewritten for 3.0.0: theme roles, red-only accent, red text roles, radius table, typography, button and card states, focus, Lucide icons, reduced motion, contrast audit.
- `references/identity.md`: typography is stated per medium; Ava Blue and Secondary Blue are identity colours, not web UI accents; red scale and red text roles documented.
- `references/authority.md` and `references/source-provenance.md`: the 2026-11-20 decision record is recorded as a newer, explicitly approved source for web and product UI.
- `references/governance-and-qa.md`: web brand-review and state/contrast checks.
- `references/voice-and-copy.md`: interface label, destructive action and error-message copy.
- `references/regional-and-localization.md`: chapter websites use the shared web core.
- `references/presentations.md`, `references/merch-campaigns.md`, `references/compatibility.md`: scope notes so the web changes are not carried into decks or print.
- Light muted text `#6C757D` → `#5F6670` (2.x value was 4.31:1 on `#F5F5F9`).
- `SKILL.md`, `README.md`, `NOTICE.md`, `tokens/README.md`, `manifest.json`, the root README, CONTRIBUTING and the tests updated for 3.0.0.

### Removed

- `global.radius` token group and the `projectLogo` 16 px radius (aliases remain in CSS until 4.0.0).
- `#E02D3D` brand hover and the `0 0 0 3px rgba(230,33,47,0.1)` focus ring.
- Aeonik from the web font roles.

### Fixed

- Primary hover was invisible: `#E02D3D` and `#E6212F` have the same luminance against white (4.55 vs 4.54).
- Keyboard focus was invisible on black with the 2.x 10 % red ring.
- Red text on `#161617` failed AA (3.98:1); the new text roles pass (5.35:1 dark, 5.0:1 light on `#F5F5F9`).
- Light tertiary text failed AA on `#F5F5F9`.

### Migration

1. Import the generated CSS after Tailwind: `@import "tailwindcss"; @import ".../tokens/design-tokens.css"; @import ".../tokens/tailwind-theme.css";`. Off-system Tailwind palette, radius and shadow utilities stop existing, which surfaces hard-coded values.
2. Load Kanit 500, Inter 300/400/500 and JetBrains Mono 400 from an authorized source. Switch body and UI text to Inter (`font-sans`); keep Kanit for headings.
3. Replace `#E84142`, `#FF394A` and `#E02D3D` with tokens (`bg-brand`, `shadow-card`, the button state tokens). Use `text-fg-brand` for red text.
4. Move buttons to pills, inputs/menus to 12 px, cards/dialogs to 20 px. Replace 4/8/10/16 px radii.
5. Replace focus styles with the 2 px outline (`focus-visible:outline-focus-ring` or the base layer), and add the reduced-motion fallbacks.
6. Remove non-red UI accents (blue, purple, green, yellow, Discord) and non-Lucide icon sets.
7. Set `data-theme` explicitly if the site must ignore the OS preference.
8. The 2.x variable names keep working as deprecated aliases; plan to rename before 4.0.0. Site-by-site notes are in `references/web-core-and-migration.md`.

## 2.2.0 — 2026-09-29

- Added the derived 0.90 headline-leading starting point for Kanit Medium event covers and social graphics, with manual-baseline examples and optical checks.
- Recorded Sangeeth's compact Kanit image-title treatment: Semibold 600, 77% line height and −4% tracking, with a separate scoped token and Figma/Illustrator export checks. It is not a global heading rule or an exact claim about Cem's files.
- Kept body copy, global font roles, identity assets and inherited templates unchanged.

## 2.1.0 — 2026-09-08

- Added derived merchandise campaign guidance from the owner-approved ETHRome sticker set and Blockchain Beach production designs.
- Distinguished typography-led stickers from illustration-led wearables; relative revision percentages are not universal layout tokens.
- Documented compact heavy campaign lettering, flat vector illustration, scoped local palettes, authentic event marks, and varied sticker silhouettes.
- Added final-source precedence and separate artwork, substrate preview, cut-guide, and vendor-preflight checks.
- Preserved all global identity assets, core tokens, and presentation templates; no partner/campaign assets or fonts added to the release.

## 2.0.0 — 2026-08-12

- Rebased global identity on the current 2026 Team1 source of truth: Ava Red `#E6212F`, Kanit Medium/Light, current wordmark/symbol/favicons, and corrected naming rules.
- Retired `#FF394A`; limited `#E84142` to Avalanche and inherited presentation contexts.
- Added current dark/light, status, spacing, type, responsive, accessibility, and motion tokens with scoped presentation, chapter, video, and blog exceptions.
- Replaced the old presentation authority with the August 2026 40-exemplar master; kept the 13-frame overview only in controlled v1 history because its contextual media is not broadly reusable.
- Added current chapter SVGs, regional/localization, co-branding, QR, event, print, merchandise, photography, video, social, web, voice, governance, and rights workflows.
- Removed participant photography, historical metrics/chapters, stale logos, campaign graphics, and other rights-unclear or time-sensitive payloads from the current asset bundle.
- Kept the former 13-frame overview and people-bearing photography previews out of v2; they remain controlled historical evidence, not reusable payloads.
- Rebuilt the current 40-page presentation reference as an image-only PDF so no font programs are redistributed.
- Added a sanitized shared-Drive source audit, stronger validation, clean-room agent evaluations, and release QA.
- Expanded the portable CSS export to match the canonical spacing, radius, z-index, breakpoint, typography, and motion foundations.

## 1.0.0 — 2026-08-12

- Initial portable skill derived from `Team1 Overview.pptx`.
