# Support

GitHub Issues are the support channel for this private repository. Discussions are not currently enabled.

## Choose the right route

- **Installation or usage help:** open a [help request](https://github.com/avalancheteam1/design-system/issues/new?template=help.yml).
- **Broken package, asset path, validator, link, or template behavior:** open a [bug report](https://github.com/avalancheteam1/design-system/issues/new?template=bug.yml).
- **Proposed brand rule, logo, photo, chapter, partner, token, or template change:** open a [brand or asset change request](https://github.com/avalancheteam1/design-system/issues/new?template=brand-change.yml).
- **Security, privacy-sensitive, or secret-exposure concern:** follow [SECURITY.md](SECURITY.md). Do not put sensitive details in a normal issue.

Search [existing issues](https://github.com/avalancheteam1/design-system/issues) before opening a new one.

## What to include

For installation or package problems, include:

- the agent harness and version;
- operating system;
- package version and installation method;
- the exact folder containing `SKILL.md`;
- the prompt or action that exposed the problem;
- expected and actual behavior;
- validator output and a sanitized screenshot when useful.

For brand or asset requests, include the source, intended audience/channel, current approval evidence, factual verification date, and any rights or participant constraints. Do not upload secrets, private attendee data, personal contact details, or unapproved sensitive media.

## Quick checks

Before filing an installation issue:

1. Confirm the installed directory is named `team1-design-system` and contains `SKILL.md` directly inside it.
2. Confirm the entire folder—not only `SKILL.md`—was installed or uploaded.
3. Start a fresh agent session so its skill list is reloaded.
4. From inside the installed `team1-design-system/` directory, run:

   ```sh
   python3 scripts/validate_package.py .
   ```

5. Use the verification prompt in the [installation guide](team1-design-system/references/compatibility.md).

## Support and approval are different

Repository maintainers can diagnose packaging and documentation problems. They cannot automatically approve a photograph, partner relationship, chapter claim, historical metric, QR destination, or public campaign.

If publication approval is still missing, keep the work in draft. A closed issue, merged pull request, or lack of response is not publication approval.

Support is provided by the community without a guaranteed response time. For time-sensitive work, provide the deadline and safe fallback, but do not bypass the approval boundaries in [GOVERNANCE.md](GOVERNANCE.md).
