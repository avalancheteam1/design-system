# Team1 web components (3.0.0)

React components for Team1 websites and product UI. They follow the shadcn/ui "new-york" API (Radix primitives, `class-variance-authority`, `cn()`), so they drop into a shadcn project, and every value comes from the generated tokens (`../tokens/design-tokens.css`, `../tokens/tailwind-theme.css`). Rules and rationale: [digital and web](../references/digital-and-web.md).

| Component | File | Notes |
|---|---|---|
| Button | `ui/button.tsx` | Pill. `variant`: primary (default), secondary, ghost, destructive, link. `size`: sm 36, default 44, lg 52, icon, icon-sm. `loading` shows a spinner and sets `aria-busy`. Hover 1.03 + glow, pressed 0.98, colour steps under reduced motion. |
| Input, Textarea, Label | `ui/input.tsx`, `ui/textarea.tsx`, `ui/label.tsx` | 12 px radius, 3:1 border, `aria-invalid` error state. |
| Select | `ui/select.tsx` | Radix Select; 12 px trigger and menu, 6 px items. |
| Checkbox, Switch | `ui/checkbox.tsx`, `ui/switch.tsx` | Red when on. |
| Badge | `ui/badge.tsx` | Pill. brand, solid, neutral, outline, success, warning, error. |
| Card | `ui/card.tsx` | `variant="glow"` (default) or `"quiet"` for dense lists; `interactive` adds hover. Header, Title, Description, Action, Media, Content, Footer. |
| Tabs, Dialog, Tooltip, Table, Alert | `ui/*.tsx` | Alert variants: info (neutral), success, warning, error. |
| Logo, SiteHeader, SiteFooter, ThemeToggle | `layout/*.tsx` | `Logo` takes the authentic dark- and light-background wordmark files and swaps them by theme; it never recolors a file. |

`lib/utils.ts` exports `cn()` with a tailwind-merge configuration that knows the Team1 radius and shadow names. `lib/theme.ts` reads and sets the theme (`data-theme` on `<html>`, stored under `team1-theme`) and exports `themeBootScript` for `<head>`.

Imports use the `@/` alias for this package folder (`@/components`, `@/lib/utils`), as in a shadcn project. Install them with the shadcn CLI from the built registry (`npm run registry:build` at the repository root; see `../registry.json`) or copy the files. Icons are Lucide only.

The red scale, translucent borders and component structure derive from the public `avalancheteam1/ecosystem-hub` repository, which is distributed under the BSD 3-Clause License, Copyright (c) 2026, Avalanche Team1. shadcn/ui is MIT licensed.
