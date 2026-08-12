import re
import unittest
import zipfile
import json
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "team1-design-system"
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class RepositoryTests(unittest.TestCase):
    def test_root_readme_routes_people_and_agents(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        required = (
            "team1-design-system/SKILL.md",
            "team1-design-system/README.md",
            "releases/latest",
            "Codex",
            "Claude",
            "OpenClaw",
            "Hermes",
        )
        for value in required:
            self.assertIn(value, readme)

    def test_community_documents_exist(self):
        for relative in ("CONTRIBUTING.md", "SUPPORT.md", ".github/pull_request_template.md"):
            self.assertTrue((REPO_ROOT / relative).is_file(), f"missing {relative}")

    def test_validation_workflow_exists(self):
        workflow = REPO_ROOT / ".github" / "workflows" / "validate.yml"
        self.assertTrue(workflow.is_file())
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("validate_package.py", text)
        self.assertIn("unittest", text)

    def test_package_docs_explain_repo_and_release_install(self):
        readme = (SKILL_ROOT / "README.md").read_text(encoding="utf-8")
        compatibility = (SKILL_ROOT / "references" / "compatibility.md").read_text(
            encoding="utf-8"
        )
        combined = readme + compatibility
        self.assertIn("https://github.com/avalancheteam1/design-system", combined)
        self.assertIn("releases/latest", combined)
        self.assertIn("team1-design-system", combined)
        self.assertIn("2026-08-12", compatibility)
        self.assertIn("Start a fresh OpenClaw session and ask naturally", compatibility)

    def test_release_metadata_uses_publication_date(self):
        manifest = json.loads((SKILL_ROOT / "manifest.json").read_text(encoding="utf-8"))
        changelog = (SKILL_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertEqual("2026-08-12", manifest["released"])
        self.assertIn("1.0.0 — 2026-08-12", changelog)

    def test_skill_directory_name_matches_frontmatter(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        match = re.search(r"^name:\s*([^\s]+)$", skill, flags=re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertEqual(SKILL_ROOT.name, match.group(1))

    def test_local_markdown_links_resolve(self):
        failures = []
        for document in REPO_ROOT.rglob("*.md"):
            if ".git" in document.parts:
                continue
            for raw_target in MARKDOWN_LINK.findall(document.read_text(encoding="utf-8")):
                target = unquote(raw_target.strip().strip("<>").split("#", 1)[0])
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (document.parent / target).resolve()
                if not resolved.exists():
                    failures.append(f"{document.relative_to(REPO_ROOT)} -> {raw_target}")
        self.assertEqual([], failures)

    def test_no_repository_file_exceeds_github_hard_limit(self):
        limit = 100 * 1024 * 1024
        oversized = []
        for path in REPO_ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            if path.stat().st_size >= limit:
                oversized.append(str(path.relative_to(REPO_ROOT)))
        self.assertEqual([], oversized)

    def test_release_archives_are_not_committed(self):
        archives = [
            str(path.relative_to(REPO_ROOT))
            for path in REPO_ROOT.rglob("*.zip")
            if ".git" not in path.parts
        ]
        self.assertEqual([], archives)

    def test_release_notes_exist_and_name_asset(self):
        notes = (REPO_ROOT / "RELEASE_NOTES.md").read_text(encoding="utf-8")
        self.assertIn("Team1 Design System 1.0.0", notes)
        self.assertIn("team1-design-system-v1.0.0.zip", notes)
        self.assertIn("private", notes.lower())

    def test_template_has_no_embedded_fonts_or_active_content(self):
        template = SKILL_ROOT / "templates" / "Team1 Design System.pptx"
        with zipfile.ZipFile(template) as archive:
            names = archive.namelist()
            self.assertFalse(any(name.startswith("ppt/fonts/") for name in names))
            self.assertFalse(any(name.endswith("vbaProject.bin") for name in names))
            presentation_xml = archive.read("ppt/presentation.xml")
            self.assertNotIn(b"embeddedFontLst", presentation_xml)
            for name in names:
                if name.endswith(".rels"):
                    self.assertNotIn(b'TargetMode="External"', archive.read(name))
            slides = [
                name
                for name in names
                if re.fullmatch(r"ppt/slides/slide[0-9]+\.xml", name)
            ]
            self.assertEqual(13, len(slides))


if __name__ == "__main__":
    unittest.main()
