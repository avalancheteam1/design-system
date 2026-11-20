# Identity

## Core palette

| Role | Value | Use |
|---|---:|---|
| Ava Red | `#E6212F` | Primary brand accent and action; the only accent in web UI |
| Ava Blue | `#3055B3` | Identity blue: blog profile, approved merchandise, data visualisation. Not a web UI accent |
| Secondary Blue | `#058AFF` | Identity blue for data visualisation and approved campaign art. Not a web UI accent |
| Dark Gray | `#161617` | Dark surface |
| Light Gray | `#F5F5F9` | Light surface |
| Black | `#000000` | Dark canvas |
| White | `#FFFFFF` | Light canvas and high-contrast type |

`#FF394A` is retired. `#E84142` belongs to Avalanche-origin or inherited presentation use, not the current Team1 primary palette; Team1 web properties replace it with `#E6212F`. Use semantic error red `#DC2626` for failures so brand red never signals an error state.

From 3.0.0 the red has a 50–950 tint scale (Ava Red is step 500) for hover, pressed and tint states, and an AA-safe red for text: `#EC5A64` on dark surfaces and `#D11725` on light ones. Ava Red itself stays the fill colour; at body-text size it does not reach 4.5:1 on `#161617`. The 2.x hover `#E02D3D` is retired because it is indistinguishable from Ava Red.

## Marks

Use only files listed as current in `assets/asset-index.json`.

- Choose the approved wordmark for explicit host identification and the symbol for compact, already-contextual placements.
- Use the red-symbol/white-wordmark variant on dark backgrounds and the red-symbol/black-wordmark variant on light backgrounds. Use approved one-color alternatives only in their documented contexts.
- Never redraw, typeset, recolor, crop, distort, rotate, outline, blur, add glow or shadow, change opacity, or assemble a homemade lockup.
- Preserve the source aspect ratio and transparent padding. Maintain the guide's X-based minimum clear space around every mark.
- The emblem/logotype always uses a lowercase `t`.

Team1 is the host identity in Team1-led work. Keep Avalanche endorsement and partner marks separate unless an approved lockup exists. Size partner and sponsor marks for approximately equal **perceived** weight and use balanced spacing; identical bounding boxes do not guarantee parity.

## Naming

- `Team1` is valid at a sentence start, in a title, or as a proper-name treatment.
- `team1` is acceptable in flowing copy.
- Never use `TEAM1`.
- Do not translate, respell, or rebuild the name inside a logo.

## Typography

Typography is set per medium. Kanit Medium 500 is the heading face everywhere except inside the inherited presentation master.

| Medium | Headings | Body | Other |
|---|---|---|---|
| Web and product UI (3.0.0) | Kanit Medium 500 | Inter: Light 300 for long-form text (16 px and above), Regular 400 for UI text (14 px and below) | JetBrains Mono 400 for metadata and code. No Aeonik. See [digital and web](digital-and-web.md). |
| Print, social graphics, documents, merchandise | Kanit Medium 500 | Kanit Light 300 | Aeonik Regular or Medium, sparingly, where licensed |
| Video | Kanit for headlines | Aeonik captions | See [photography and video](photography-and-video.md) |
| Presentations | The current master's inherited Inter rules | Inherited | Unchanged in 3.0.0. See [presentations](presentations.md). |

Do not bundle or redistribute fonts without their license. Verify installed fonts, script coverage, line breaks, and the exported render. Medium exceptions are documented in the corresponding reference; do not carry one medium's typography into another.

## Composition

Prefer clean hierarchy, generous spacing, one dominant message, and strong real imagery. Use red as a signal rather than a field of continuous decoration. Preserve contrast and keep text away from busy imagery. Avoid generic crypto tropes, invented UI, coins, neon chains, synthetic crowds, and effects applied merely to make an artifact feel “technical.”

## Approved merchandise treatments

For an explicitly approved merchandise campaign, see [campaign composition](merch-campaigns.md) for heavy lettering, solid red fields and local accents. These scoped treatments do not change the global font/color tokens or permit altered marks.
