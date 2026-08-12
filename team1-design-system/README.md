# Team1 Design System Agent Skill

Version 2.0.0 is a portable Team1 brand and production system for humans and AI agents. It combines the current global identity, official logo families, current chapter vectors, a current presentation master, machine-readable tokens, medium-specific rules, and output QA.

## Quick start

1. Download `team1-design-system-v2.0.0.zip` from the [latest private release](https://github.com/avalancheteam1/design-system/releases/latest), or use this folder from an authorized checkout.
2. Keep the complete directory named `team1-design-system`; `SKILL.md`, assets, tokens, templates, and references work together.
3. Follow the [cross-harness guide](references/compatibility.md), start a fresh session, and say: “Use the team1-design-system skill to create…”
4. Supply audience, locale, dimensions, deadline, approved copy/facts, links, photos, partner files, editable format, and final export.
5. Require rendered QA and a fact/source/rights ledger.

If the harness has no Skills feature, attach the complete folder or ZIP and ask it to read `SKILL.md` first.

## Authority hierarchy

1. A newer explicitly approved Team1 source, with its date and owner recorded.
2. The 2026 global brand guide and current official Brand Assets source.
3. The current medium-specific authority: for presentations, the August 2026 master; for photography, the July 2026 photography guide.
4. Bundled current identity assets and global tokens.
5. Written medium modules and approved examples.
6. Clearly labeled derived production judgment.

Old decks, screenshots, archived folders, campaign files, regional examples, and Avalanche defaults are evidence—not automatic authority. See [authority and conflict resolution](references/authority.md).

## Included

- `SKILL.md` — compact agent workflow and hard rules.
- `references/` — identity, web, presentation, social, event/print, regional, photo/video, copy, governance, provenance, and compatibility modules.
- `tokens/` — global tokens plus explicitly scoped presentation, chapter, video, and blog profiles.
- `assets/identity/` — current wordmark, symbol, square, PFP, and favicon families.
- `assets/chapters/` — current verified chapter SVG module with provenance and usage gates.
- `templates/Team1 Current Presentation Template.pptx` — editable current 40-exemplar master, sanitized to remove embedded font payloads.
- `templates/Team1 Current Presentation Template.pdf` — read-only 40-page visual reference.
- `previews/current-presentation-master-contact-sheet.png` — all 40 current exemplar slides for source-selection review.
- `examples/` — prompts and production maps.
- `scripts/` — offline validation and checksum maintenance.

See the [photography/video](references/photography-and-video.md), [voice/copy](references/voice-and-copy.md), and [governance/QA](references/governance-and-qa.md) modules directly when those parts of a brief are in scope.

## Deliberately excluded

No font binaries, participant/member photography, attendee data, recognition decks, live or archived QR payloads, partner logos, licensed music/SFX, raw video, stock libraries, campaign PSD/AI sources, legacy presentations with contextual media, private operational records, or archive/migration assets are redistributed. The system documents how to request and validate those materials safely.

## Validate

From inside this folder:

```sh
python3 scripts/validate_package.py .
```

From the repository root:

```sh
python3 team1-design-system/scripts/validate_package.py team1-design-system
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

After an approved package edit, refresh checksums last:

```sh
python3 team1-design-system/scripts/update_checksums.py team1-design-system
```

## Rights

This private package supports authorized Team1 work. It does not grant new trademark, copyright, publicity, photography, partner, font, or external redistribution rights. Read [NOTICE.md](NOTICE.md) and every asset status before publication.
