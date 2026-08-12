# Cross-harness installation

Verified against primary documentation on 2026-08-12. Discovery paths and product interfaces can change; if a tool disagrees with this file, follow that tool’s current official skill settings while keeping this folder unchanged.

The package follows the open [Agent Skills specification](https://agentskills.io/specification): a directory whose canonical entrypoint is `SKILL.md`, with relative references, assets, and optional scripts.

## Get the canonical package

For Team1 members with access, download `team1-design-system-v1.0.0.zip` from the [latest private GitHub release](https://github.com/avalancheteam1/design-system/releases/latest). The release archive contains one correctly named top-level `team1-design-system/` directory.

If you clone the repository instead, use the nested skill folder rather than the repository root:

```sh
git clone https://github.com/avalancheteam1/design-system.git
cd design-system
python3 team1-design-system/scripts/validate_package.py team1-design-system
```

GitHub's automatically generated source archive is a repository snapshot named after `design-system`; it is not the portable skill release. Install the nested `team1-design-system/` folder or the attached release ZIP.

## Universal fallback — works with any capable agent

Attach or expose the complete `team1-design-system` folder, then instruct the agent:

> Read `SKILL.md` completely, resolve every referenced path relative to this folder, load only the references needed for the task, and apply the Team1 QA checklist before delivery.

This requires no special registry or universal configuration schema. A text-only harness can produce a compliant brief/specification or review; final visual production requires access to the relevant editing and rendering tools.

## Codex and ChatGPT

OpenAI describes skills as shareable `SKILL.md` workflows that can be reviewed, installed, and reused across workspaces: [Using skills](https://openai.com/academy/skills/).

- In a workspace with a Skills interface, upload the release ZIP or install the unpacked skill there.
- For local Codex, copy the complete folder into the skill root shown by the installed Codex app/CLI. The Codex Desktop environment used to build this release currently loads personal skills from `~/.codex/skills/<skill-name>/`.
- Start a new task if the skill list was cached, then invoke `$team1-design-system` or ask naturally for Team1-branded work.

Do not assume a community post or an older `~/.agents/skills` example overrides the discovery root displayed by the installed Codex version.

## Claude Code

Claude Code follows the Agent Skills standard and documents these locations: [Claude Code skills](https://code.claude.com/docs/en/skills).

- Personal: `~/.claude/skills/team1-design-system/`
- Project: `.claude/skills/team1-design-system/`

Copy the complete folder so `SKILL.md` sits directly inside that directory. Start Claude Code and invoke `/team1-design-system`, or use a prompt that matches its description. Claude cloud/Cowork sessions may require account upload or a skill committed inside the project rather than a local home-directory install.

## OpenClaw

OpenClaw documents local directory installation and multiple skill scopes: [OpenClaw skills](https://docs.openclaw.ai/tools/skills).

From the directory containing the unpacked folder:

```sh
openclaw skills install ./team1-design-system --as team1-design-system
```

Without the CLI installer, supported discovery roots include a workspace `skills/` directory, `<workspace>/.agents/skills/`, `~/.agents/skills/`, and the managed OpenClaw state skill directory. A Git install expects `SKILL.md` at the Git source root, so this repository's nested layout is best consumed through the release ZIP or a local checkout of its `team1-design-system/` subfolder.

Start a fresh OpenClaw session and ask naturally: **“Use the `team1-design-system` skill to create…”** Then run the verification prompt below.

## Hermes Agent

Hermes loads `SKILL.md` packages progressively and supports user-created skills under `~/.hermes/skills/`: [Working with Skills](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/guides/work-with-skills.md).

Copy the complete folder to:

```text
~/.hermes/skills/team1-design-system/
```

Start a new session, run `hermes skills list`, then invoke `/team1-design-system`. Hermes also supports installing a hosted `SKILL.md` URL, but a local copy of this complete release is preferred because the skill depends on bundled binary assets and templates.

## Generic Agent Skills clients

Point the client’s documented skill root or loader at the unpacked folder. A compliant loader should index `name` and `description` from the YAML frontmatter, load the body only when selected, and resolve supporting files relative to the skill root. Do not invent configuration keys: use the client’s actual schema.

## Verification after any install

1. Confirm `team1-design-system` appears in the tool’s skill list or can be invoked explicitly.
2. Start a fresh session.
3. Ask: “Use the Team1 design system to outline a three-slide local meetup deck and name the exact bundled frame and assets for each slide.”
4. A valid response should reference the bundled template, authentic asset paths, the two typography modes, the three red roles, and the final QA checklist.
5. If it only produces generic black/red styling, the skill or its supporting folder was not loaded.

## Security and update model

Review the folder before installation. This release has no network requirement, secret, hook, plugin, MCP server, or automatic installer. Its only executable is an optional standard-library validator. Update by replacing the entire versioned folder, not by merging vendor-specific forks.

To update, download the newest private release, validate it, and replace the old complete folder. If discovery fails, confirm that the installed folder is exactly `team1-design-system`, that `SKILL.md` sits directly inside it, and that the complete `assets/`, `references/`, `tokens/`, and `templates/` directories came with it.
