# Web core and site migration (3.0.0)

This module turns the 3.0.0 web decisions into a shared core for every Team1 web property and records what each live site must change. It complements [digital and web](digital-and-web.md), which states the rules; this module states who has to move and how. The site observations come from a read-only review of the public pages on 2026-11-20 (computed styles, CSS variables, axe-core). Only `ecosystem-hub` has public source, so the notes for other sites name observed values, not file paths.

## Principles

1. **One core, many voices.** Every Team1 site uses the same tokens, type roles, button and card behaviour, focus treatment, icons and accessibility floor. Chapter and campaign sites express their place and moment in an extension layer on top, never by forking the core.
2. **Dark first, light by choice.** Black canvas and neutral greys are the default. Light mode is an explicit, complete theme rather than an afterthought.
3. **Red is the signal.** Ava Red is the only accent: one primary action per view, selection, glow. Everything else is neutral, and status colours appear only to communicate status.
4. **Readable before expressive.** Inter for reading and interface text, Kanit for headings, AA contrast for every body pair, visible keyboard focus, reduced-motion fallbacks.
5. **Tokens, not hex.** Sites consume `design-tokens.css` and `tailwind-theme.css` (or the registry components). A hard-coded brand hex in a site stylesheet is a defect.

## Locked core versus extension layer

| Area | Locked (all sites) | Extendable (chapter and campaign layer) |
|---|---|---|
| Palette | Red scale, neutral dark/light roles, status colours, text roles, focus colour. No other UI accent. | Illustration, hero art, photography grading and section backgrounds may use an approved local palette (for example a chapter flag colour inside artwork), never on buttons, links, focus or status. |
| Typography | Kanit 500 headings, Inter body (300 long-form, 400 UI), JetBrains Mono metadata. | Display sizes and tracking for hero headlines; an approved chapter display treatment inside artwork. No extra UI typefaces. |
| Radius | full / 12 / 20 (+ 6 for nested small parts). | None. Decorative shapes inside illustrations are artwork, not UI radius. |
| Buttons | Pill shape, variants, sizes, hover/pressed/focus/disabled/loading behaviour, reduced-motion fallback. | Label copy and icon choice (Lucide). |
| Cards | Glow default, quiet for dense lists, hover behaviour. | Media, content layout inside the card, card grid density. |
| Icons | Lucide only for UI. | Custom illustrations and authentic partner/social logos. |
| Logo | Authentic files from `assets/asset-index.json`; dark/light swap. | Approved chapter marks from `assets/chapters/` where the chapter gate allows them. |
| Motion | Durations, easing, entrance curve, reduced-motion rules, no motion that hides content. | Scroll-driven scenes, loaders and smooth scrolling, provided content is visible without scrolling or JavaScript, the reduced-motion preference disables them, and keyboard scrolling still works. |
| Layout | 1280 px container, 24/16 px padding, breakpoints, 44 px targets, shared header/footer pattern. | Full-bleed sections and hero composition. |
| Accessibility | AA text contrast, 3:1 field boundaries, visible focus, named links and icon buttons, semantic landmarks. | Nothing; this is a floor. |

A site that needs something outside this table asks the design-system owner for a scoped exception and records it, the same way medium exceptions are recorded in [authority](authority.md).

## Adoption

```css
/* app.css, Tailwind 4 */
@import "tailwindcss";
@import "../team1-design-system/tokens/design-tokens.css"; /* adjust to where the package lives */
@import "../team1-design-system/tokens/tailwind-theme.css";
```

Load Kanit 500, Inter (300/400/500) and JetBrains Mono 400 from an authorized source and expose them under those family names. Add the theme boot script from `lib/theme.ts` (`themeBootScript`) to `<head>` to avoid a flash of the wrong theme. Pull components with the shadcn CLI from the registry built by `npm run registry:build` (configure `"registries": { "@team1": "<registry-url>/{name}.json" }` in `components.json`) or copy them from `components/`. The 2.x variable names still resolve as deprecated aliases until 4.0.0.

## Per-site migration notes

### www.team1.network (marketing)

- Card and focus shadows use the retired `#FF394A`: replace with `--team1-shadow-card` / `shadow-card` and `shadow-card-hover`.
- Body text is Kanit 400 at 14 px: move body to Inter (300 long-form, 400 UI).
- Buttons are already pills; align hover to scale 1.03 + `shadow-button-hover` (currently 1.01) and add the reduced-motion colour steps. Replace the `#e02d3d` hover.
- Focus falls back to the 1 px browser default: apply the 2 px focus outline. Fix the scrollable region that cannot receive focus (axe).
- Card radii 16/24 → 20 (`rounded-lg`).
- Add the light theme (the site is dark-only today) or set `data-theme="dark"` explicitly until light is designed.

### hub.team1.network (Ecosystem Hub, `avalancheteam1/ecosystem-hub`)

- The reference implementation: the red scale, translucent borders, Lucide, shadcn new-york and JetBrains Mono metadata come from here.
- Replace the violet-tinted neutrals `#0b0a0f / #121118 / #181720` with `#000000 / #161617 / #1A1B1C`.
- Buttons are 8 px with weight 400: switch to the registry `Button` (pill, Inter 500 label).
- Card radius 12 → 20; inputs stay 12.
- Body moves from Kanit 300 to Inter 300; keep Kanit 500 headings.
- Entrance curve `cubic-bezier(0.22, 1, 0.36, 1)` → the token curve `cubic-bezier(0.16, 1, 0.3, 1)`.
- The blue hero glow is a second accent: make it red or neutral.
- Focus: replace the 2 px red outline + glow with the white/ink 2 px outline.
- Light theme exists: map its greys to the light roles (`#FFFFFF / #F5F5F9`, muted `#5F6670`).

### cascade.team1.network (Avalanche Cascade)

- Remove purple, green and Discord `#5865F2` CTAs; use primary/secondary buttons. Discord or X links use a secondary button with the authentic logo.
- Replace react-icons (Feather and Font Awesome glyphs) with Lucide.
- Red uppercase kickers fail contrast (5 axe failures): use `text-fg-brand` (`#EC5A64`) or JetBrains Mono `meta` in muted grey.
- Replace the custom `team1-wordmark-white.svg` with the authentic indexed wordmark files.
- Neutrals `#0C0C10 / #060608 / #1A1C1F` → token roles; container 1152 → 1280.
- Buttons 8 px → pill; card radii 10/14 → 20.

### events.team1.network (Team1 Events)

- No visible keyboard focus: apply the focus outline to every control and card link.
- Replace Heroicons-style inline SVGs with Lucide.
- UI labels use Kanit 600 14 px: move to Inter 500; body to Inter.
- Canvas `#0A0A0A` → `#000000`; card radii 10/16 → 20; button 8–10 → pill.
- Its shadcn-style structure (`data-slot`, Radix) makes it the easiest site to move onto the registry components.

### india.team1.network (chapter)

- Zinc greys → token neutrals; footer zinc-500 text fails contrast (axe): use `text-fg-muted`.
- `#F87171` red text → `text-fg-brand`.
- Three social links have no accessible name: add `aria-label`.
- Fix the banner landmark misuse.
- Lenis and the scroll-driven scenes are allowed in the extension layer only if content is visible before scrolling and `prefers-reduced-motion` disables them (content currently stays blank until scrolled).
- Check the custom `team1-horizontal.svg` against `assets/asset-index.json` and the chapter-mark gate in [regional and localization](regional-and-localization.md); replace it if it is not an approved file.
- Headings Kanit 600/700 → 500; body Kanit 400 → Inter; card radii 16/24/32 → 20; container 1400 → 1280.

### turkiye.team1.network (chapter, Vite SPA)

- Headings Kanit 400 → Kanit 500; body Kanit 400 → Inter.
- Replace Heroicons-style icons with Lucide.
- 16 axe region violations: wrap content in landmarks.
- The GSAP intro loader belongs to the extension layer: it must be skippable, must not block content, and must be disabled under reduced motion.
- Buttons 8/12 → pill; replace the `#e02d3d` hover; card radius 16 → 20; container 1152 → 1280.

### seedsprint.team1.network (campaign micro-site)

- `#E84142` → `--team1-red` / `bg-brand`. Primary buttons use dark text `#090909` on red: use the white `text-fg-on-brand` label.
- Hover `#F07575` with `translateY(-2px)` → the token hover (scale 1.03 + glow; colour steps under reduced motion). Focus `#F07575` → the focus outline.
- Radius 4–5 px → pill buttons, 12 px fields, 20 px cards.
- Phosphor and the custom 16 px icons → Lucide.
- Inter body and JetBrains Mono already match; keep them. Uppercase Kanit display headlines can stay as a campaign display treatment in the hero only, at weight 500.
- Container 1520 and the extra 900 px breakpoint → 1280 and the standard breakpoints.

### members.team1.network (Member Portal; only the public login page was reviewed)

- Inter-only: headings move to Kanit 500 (Inter 700 → Kanit 500).
- Remove the yellow `--highlight: #fac800`; use red or neutral emphasis.
- Zinc greys → token neutrals; canvas `#0B0A0F` → `#000000`.
- Buttons 12 px → pill; card radius 16 → 20; container 1600 → 1280.
- The pages behind login were not reviewed; audit them before the migration is called complete.

### Infrastructure tools

go (Sink), lm (listmonk), mon (Uptime Kuma), wal (Plausible) and gt (GlitchTip) run third-party admin UIs and are out of scope. The public go.team1.network page shows the unbranded Sink template; branding it is optional and should use the core if it happens.
