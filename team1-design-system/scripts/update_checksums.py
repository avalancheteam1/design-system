#!/usr/bin/env python3
"""Regenerate checksums.sha256 for the portable Team1 skill folder."""

import hashlib
import sys
from pathlib import Path


IGNORED_FILE_NAMES = {"checksums.sha256", ".DS_Store"}
IGNORED_DIRECTORY_NAMES = {".git", "__pycache__"}


def portable_files(root):
    root = Path(root).resolve()
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if relative.name in IGNORED_FILE_NAMES:
            continue
        if any(part in IGNORED_DIRECTORY_NAMES for part in relative.parts):
            continue
        yield relative


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def update_checksums(root):
    root = Path(root).resolve()
    if not (root / "SKILL.md").is_file():
        raise FileNotFoundError(f"SKILL.md not found in {root}")

    lines = []
    for relative in portable_files(root):
        digest = sha256_file(root / relative)
        lines.append(f"{digest}  {relative.as_posix()}")

    checksum_path = root / "checksums.sha256"
    checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return checksum_path


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    root = Path(argv[0]) if argv else Path(__file__).resolve().parents[1]
    checksum_path = update_checksums(root)
    print(f"Updated {checksum_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
