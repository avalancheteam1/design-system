# Team1 source audit — 2026-08-12

## Purpose and handling

This report records the source review used to define the Team1 design-system v2 authority model. The shared-drive review was read-only. This document is intentionally sanitized: it contains no member names, personal data, shared-drive identifiers, or private operational records.

## Completed scope

| Scope | Records observed | Traversal evidence |
|---|---:|---|
| Marketing, Social Media, and Presentation Materials | 1,608 child records: 1,400 files and 208 folder records | 211 folders listed; 0 listing failures |
| Regions and Events | 203 items: 173 files and 30 folders | 0 scoped listing failures; 41 probable duplicate pairs identified |
| Operations, AI Skills, Tech, and Archive | 201 items: 142 files and 59 child folders | 63 folders scanned including scope roots; 0 listing failures |

These figures describe scoped observations, not a unique global file count. The three rows sum to 2,012 observations, but shortcut targets and mirrored material cross scope boundaries. Probable duplicates were retained in the audit evidence so provenance was not lost. A naive sum must not be presented as the number of unique Team1 assets.

The review covered current guidance, templates, identity files, web and technical governance, presentation exemplars, photography guidance, social and marketing production material, event and regional collateral, and archived or migration-era references. Bulk event media and operational records were classified for relevance and risk rather than copied into this package.

## Authority hierarchy

When sources disagree, use this order:

1. **Current global brand source of truth.** The Team1 common repository and its brand guide, pinned for this audit at commit `9d1b3d1a9d9e3e254149885605504c6dfd84ec54`, govern global identity, naming, color, typography, official assets, accessibility, and reusable digital tokens.
2. **Current medium-specific governance.** Approved technical, photography, social, print, video, event, and localization guidance may add medium-specific rules without redefining the global identity.
3. **Current production master for the medium.** For presentations, the August 3 master is the production source: 40 exemplar slides, one master, and 20 inherited layout parts in the sanitized packaged PPTX. Its inherited typography, objects, and presentation furniture must be preserved.
4. **Current approved production assets.** Campaign, regional, partner, photo, QR, and print files may be used only for their verified context, rights, relationship, destination, and approval state.
5. **Historical, archive, migration, and prior-package material.** These sources can explain provenance or supply a clearly labelled legacy reference. They do not override current rules.

### Resolved source conflicts

- The global Team1 brand red is `#E6212F`. `#E84142` is Avalanche-origin red and `#FF394A` is retired; neither is the current Team1 primary red.
- Global headings use Kanit Medium 500 and body copy uses Kanit Light 300. Aeonik is a sparse secondary face, not the default body family.
- The current presentation master contains inherited Inter/Helvetica Neue use and legacy `#E84142` furniture. Preserve those values only inside inherited presentation layouts; do not promote them to global tokens or rebuild the master to force global defaults.
- The identity is written `team1` in running text, with `Team1` allowed at sentence starts, titles, and proper-name boundaries. `TEAM1` is not an approved styling.
- Current approved QR destinations outrank archived QR artwork. Every delivered QR requires a verified destination, visible fallback URL, and scan testing from final exports.

## Gaps found in v1.0.0

The first package was a faithful extraction from one overview deck, but it could not serve as the complete current system after the wider audit.

| v1.0.0 behavior | v2 correction |
|---|---|
| Elevated `#FF394A`, `#E84142`, and `#F5384B` from one deck into broad brand roles | Restore `#E6212F` as the global Team1 red; scope inherited presentation colors to the presentation profile |
| Used Kanit Medium with Inter body copy as a general rule | Use Kanit Medium 500 and Kanit Light 300 globally; document medium-specific typography exceptions |
| Shipped a limited dark-field identity selection | Index the official wordmark, symbol, monochrome, square, profile-image, and favicon families for their intended contexts |
| Treated a 13-slide distilled overview as the main template | Make the August 3 40-exemplar master current; retain the old file only in controlled v1 history because its contextual media is not broadly reusable |
| Had derived web spacing, motion, responsive, and state guidance | Add current light/dark surfaces, semantic statuses, spacing, radii, z-index, breakpoints, container, touch-target, focus, and reduced-motion rules |
| Had limited regional, localization, social, print, photography, video, and governance coverage | Add medium-specific references, approvals, provenance, rights, accessibility, production, and go-live gates |
| Bundled historical photos, chapter graphics, and metric tiles without a complete current-authority model | Exclude or quarantine rights-sensitive, stale, claim-bearing, and context-specific material from the current reusable asset set |

## Package inclusion policy

### Included

- Exact current official Team1 identity assets with provenance and integrity hashes.
- Canonical global tokens plus explicitly scoped presentation, blog, chapter, social, photo, video, event, print, and regional guidance.
- The current presentation master as a font-clean export. The prior 13-slide deck remains in controlled v1 history and is excluded from v2 because it contains contextual people, partner, metric, and campaign media.
- Reusable, non-personal production instructions for digital, presentation, social, event, print, merchandise, localization, photography, video, voice, governance, and QA.
- Asset indexes, checksums, validation scripts, compatibility guidance, and source-authority documentation needed by agent harnesses.

### Excluded or reference-only

- Font binaries without verified redistribution rights, including proprietary type families.
- Member, attendee, applicant, recognition, operational, or contact data.
- Participant photography and event media without artifact-specific rights, consent, and context confirmation.
- Archived or unverified QR codes, redirects, campaign links, and tracking destinations.
- Unverified historical metrics, baked claims, dated statistics, and claim-bearing tiles.
- Older regional marks, campaign lockups, partner marks, and sponsor relationships unless current approval is independently verified.
- Editable production archives and bulk source media whose rights or reuse scope are not established for broad distribution.
- Macros, active content, external relationships, embedded font payloads, and other non-portable presentation content.

Exclusion from the portable package does not declare an item invalid. It means the item is contextual, rights-sensitive, stale, duplicated, operational, or insufficiently authoritative for general agent reuse.

## Limitations

One externally linked USA-specific guide was not accessible within the reviewed shared-drive scope. It was not evaluated, copied, or used as authority. This audit therefore makes no completeness claim for additional USA-only rules that may exist in that external source; any USA production must obtain and review the current approved guide before release.

The audit is a dated source snapshot. Time-sensitive destinations, event facts, partner relationships, chapter status, photo permissions, and production approvals must still be reverified at the time an artifact is produced.
