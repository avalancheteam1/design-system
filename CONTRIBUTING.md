# Contributing to the Team1 Design System

Thank you for helping Team1 make consistent, useful community materials. This repository is private, but the same care still applies to brand ownership, participant privacy, partner assets, and factual accuracy.

## Before contributing

- Read the package [`SKILL.md`](team1-design-system/SKILL.md), [authority](team1-design-system/references/authority.md), [identity](team1-design-system/references/identity.md), [governance and QA](team1-design-system/references/governance-and-qa.md), and [usage notice](team1-design-system/NOTICE.md).
- Search existing [issues](https://github.com/avalancheteam1/design-system/issues) before opening a new one.
- Confirm you are authorized to submit any logo, photograph, template, copy, or third-party material included in the change.
- Remove secrets, attendee lists, private contact details, unapproved links, tracking data, and unnecessary personal information.

Small spelling, link, and clarity fixes may go directly to a pull request. Open an issue first for changes to logos, core colors, typography, templates, official brand rules, chapter identities, photography, partner material, or redistribution policy.

## What needs approval

| Change | Required evidence or approval |
|---|---|
| Packaging, installation, validator, or documentation correction | Reproducible problem, source documentation, or a clear before/after explanation |
| New derived recommendation | Practical rationale, target medium, and a clear `derived` label |
| Change to an observed brand rule or core token | Evidence from a newer explicitly approved Team1 source and Team1 brand/community-owner review |
| Logo, chapter tile, partner mark, or official template | Authentic source file, provenance, current relationship, allowed use, and relevant owner approval |
| Photograph or image depicting people | Source, permission/reuse context, intended channels and territory, and privacy review where needed |
| Metric, link, QR, program name, chapter status, or partner claim | Current dated source and an approved publication destination |
| External distribution or licensing change | Explicit Team1 organizational approval; repository access is not sufficient |

Do not redraw or generate substitute identity assets. Do not convert a practical recommendation into an “official” rule without evidence and approval.

## Pull-request workflow

1. For material brand or asset changes, open the appropriate issue and wait for direction before doing extensive work.
2. Create a focused branch and keep unrelated changes in separate pull requests.
3. Preserve the nested `team1-design-system/` directory name and the `name: team1-design-system` field in `SKILL.md`.
4. Update only the canonical source files relevant to the change. Keep observed rules distinct from derived guidance.
5. Add or update provenance, status, and warnings in [`assets/asset-index.json`](team1-design-system/assets/asset-index.json) for every asset change.
6. Render and inspect visual changes in the application and export format they affect.
7. Update [`CHANGELOG.md`](team1-design-system/CHANGELOG.md) when the change is user-visible.
8. Refresh checksums after all package edits are final, run validation, and open a pull request using the repository template.

## Adding or changing assets

For every asset, record:

- the relative package path;
- the authentic source and, when available, source filename or checksum;
- its category and intended role;
- whether it may be modified;
- whether it is current, historical, restricted, or awaiting approval;
- any context, channel, territory, partner, or participant limitation.

An asset appearing in an older Team1 deck proves provenance, not automatically current publication rights. Do not add screenshot crops of missing marks, synthetic event photography presented as real, stale QR codes, or media whose reuse context cannot be established.

## Validation and visual QA

Run from the repository root:

```sh
python3 team1-design-system/scripts/update_checksums.py team1-design-system
python3 team1-design-system/scripts/validate_package.py team1-design-system
python3 -m unittest discover -s tests -v
```

Run the checksum updater only after the package change is complete. Never edit `checksums.sha256` manually.

For visual changes, also follow the complete [governance and delivery QA](team1-design-system/references/governance-and-qa.md). Attach a contact sheet or before/after render to the pull request when a template, layout, logo treatment, crop, typography rule, or color role changes. Source-file inspection alone is not visual QA.

## Versioning and releases

Repository maintainers own version numbers, tags, and release publication. A release should keep these values aligned:

- `SKILL.md` metadata version;
- `manifest.json` version and release date;
- `CHANGELOG.md` entry;
- `checksums.sha256`;
- Git tag and private GitHub release.

The release ZIP must contain one top-level `team1-design-system/` folder. GitHub's automatically generated source archive is a repository snapshot, not the portable skill release.

## Review and merging

Repository maintainers may merge documentation, packaging, and implementation corrections after the required checks pass. Changes to identity, official rules, public asset use, partner relationships, or distribution require the relevant Team1 or asset-owner approval in addition to technical review.

No response, expired status, or successful test run should be interpreted as brand or publication approval.
