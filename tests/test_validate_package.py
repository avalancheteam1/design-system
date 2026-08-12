import hashlib
import importlib.util
import json
import tempfile
import unittest
import zipfile
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
                    "brand": {"$type": "color", "$value": "#E6212F"},
                    "avaBlue": {"$type": "color", "$value": "#3055B3"},
                    "secondaryBlue": {"$type": "color", "$value": "#058AFF"},
                    "darkSurface": {"$type": "color", "$value": "#161617"},
                    "lightSurface": {"$type": "color", "$value": "#F5F5F9"},
                    "error": {"$type": "color", "$value": "#dc2626"},
                }
            }
        ),
    )
    write_text(
        skill_root / "assets" / "asset-index.json",
        json.dumps(
            {
                "schemaVersion": "2",
                "assets": [
                    {
                        "path": "assets/logos/team1-mark.png",
                        "category": "identity",
                        "role": "approved Team1 mark",
                        "status": "current-approved-source",
                        "authority": "current-global",
                        "source": "fixture",
                        "sha256": hashlib.sha256(b"fixture").hexdigest(),
                        "modifiable": False,
                        "rights": "authorized-use-only",
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

    def test_indexed_asset_hash_is_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(skill_root / "assets" / "logos" / "team1-mark.png", "changed")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("indexed asset hash mismatch" in error for error in errors))

    def test_duplicate_indexed_asset_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            index_path = skill_root / "assets" / "asset-index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["assets"].append(dict(index["assets"][0]))
            write_text(index_path, json.dumps(index))
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("duplicate indexed asset" in error for error in errors))

    def test_v2_asset_metadata_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            index_path = skill_root / "assets" / "asset-index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            del index["assets"][0]["rights"]
            write_text(index_path, json.dumps(index))
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("asset entry missing metadata" in error for error in errors))

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

    def test_current_global_brand_colors_are_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            token_path = skill_root / "tokens" / "design-tokens.json"
            tokens = json.loads(token_path.read_text(encoding="utf-8"))
            del tokens["color"]["brand"]
            write_text(token_path, json.dumps(tokens))
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("#E6212F" in error for error in errors))

    def test_checksum_manifest_must_cover_every_package_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            skill_hash = hashlib.sha256((skill_root / "SKILL.md").read_bytes()).hexdigest()
            write_text(skill_root / "checksums.sha256", f"{skill_hash}  SKILL.md\n")
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("checksum manifest missing entry" in error for error in errors))

    def test_checksum_manifest_rejects_unexpected_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            updater = load_module("team1_checksum_updater_unexpected", UPDATER_PATH)
            updater.update_checksums(skill_root)
            manifest = skill_root / "checksums.sha256"
            manifest.write_text(
                manifest.read_text(encoding="utf-8")
                + f"{'0' * 64}  missing.txt\n",
                encoding="utf-8",
            )
            errors = self.validator.validate(skill_root)
            self.assertTrue(
                any("checksum manifest has unexpected entry" in error for error in errors)
            )

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

    def test_symlinked_checksum_target_must_stay_inside_package(self):
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            skill_root = build_minimal_skill(temp_root)
            outside = temp_root / "outside.txt"
            write_text(outside, "outside")
            link = skill_root / "outside-link.txt"
            link.symlink_to(outside)
            checksum = hashlib.sha256(outside.read_bytes()).hexdigest()
            checksum_path = skill_root / "checksums.sha256"
            updater = load_module("team1_checksum_updater_symlink", UPDATER_PATH)
            updater.update_checksums(skill_root)
            checksum_path.write_text(
                checksum_path.read_text(encoding="utf-8")
                + f"{checksum}  outside-link.txt\n",
                encoding="utf-8",
            )
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("checksum path is unsafe" in error for error in errors))

    def test_symlinked_indexed_asset_must_stay_inside_package(self):
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            skill_root = build_minimal_skill(temp_root)
            outside = temp_root / "outside.svg"
            write_text(outside, "outside")
            link = skill_root / "assets" / "logos" / "outside.svg"
            link.symlink_to(outside)
            index_path = skill_root / "assets" / "asset-index.json"
            index = json.loads(index_path.read_text(encoding="utf-8"))
            index["assets"].append(
                {
                    "path": "assets/logos/outside.svg",
                    "category": "identity",
                    "role": "fixture",
                    "status": "fixture",
                    "authority": "fixture",
                    "source": "fixture",
                    "sha256": hashlib.sha256(outside.read_bytes()).hexdigest(),
                    "modifiable": False,
                    "rights": "fixture",
                }
            )
            write_text(index_path, json.dumps(index))
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("indexed asset path is unsafe" in error for error in errors))

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

    def test_validator_rejects_unsafe_pptx_payloads(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            template = skill_root / "templates" / "unsafe.pptx"
            template.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(template, "w") as archive:
                archive.writestr("ppt/fonts/font1.dat", b"font")
                archive.writestr(
                    "ppt/slides/_rels/slide1.xml.rels",
                    b'<Relationship TargetMode="External" Target="https://example.com"/>',
                )
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("embedded font payload" in error for error in errors))
            self.assertTrue(any("external relationship" in error for error in errors))

    def test_validator_rejects_unsafe_pdf_payloads(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_root = build_minimal_skill(Path(tmp))
            write_text(
                skill_root / "templates" / "unsafe.pdf",
                "%PDF-1.4\n/FontFile2 /JavaScript /EmbeddedFile /URI\n%%EOF\n",
            )
            errors = self.validator.validate(skill_root)
            self.assertTrue(any("embedded font program" in error for error in errors))
            self.assertTrue(any("active or external content" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
