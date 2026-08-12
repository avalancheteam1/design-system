#!/usr/bin/env python3
"""Validate the portable Team1 Agent Skill package with Python's standard library."""

import hashlib
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "NOTICE.md",
    "manifest.json",
    "tokens/design-tokens.json",
    "assets/asset-index.json",
)
REQUIRED_COLORS = ("#000000", "#FFFFFF", "#FF394A", "#E84142", "#F5384B")
TEXT_SUFFIXES = {".css", ".json", ".md", ".py", ".txt", ".yaml", ".yml"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MACOS_USER_ROOT = "/" + "Users" + "/"
WINDOWS_USER_ROOT = re.compile(r"[A-Za-z]:[\\\\/]" + "Users" + r"[\\\\/]")
CHECKSUM_PATTERN = re.compile(r"^[0-9a-f]{64}$")
IGNORED_FILE_NAMES = {"checksums.sha256", ".DS_Store"}
IGNORED_DIRECTORY_NAMES = {".git", "__pycache__"}


def _frontmatter(skill_path):
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, "SKILL.md must start with YAML frontmatter"
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, "SKILL.md frontmatter is not closed"

    values = {}
    in_metadata = False
    for raw_line in text[4:end].splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        if indent == 0:
            in_metadata = key == "metadata"
            if value:
                values[key] = value
        elif in_metadata and key == "version":
            values["metadata.version"] = value
    return values, None


def _all_strings(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from _all_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from _all_strings(child)
    elif isinstance(value, str):
        yield value


def _portable_files(root):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if relative.name in IGNORED_FILE_NAMES:
            continue
        if any(part in IGNORED_DIRECTORY_NAMES for part in relative.parts):
            continue
        yield relative


def _sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _verify_checksums(root, errors):
    checksum_path = root / "checksums.sha256"
    if not checksum_path.exists():
        return
    indexed = set()
    for line_number, line in enumerate(
        checksum_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        parts = line.split("  ", 1)
        if len(parts) != 2:
            errors.append(f"checksums.sha256:{line_number} is malformed")
            continue
        expected, relative = parts
        candidate = Path(relative)
        if (
            not relative
            or candidate.is_absolute()
            or ".." in candidate.parts
            or any(part in IGNORED_DIRECTORY_NAMES for part in candidate.parts)
            or candidate.name in IGNORED_FILE_NAMES
        ):
            errors.append(f"checksum path is unsafe: {relative!r}")
            continue
        normalized = candidate.as_posix()
        if normalized in indexed:
            errors.append(f"duplicate checksum entry: {normalized}")
            continue
        indexed.add(normalized)
        if not CHECKSUM_PATTERN.fullmatch(expected):
            errors.append(f"checksums.sha256:{line_number} has an invalid digest")
            continue
        target = (root / candidate).resolve()
        try:
            target.relative_to(root)
        except ValueError:
            errors.append(f"checksum path is unsafe: {relative!r}")
            continue
        if not target.is_file():
            errors.append(f"checksum target is missing: {relative}")
            continue
        actual = _sha256_file(target)
        if actual != expected:
            errors.append(f"checksum mismatch: {relative}")

    present = {relative.as_posix() for relative in _portable_files(root)}
    for relative in sorted(present - indexed):
        errors.append(f"checksum manifest missing entry: {relative}")


def validate(root):
    root = Path(root).resolve()
    errors = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"required file is missing: {relative}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        frontmatter, frontmatter_error = _frontmatter(skill_path)
        if frontmatter_error:
            errors.append(frontmatter_error)
        else:
            name = frontmatter.get("name", "")
            description = frontmatter.get("description", "")
            if not NAME_PATTERN.fullmatch(name):
                errors.append("frontmatter name must use lowercase letters, numbers, and hyphens")
            if name != root.name:
                errors.append("parent directory name must match frontmatter name")
            if not description.startswith("Use when "):
                errors.append("frontmatter description must begin with 'Use when '")
            if len(description) > 1024:
                errors.append("frontmatter description exceeds 1024 characters")

            manifest_path = root / "manifest.json"
            if manifest_path.is_file():
                try:
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    errors.append(f"manifest.json is invalid: {exc}")
                else:
                    if not isinstance(manifest, dict):
                        errors.append("manifest.json must contain an object")
                    elif manifest.get("id") != name:
                        errors.append("manifest id must match frontmatter name")
                    if isinstance(manifest, dict):
                        if manifest.get("entrypoint") != "SKILL.md":
                            errors.append("manifest entrypoint must be SKILL.md")
                        skill_version = frontmatter.get("metadata.version")
                        if skill_version and manifest.get("version") != skill_version:
                            errors.append("manifest version must match frontmatter metadata.version")

    token_path = root / "tokens" / "design-tokens.json"
    if token_path.is_file():
        try:
            token_data = json.loads(token_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"design-tokens.json is invalid: {exc}")
        else:
            token_strings = set(_all_strings(token_data))
            for color in REQUIRED_COLORS:
                if color not in token_strings:
                    errors.append(f"required Team1 color token is missing: {color}")

    index_path = root / "assets" / "asset-index.json"
    if index_path.is_file():
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"asset-index.json is invalid: {exc}")
        else:
            if not isinstance(index, dict):
                errors.append("asset-index.json must contain an object")
            else:
                assets = index.get("assets", [])
                if not isinstance(assets, list):
                    errors.append("asset-index.json assets must contain a list")
                    assets = []
                indexed_assets = set()
                for item in assets:
                    if not isinstance(item, dict):
                        errors.append("asset-index.json asset entries must be objects")
                        continue
                    relative = item.get("path", "")
                    candidate = Path(relative)
                    if not relative or candidate.is_absolute() or ".." in candidate.parts:
                        errors.append(f"indexed asset path is unsafe: {relative!r}")
                        continue
                    normalized = candidate.as_posix()
                    indexed_assets.add(normalized)
                    target = (root / candidate).resolve()
                    try:
                        target.relative_to(root)
                    except ValueError:
                        errors.append(f"indexed asset path is unsafe: {relative!r}")
                    else:
                        if not target.is_file():
                            errors.append(f"indexed asset is missing: {relative}")

                asset_root = root / "assets"
                actual_assets = {
                    path.relative_to(root).as_posix()
                    for path in asset_root.rglob("*")
                    if path.is_file()
                    and path.name not in {"README.md", "asset-index.json", ".DS_Store"}
                    and "__pycache__" not in path.parts
                }
                for relative in sorted(actual_assets - indexed_assets):
                    errors.append(f"asset index missing entry: {relative}")

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if MACOS_USER_ROOT in content or WINDOWS_USER_ROOT.search(content):
            relative = path.relative_to(root)
            errors.append(f"absolute maintainer path found in {relative}")

    _verify_checksums(root, errors)
    return errors


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    root = Path(argv[0]) if argv else Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("Team1 package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Team1 package valid: {root.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
