## Summary

Describe the problem and the smallest change that solves it.

## Change type

- [ ] Documentation or link correction
- [ ] Packaging, installation, validation, or checksum change
- [ ] Derived guidance for a new medium
- [ ] Observed brand rule, token, or template change
- [ ] Logo, photo, chapter, partner, or other asset change
- [ ] Governance, rights, or distribution change

## Evidence and approval

Link the source, issue, current facts, and relevant approval. State whether each rule is observed or derived. For assets, describe provenance, allowed use, intended channels/territory, and any participant or partner restrictions.

## Validation

- [ ] I refreshed package checksums after the final package edit, or this PR does not change the portable package.
- [ ] `python3 team1-design-system/scripts/validate_package.py team1-design-system` passes.
- [ ] `python3 -m unittest discover -s tests -v` passes.
- [ ] I inspected rendered output when the change affects a visual artifact.
- [ ] I attached a contact sheet or before/after evidence for a visual change.

## Safety and rights

- [ ] I did not add secrets, private attendee data, unnecessary personal information, or unapproved tracking links.
- [ ] I am authorized to submit each new asset and documented its status in `assets/asset-index.json`.
- [ ] I did not treat a passing test, repository access, or silence as brand/publication approval.
- [ ] The nested skill directory and `name: team1-design-system` identifier remain unchanged.

## Handoff notes

List substitutions, unresolved approvals, migration steps, release notes, or follow-up work. Write `None` if there are none.
