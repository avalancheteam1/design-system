# Security Policy

## Supported version

Security fixes are applied to the latest private release and the current default branch. Older downloaded copies should be replaced rather than patched file by file.

## What to report

Report concerns involving:

- malicious or unexpected instructions in `SKILL.md` or supporting references;
- unsafe path handling, checksum bypasses, archive traversal, or validator behavior;
- unexpected network access, secret collection, hooks, macros, external relationships, or active content;
- a compromised release archive or mismatch between a published checksum and release asset;
- credentials, private participant data, or other sensitive information accidentally committed to the repository;
- a bundled link or QR destination that may be malicious or compromised.

Brand disagreements, missing approvals, outdated metrics, and ordinary package bugs are not security vulnerabilities. Route them through [SUPPORT.md](SUPPORT.md), unless the report also exposes private or exploitable information.

## Report privately

Do not open a normal issue containing secrets, personal data, exploit details, or sensitive media.

Use GitHub's private vulnerability-reporting control if it is available in the repository's **Security** tab. If it is unavailable, contact a repository maintainer through Team1's established private organizational channel and share only the minimum information needed to route the report. This file intentionally does not invent an unmonitored email address or person.

Include, where safe:

- affected version, file, and path;
- impact and conditions required to reproduce it;
- minimal reproduction steps;
- whether a secret or personal record was exposed;
- suggested containment, if known.

Do not include live credentials. If a secret was exposed, revoke or rotate it through its owning system immediately; removing it from the latest commit is not sufficient.

## What happens next

Maintainers will validate the report, limit access to sensitive evidence, coordinate with the relevant Team1 or asset owner, and prepare a corrected package when warranted. A corrected release should receive a new version, checksum, changelog entry, and private release asset.

No response-time or disclosure deadline is guaranteed. Please avoid public disclosure until the affected Team1 owner has had a reasonable opportunity to contain the issue.
