import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "team1-design-system"
VALIDATOR_PATH = SKILL_ROOT / "scripts" / "validate_package.py"
UPDATER_PATH = SKILL_ROOT / "scripts" / "update_checksums.py"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {name} at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_minimal_skill(root):
    skill_root = root / "team1-design-system"
    write_text(
        skill_root / "SKILL.md",
        """---
name: team1-design-system
description: Use when creating or reviewing Team1-branded visual artifacts.
license: See NOTICE.md
metadata:
  version: "1.0.0"
---

# Team1 Design System
""",
    )
    write_text(skill_root / "README.md", "# Team1 Design System\n")
    write_text(skill_root / "NOTICE.md", "Brand assets remain with their owners.\n")
    write_text(
        skill_root / "manifest.json",
        json.dumps(
            {
                "schemaVersion": "1",
                "id": "team1-design-system",
                "version": "1.0.0",
                "entrypoint": "SKILL.md",
                "format": "https://agentskills.io/specification",
            }
        ),
    )
    write_text(
        skill_root / "tokens" / "design-tokens.json",
        json.dumps(
            {
                "color": {
                    "canvas": {"$type": "color", "$value": "#000000"},
                    "text": {"$type": "color", "$value": "#FFFFFF"},
                    "signal": {"$type": "color", "$value": "#FF394A"},
                    "structure": {"$type": "color", "$value": "#E84142"},
                    "themeAccent": {"$type": "color", "$value": "#F5384B"},
                }
            }
        ),
    )
    write_text(
        skill_root / "assets" / "asset-index.json",
        json.dumps(
            {
                "schemaVersion": "1",
                "assets": [
                    {
                        "path": "assets/logos/team1-mark.png",
                        "role": "approved Team1 mark",
                        "source": "Team1 Overview.pptx",
                    }
                ],
            }
        ),
    )
    write_text(skill_root / "assets" / "logos" / "team1-mark.png", "fixture")
    return skill_root


class PackageValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_module("team1_validator", VALIDATOR_PATH)

    def test_minimal_valid_package_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            self.assertEqual([], self.validator.validate(skill_root))

    def test_parent_directory_must_match_frontmatter_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            renamed = skill_root.with_name("wrong-name")
            skill_root.rename(renamed)
            errors = self.validator.validate(renamed)
            self.assertTrue(any("directory name" in error for error in errors))

    def test_missing_indexed_asset_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            (skill_root / "assets" / "logos" / "team1-mark.png").unlink()
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("indexed asset" in error for error in errors))

    def test_unindexed_asset_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(skill_root / "assets" / "logos" / "unindexed.png", "fixture")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("asset index missing entry" in error for error in errors))

    def test_manifest_top_level_must_be_an_object(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(skill_root / "manifest.json", "[]\n")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("manifest.json must contain an object" in error for error in errors))

    def test_asset_index_top_level_must_be_an_object(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(skill_root / "assets" / "asset-index.json", "[]\n")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("asset-index.json must contain an object" in error for error in errors))

    def test_maintainer_absolute_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(skill_root / "README.md", "Read /Users/example/private/source.pptx\n")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("absolute maintainer path" in error for error in errors))

    def test_windows_maintainer_absolute_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(skill_root / "README.md", "Read C:\\Users\\example\\private\\source.pptx\n")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("absolute maintainer path" in error for error in errors))

    def test_three_brand_red_roles_are_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            token_path = skill_root / "tokens" / "design-tokens.json"
            tokens = json.loads(token_path.read_text(encoding="utf-8"))
            del tokens["color"]["structure"]
            write_text(token_path, json.dumps(tokens))
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("#E84142" in error for error in errors))

    def test_checksum_manifest_must_cover_every_package_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            skill_hash = hashlib.sha256((skill_root / "SKILL.md").read_bytes()).hexdigest()
            write_text(skill_root / "checksums.sha256", f"{skill_hash}  SKILL.md\n")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("checksum manifest missing entry" in error for error in errors))

    def test_checksum_paths_must_stay_inside_package(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = Path(tmp)
            skill_root = build_minimal_skill(tmp_root)
            outside = tmp_root / "outside.txt"
            write_text(outside, "outside")
            outside_hash = hashlib.sha256(outside.read_bytes()).hexdigest()
            write_text(skill_root / "checksums.sha256", f"{outside_hash}  ../outside.txt\n")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("checksum path is unsafe" in error for error in errors))

    def test_checksum_updater_covers_portable_files(self):
        self.assertTrue(UPDATER_PATH.is_file(), "checksum updater is missing")
        updater = load_module("team1_checksum_updater", UPDATER_PATH)
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(skill_root / "examples" / "prompt.md", "Use Team1.\n")
            updater.update_checksums(skill_root)
            errors = self.validator.validate(skill_root)
            self.assertEqual([], errors)
            manifest = (skill_root / "checksums.sha256").read_text(encoding="utf-8")
            self.assertIn("examples/prompt.md", manifest)
            self.assertNotIn("checksums.sha256", manifest)


if __name__ == "__main__":
    unittest.main()
