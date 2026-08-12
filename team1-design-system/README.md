# Team1 Design System Agent Skill

This is the Team1 visual system packaged for humans and AI agents. One unchanged folder works as an Agent Skill in compatible tools and as a self-contained brand kit everywhere else.

## Quick start

1. Download `team1-design-system-v1.0.0.zip` from the [latest private release](https://github.com/avalancheteam1/design-system/releases/latest), or use the `team1-design-system/` folder in an authorized repository checkout.
2. Unzip it and keep the whole `team1-design-system` folder together. Do not upload only `SKILL.md`; the assets, tokens, references, and templates are part of the system.
3. Install or upload the folder using the [cross-harness guide](references/compatibility.md).
4. Start a fresh agent session and say: **“Use the team1-design-system skill to create…”**
5. Supply the real brief: audience, language, format, dimensions, deadline, approved copy, facts, links, partner marks, and photos.
6. Ask for both the editable source and the final export, with a visual QA pass.

If the tool has no skill feature, attach the complete folder or ZIP and instruct it to read `SKILL.md` first. That is the universal fallback.

## What is included

- `SKILL.md` — the canonical workflow and guardrails.
- `references/` — brand rules, layout selection, collateral guidance, QA, and current install notes.
- `tokens/` — machine-readable design tokens plus CSS convenience variables.
- `assets/` — authentic Team1/Avalanche marks, source backgrounds, chapter and metric specimens, graphics, and documentary photography.
- `templates/Team1 Design System.pptx` — editable 16:9 presentation source with inherited Team1 layouts.
- `templates/Team1 Design System.pdf` — read-only visual reference for agents without PowerPoint support.
- `examples/` — ready-to-copy prompts and an event-deck frame-map example.
- `scripts/validate_package.py` — offline package integrity and portability check.
- `scripts/update_checksums.py` — maintainer utility for refreshing the package manifest after an approved change.

## Authority order

1. The current verified brief and any newer explicitly approved Team1 source.
2. Authentic bundled assets and the presentation template.
3. Machine-readable tokens.
4. Written reference rules.
5. Approved examples.
6. Agent judgment, clearly labeled as derived.

Conflicts should be surfaced, not silently blended.

## Important boundaries

- The package does not grant trademark, photography, or redistribution rights; see `NOTICE.md`.
- No font files are redistributed. Install Kanit and Inter for authoring new copy. Helvetica Neue requires a licensed local installation where used.
- Source metrics and program labels are historical evidence, not automatically current claims.
- The legacy QR asset from the source deck is excluded on purpose.

## Validate a copy

From inside this folder, run:

```sh
python3 scripts/validate_package.py .
```

The validator requires only Python 3 and no network access.

## Version

Version 1.0.0, built from the Team1 Overview source deck whose SHA-256 is recorded in `references/source-provenance.md`.

The repository is named [`avalancheteam1/design-system`](https://github.com/avalancheteam1/design-system), while the portable skill folder must remain named `team1-design-system` to match the Agent Skills specification.
