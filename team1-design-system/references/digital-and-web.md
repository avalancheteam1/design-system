# Digital and web

The conventions here are the current frontend profile (3.0.0, decisions approved by Giacomo Barbieri on 2026-11-20). They are implementation rules for websites, web apps and product UI, not universal print, social or presentation tokens. Machine-readable values live in `tokens/design-tokens.json` under `web`; `scripts/build_tokens.py` generates `tokens/design-tokens.css` and the Tailwind 4 theme `tokens/tailwind-theme.css`. Reference React components (shadcn-compatible) live in `components/`, with `registry.json` for the shadcn CLI. See [web core and site migration](web-core-and-migration.md) for what each Team1 site must change.

## Foundation

- Dark is the default theme. Light is an explicit option set with `data-theme="light"` (or the `.light` class) on `<html>`. The operating-system preference is only a fallback when the visitor or site has made no explicit choice. A site that must always open dark sets `data-theme="dark"`.
- Dark: background `#000000`, surface `#161617`, raised surface `#1A1B1C`, hover surface `#2A2B2C`. Neutral steps only; do not tint dark surfaces violet, blue or zinc.
- Dark text roles: headings `#FFFFFF`, body `#E5E7EB`, muted `#9CA3AF`.
- Light: background `#FFFFFF`, surface `#F5F5F9`, hover surface `#E8E9EC`; headings `#161617`, body `#3F3F46`, muted `#5F6670` (replaces 2.x `#6C757D`, which failed AA on `#F5F5F9`).
- Borders are translucent so they sit correctly on every surface: dark `rgba(255,255,255,0.08)` hairline and `0.16` strong; light `rgba(22,22,23,0.10)` and `0.20`. Form-field borders use the stronger `inputBorder` role (`0.38` dark, `0.50` light) so the field boundary meets 3:1.
- **Red is the only accent.** Ava Red `#E6212F` is for primary actions, brand emphasis, selection and the card glow. Do not introduce blue, purple, green, yellow or Discord-coloured accents into UI chrome, buttons, links or highlights. The 50–950 red scale (`--team1-red-*`) supplies hover, pressed and tint steps.
- Red text uses the AA-safe text role, not raw Ava Red: `#EC5A64` on dark (6.2:1 on black, 5.4:1 on `#161617`) and `#D11725` on light (5.4:1 on white, 5.0:1 on `#F5F5F9`). Never assume red text on a dark surface passes contrast merely because both colors are approved. Do not put red text on the hover surface; use the heading colour there.
- Status colours are functional, minimal and never decorative: error `#DC2626` (distinct from brand red; brand red never signals an error), success `#16A34A`, warning `#F59E0B`. Text versions are tuned per theme (`textError`, `textSuccess`, `textWarning`). Information messages are neutral (no blue). `#2563EB` and `#9333EA` remain in the token file for data visualisation only.
- The official brand accents Ava Blue `#3055B3` and Secondary Blue `#058AFF` remain identity colours for the blog profile, approved merchandise and data visualisation. They are not web UI accents and not substitutes for semantic status colors.

Use the complete spacing scale—2, 4, 6, 8, 12, 14, 16, 20, 24, 32, 40, 48, 64, and 80 px—rather than inventing near-duplicates. Use z-index levels 0 through 90 in steps of 10 and the packaged motion tokens. Build mobile-first at 640, 768, 1024, 1280, and 1536 px; cap the main container at 1280 px with 24 px desktop and 16 px mobile padding.

### Radius

Three steps plus one justified small step:

| Token | Value | Use |
|---|---:|---|
| `full` | 9999 px | Buttons, badges, tabs, switches, avatars, chips |
| `sm` | 12 px | Inputs, selects, textareas, menus, popovers, tooltips, alerts, media inside cards |
| `lg` | 20 px | Cards, dialogs, sheets, table frames |
| `xs` | 6 px | Checkboxes, inline code/kbd, items nested inside a 12 px menu (a 12 px item inside a 12 px menu looks unnested) |

The 2.x radii 4, 8, 10 and 16 px are retired for web. Do not add new radius values.

## Typography

- Headings and display: **Kanit Medium 500**, tight leading (≈1.15, display down to 1.0) and slight negative tracking.
- Body and UI: **Inter**. Long-form reading text at 16 px and above uses **Inter Light 300** at 1.6 line height. Interface text at 14 px and below (labels, inputs, buttons, tables, navigation, captions) uses **Inter Regular 400**; Inter Medium 500 for emphasis in UI (button labels, active nav, table headers).
- Metadata, code, dates, IDs and kickers: **JetBrains Mono** 400 at 12 px with light positive tracking.
- Aeonik is not used in web or product UI from 3.0.0. It remains a controlled alternative for video captions, chapter marks and approved print (see the relevant modules).
- Kanit Light 300 remains the body face for print, social graphics and documents (see [identity](identity.md)). Decks keep the template's Inter rules (see [presentations](presentations.md)).
- Do not substitute a decorative display face for UI copy. Load fonts from an authorized source (Google Fonts or self-hosted files you are licensed to serve); this package ships no font binaries.

## Identity mapping

An implementation handoff must map authentic indexed files to every live context: a dark-background wordmark, light-background wordmark, approved monochrome fallback, compact symbol, square app/social icon, PFP, and the complete favicon set. Do not derive one variant from another. In a theme-switching site, render both authentic wordmark files and show the one that matches the active theme (the `Logo` component does this); never recolor one file with CSS filters. Keep `Team1` at sentence starts, in titles, and in proper-name treatments; `team1` is acceptable in flowing copy; never write `TEAM1`.

## Components and interaction

- Use real buttons for actions and links for navigation. Provide hover, active, focus, disabled, loading, validation, empty, and error states.
- **Buttons are pills.** Variants: primary (solid red, white label), secondary (outline), ghost, destructive (error-tinted, never the brand red) and link. Heights 36, 44 (default) and 52 px.
- **Primary button states:** hover scales to 1.03 with a red glow (`shadowButtonHover`); pressed scales to 0.98 and drops the glow; disabled is 40 % opacity with no pointer events; loading shows a spinner, sets `aria-busy` and blocks repeat submission.
- **Reduced motion:** under `prefers-reduced-motion: reduce` there is no scale or lift. Hover steps the fill to red 600 `#D11725` and pressed to red 700 `#B0141F`.
- **Focus:** every interactive control shows a 2 px solid outline at 2 px offset, white `#FFFFFF` on dark and `#161617` on light, on `:focus-visible`. Never remove the browser outline without this replacement. The 2.x `0 0 0 3px rgba(230,33,47,0.1)` ring is retired because it is invisible on black.
- **Cards:** the glow card is the default: surface fill, hairline border and a soft red glow (`0 4px 24px rgba(230,33,47,0.15)` on dark); interactive cards strengthen the glow, tint the border red and lift 2 px on hover. Use the **quiet** card (no glow, hover changes the fill) for dense lists, tables of projects, nested cards and anything repeated more than about six times on a screen. One glow level per surface; never nest glow cards.
- **Icons:** use Lucide (`lucide-react` or the Lucide SVG set) only, at 16 px in controls and 20–24 px standalone, 1.5–2 px stroke, inheriting `currentColor`. Do not mix Heroicons, Phosphor, react-icons or emoji as UI icons. Brand and social logos come from authentic files, not icon fonts.
- Keep pointer targets at least 44 × 44 px with at least 8 px separation where practical.
- Standard transitions are 150, 200, and 300 ms. Entrance motion may use 400 ms `cubic-bezier(0.16, 1, 0.3, 1)` with a 20 px fade-up and 80 ms stagger.
- Honor `prefers-reduced-motion`; remove non-essential movement rather than merely speeding it up.
- Use current favicons and social preview assets. Keep logo files intrinsic and unmodified.

## Core and extension layer

Every Team1 web property, including chapter and campaign sites, uses the shared core. A site may add an expressive layer on top. The full locked/extendable table and the per-site migration notes are in [web core and site migration](web-core-and-migration.md).

## Accessibility

- Use semantic headings, landmarks, lists, labels, and controls with a logical reading and tab order. Every icon-only control and link needs an accessible name.
- Supply useful alt text for informative images and empty alt text for decoration. Captions and transcripts are required where the medium needs them.
- Test contrast for the actual size, weight, state, and background. In particular, never assume red text on a dark surface passes merely because both colors are approved. Brand approval does not imply accessible contrast. `tokens/CONTRAST.md` (generated by `scripts/contrast_audit.py`) lists every token text/background pair; all body pairs pass AA.
- Do not communicate status through color alone. Pair status colour with an icon and text, associate errors with their fields and expose status changes to assistive technology.
- Test keyboard-only use, zoom/reflow, small screens, slow/loading states, and a screen reader before launch.
- Run responsive QA on the deployed candidate in supported real desktop and mobile browsers/devices; viewport emulation is useful but does not replace at least one physical mobile-device check.

## Project and launch governance

Before implementation, obtain project approval and name the content, design, technical, and operational owners. Team1 web properties should use the approved Team1 network domain pattern, shared navigation/header, responsive behavior, current favicon set, SEO metadata, and a 1200 × 630 px Open Graph image.

The launch path is: content walkthrough → design review → Team1 review skill when available → automated/source checks → final code review → go-live approval. Record the repository, deployment owner, analytics choice, data collection, and privacy implications. Never expose private operations data, internal contacts, credentials, or unapproved tracking in a public artifact.
