# Governance and delivery QA

Use this workflow for every public or shared artifact:

`brief → authority check → content walkthrough → design review → Team1 review → automated/source checks → final code/artifact review → go-live approval → documented handoff`

Assign a content owner, design owner, implementation/production owner, and final approver. Record outcomes as `PASS`, `WARN`, `FAIL`, `MANUAL`, or `N/A`, with evidence. A required `FAIL` blocks delivery. A rights, naming, partner, privacy, or destination `MANUAL` check blocks publication until a named owner approves it.

## Before production

- Confirm audience, language/locale, medium, dimensions, channel, deadline, required source and export formats.
- Record the authoritative source version and medium profile. Reject archive, `_OLD`, migration, screenshot-derived, and untraceable assets.
- Confirm rights for logos, fonts, photos, video, music, partner marks, and third-party content.
- Verify facts, claims, dates/timezones, programs, partners, links, handles, and QR destinations.
- Keep member/applicant identities, contacts, private operations data, credentials, internal URLs, and restricted media out of public artifacts.

## Brand review

- Current primary red is `#E6212F`; `#FF394A` fails current-primary use; `#E84142` is limited to Avalanche/inherited-presentation scope.
- Approved marks retain their file, proportions, clear space, lowercase `t`, and intended background variant.
- `Team1`/`team1` usage is intentional; `TEAM1` fails.
- Medium-specific typography and color exceptions stay inside their documented scope.
- Team1 is primary in Team1-led work; partner marks have optical parity and an approved relationship.

## Functional and accessibility review

- Inspect hierarchy, contrast, reading order, keyboard access, focus, alt text/captions, motion preference, touch size, responsive behavior, and error states where applicable.
- Render every output at its final dimensions. Check overflow, clipping, substitution, image crop, compression, color, and platform UI/safe areas.
- Test links and QR codes from the final export and their real viewing distance. Pair QR with a visible fallback.
- For presentations, inspect every slide plus the contact sheet and test the target app/hardware.
- For print/merch, approve vendor preflight and a physical or photographed proof.
- For localized work, test script coverage, text expansion, date/timezone, and fluent review.

## Handoff

Deliver the editable source, requested exports, versioned filenames, source/rights ledger, and a concise exceptions report. Remove hidden notes, stale links, personal paths, secrets, private identifiers, embedded font binaries without redistribution rights, and unused/restricted media. Confirm files open successfully and record final approval, delivery date, owner, and future expiry/review triggers.
