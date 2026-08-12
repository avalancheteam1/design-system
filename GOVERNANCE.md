# Governance

This repository maintains the portable Team1 design-system package. Governance separates technical stewardship from brand, content, and rights approval.

## Roles

### Repository maintainers

People with repository maintenance permissions manage issue triage, packaging, tests, checksums, versions, releases, and merges. They may correct reproducible documentation or implementation defects.

Repository maintenance permission does not automatically grant authority over trademarks, participant imagery, partner relationships, chapter status, public claims, or external distribution.

### Team1 brand and community stewards

The relevant Team1 brand owner, global community lead, or authorized local lead decides whether a proposed rule, identity change, campaign, chapter claim, or public asset use is approved. The appropriate steward depends on the scope of the change.

### Contributors

Contributors identify problems, propose improvements, provide provenance and approval evidence, and complete the documented QA. A contribution is a proposal until it is reviewed and merged.

## Decision boundaries

| Decision | Who can approve it |
|---|---|
| Typo, broken link, portability fix, or validator correction | Repository maintainer after checks pass |
| New derived guidance for a specific medium | Repository maintainer, with the guidance labeled as derived |
| Change to an observed brand rule, core token, or canonical template | Relevant Team1 brand/community steward plus repository maintainer |
| New or changed Team1, Avalanche, chapter, or partner identity asset | Relevant identity or relationship owner plus repository maintainer |
| Publication of photographs, participant imagery, metrics, links, QR codes, or partner claims | Relevant content/asset owner or community lead for the intended context |
| Public release, relicensing, or redistribution outside authorized Team1 work | Team1 organizational approval |

Silence is not approval. A test pass proves package integrity, not brand, legal, factual, or publication approval.

## Authority order

When sources conflict, use the hierarchy in the package [authority guide](team1-design-system/references/authority.md). A newer source supersedes the pinned global system only when the relevant Team1 owner explicitly approved it and its date, owner, and scope are recorded; a requester brief alone does not redefine the identity.

Do not silently blend conflicting sources. Record the conflict in the issue or pull request and ask the appropriate steward to decide.

## Change process

1. Use an issue to state the problem, evidence, affected audiences, and approval needs.
2. Use a focused pull request to show the exact change and its QA evidence.
3. Keep source-evidenced observations separate from derived recommendations.
4. Obtain the approval required by the decision table.
5. Merge only after package tests, checksums, links, and visual QA pass as applicable.
6. Publish user-visible changes through a versioned private release and changelog entry.

Emergency deadlines do not broaden authority. If a required fact, asset permission, or owner decision is unavailable, keep the artifact in draft or use a clearly labeled placeholder.

## Maintainer identity

This document intentionally does not invent personal maintainers or organization teams. GitHub repository permissions are the current source for technical maintainer access. A `CODEOWNERS` file may be added after Team1 confirms the correct durable user or organization-team handles.

## Changing governance

Governance changes use the same issue and pull-request process. Material changes to approval, licensing, or distribution require Team1 organizational review.
