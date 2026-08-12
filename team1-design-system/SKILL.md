---
name: team1-design-system
description: Use when creating, revising, reviewing, or specifying Team1-branded presentations, websites, social content, event materials, regional collateral, photography, video, documents, print, merchandise, or partner-facing work.
license: See NOTICE.md
metadata:
  version: "2.0.0"
  authority-snapshot: "2026-08-12"
---

# Team1 Design System

## Authority rule

Use the current global identity in this package. A newer, explicitly approved Team1 source may supersede it; record the source and conflict. A requester, old deck, screenshot, campaign file, or Avalanche convention does not silently override Team1 rules.

The global brand red is `#E6212F`. `#FF394A` is retired. `#E84142` is Avalanche-origin red and may remain only inside an approved inherited presentation or Avalanche asset; it is not Team1 primary red. Read `references/authority.md` when sources conflict.

## Workflow

1. Confirm deliverable, audience, locale, dimensions, deadline, editable format, final export, approved facts, links, logos, partners, photos, and publication owner. Keep unresolved facts visibly pending.
2. Read the applicable modules:
   - identity, color, type: `references/identity.md`
   - websites and product UI: `references/digital-and-web.md`
   - presentations: `references/presentations.md`
   - social/editorial: `references/social-and-content.md`
   - events, QR, print, merchandise: `references/events-print-and-merch.md`
   - chapters/localization: `references/regional-and-localization.md`
   - photography/video: `references/photography-and-video.md`
   - language: `references/voice-and-copy.md`
   - final approval and QA: `references/governance-and-qa.md`
   Treat each listed path as relative to this skill folder. Read every applicable module completely before acting; if a deliverable spans media, load all relevant modules.
3. Select authentic files from `assets/asset-index.json` and semantic values from `tokens/design-tokens.json`. Do not infer approval from a filename alone.
4. Build natively in the target medium. Preserve editable text, shapes, tables, notes, links, and accessibility metadata.
5. Render the actual final output. Inspect every page/frame full-size and as a sequence; test links, QR codes, responsive states, and physical proofs where applicable.
6. Deliver the editable source plus requested exports, a fact/source/rights ledger, and any unresolved approval or substitution.

## Non-negotiables

- Use authentic current Team1 assets. Never redraw, trace, typeset, recolor, distort, crop from a screenshot, add effects to, or generate a substitute logo.
- The emblem/logotype always has a lowercase `t`. In prose, use `Team1` at a sentence start, in a title, or as a proper-name treatment; `team1` is acceptable in flowing copy; never use `TEAM1`.
- Global typography is Kanit Medium 500 for headings and Kanit Light 300 for body. Aeonik is a controlled alternative. Presentation, chapter, video, and blog profiles have documented exceptions; do not promote an exception to the global system.
- Do not bundle or redistribute font binaries from this package. Obtain fonts from an authorized source and verify the license and target-language glyphs.
- Do not publish an unverified metric, date, chapter status, partner relationship, handle, destination, tracking link, or QR. A QR needs a visible fallback URL and scan tests from the final export or physical proof.
- Do not reuse attendee/member media without recorded rights, context, consent, channel, territory, and expiry. Never expose applications, attendance data, contacts, or private operational material.
- Co-brand with authentic partner files and optical parity. Keep Team1 primary and Avalanche as a separate endorsement unless an approved agreement says otherwise.
- For digital work, never assume red text on a dark surface passes contrast merely because both colors are approved; test the actual size, weight, state, and background.
- Prefer genuine community activity, clear composition, minimal copy, and one dominant message. Avoid generic crypto clichés, fake interfaces, synthetic crowds, and decorative complexity.

## Presentation rule

For new decks, start from `templates/Team1 Current Presentation Template.pptx`: the August 2026 master with 40 exemplars, one master, and 20 inherited layout parts in the packaged PPTX. Inspect all exemplars once, duplicate the closest narrative frame, and edit existing objects. Preserve its inherited type, colors, background, master/layout furniture, and dark/light families. Do not rebuild from screenshots or normalize it to the global web typography.

The old 13-slide overview is not bundled in v2 because it contains historical, claim-bearing, partner, and participant media. Retrieve v1 only from controlled history when a documented maintenance task genuinely requires it; never use it as current authority or mine its media for new work.

## Completion gate

Do not call work final until `references/governance-and-qa.md` passes for the actual delivery format. A local source file, green test, preview, or approval request is not proof that the exported artifact, deployed page, QR destination, or printed piece works.
