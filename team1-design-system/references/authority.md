# Authority and precedence

This package records the Team1 design system as reviewed on **2026-08-12**, with the web and product UI rules updated on **2026-11-20** (3.0.0). It is a portable working copy, not a replacement for the organizational sources below.

## Source order

0. For websites and product UI only: the 3.0.0 web decision record approved by Giacomo Barbieri on 2026-11-20 (see `source-provenance.md` and `digital-and-web.md`). It is newer than `common` and explicitly approved, so it supersedes `common`'s frontend guidance where they differ, until `common` is updated to match.
1. The private `avalancheteam1/common` repository at commit `9d1b3d1a9d9e3e254149885605504c6dfd84ec54` is the global machine-readable source of truth. Its `brand/brand_guide.md`, formal branding PDF, approved assets, frontend guidance, and review skill govern identity and digital implementation.
2. The June 2026 formal branding guide governs visual constructions that are more specific than the machine-readable guide, including chapters, video, blog, partner parity, and logo clear space.
3. Current medium owners govern their medium: the August 3, 2026 presentation master; the July 18, 2026 photography guide; and the July 30, 2026 event process.
4. Current master/edit-source folders outrank published examples. Published examples outrank migration material. Archive, `_OLD`, historical QR codes, and superseded packages are evidence only.

When rules differ, apply the most specific current rule only inside its stated medium. Do not promote a presentation, blog, chapter, video, campaign, or frontend exception into the global system.

## Global facts versus scoped exceptions

- Global brand red is Ava Red `#E6212F`.
- `#FF394A` is retired. It must not appear as a current Team1 primary color.
- `#E84142` is an Avalanche-origin red and remains in inherited presentation furniture. It is not a global Team1 token.
- Kanit Medium for headings is the global typography baseline. Body type is set per medium: Kanit Light for print, social and documents; Inter (Light 300 long-form, Regular 400 UI) for websites and product UI from 3.0.0; the inherited Inter of the presentation master for decks. Aeonik is secondary and not used on the web. Aeonik Black and Neuropol X are allowed only where the relevant medium rule calls for them.
- On Team1 web properties red is the only UI accent; `#E84142` is replaced by `#E6212F`, and red text uses the AA-safe text roles.
- `Team1` is allowed; `team1` is acceptable in flowing copy. Never write `TEAM1`. Every emblem composition retains the approved lowercase `t`.

## Decision rule

Before producing an artifact, record its medium, audience, locale, source master, required approvals, and evidence date. If an asset, claim, partner relationship, destination, or exception cannot be traced to a current approved source, keep it as a labeled placeholder or request approval. Never infer current authority from frequent historical use.

## Drift control

At each release, compare this package with the current `common` default branch and the current medium masters. Record the reviewed commit and date in `source-provenance.md`. A newer authoritative source supersedes this snapshot; update the package before presenting the new rule as current.
