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
        self.assertIn("actions/checkout@v7", text)
        self.assertIn("actions/setup-python@v7", text)

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
        self.assertEqual("2.0.0", manifest["version"])
        self.assertEqual("2026-08-12", manifest["released"])
        self.assertIn("2.0.0 — 2026-08-12", changelog)
        self.assertTrue(manifest["portable"])
        resources = manifest["canonicalResources"]
        for relative in resources.values():
            self.assertTrue((SKILL_ROOT / relative).is_file(), relative)

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
        self.assertIn("Team1 Design System 2.0.0", notes)
        self.assertIn("team1-design-system-v2.0.0.zip", notes)
        self.assertIn("private", notes.lower())
        self.assertIn("59/60", notes)
        evaluation = (REPO_ROOT / "docs" / "EVALUATION_2026-08-12.md").read_text(
            encoding="utf-8"
        )
        for value in (
            "59/60 (98.33%)",
            "3/3 PASS",
            "fe232b9484cc9c27115ed0671c6614c1daa2cda3b069192e4f35eb0ae3f747ff",
            "b3a76ce01c5752bf81b02fd994dfab0dae2edc157a4c56e38400c0dc1152c821",
            "9ab72aed9949895615600d224508506fc17eee000a69efa92e780ad6ce03b5fe",
        ):
            self.assertIn(value, evaluation)

    def test_current_brand_authority_and_retired_values_are_explicit(self):
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        authority = (SKILL_ROOT / "references" / "authority.md").read_text(
            encoding="utf-8"
        )
        combined = skill + authority
        self.assertIn("#E6212F", combined)
        self.assertIn("retired", combined.lower())
        self.assertIn("#FF394A", combined)
        self.assertIn("#E84142", combined)
        self.assertIn("9d1b3d1a9d9e3e254149885605504c6dfd84ec54", authority)

    def test_complete_current_global_tokens_exist(self):
        tokens = json.loads(
            (SKILL_ROOT / "tokens" / "design-tokens.json").read_text(encoding="utf-8")
        )
        serialized = json.dumps(tokens)
        for value in (
            "#E6212F",
            "#3055B3",
            "#058AFF",
            "#161617",
            "#F5F5F9",
            "#dc2626",
            "#16a34a",
            "#f59e0b",
            "#2563eb",
            "#9333ea",
            "Kanit Medium",
            "Kanit Light",
            "Aeonik",
            "640px",
            "1536px",
            "44px",
            "150ms",
            "400ms",
        ):
            self.assertIn(value, serialized)
        self.assertEqual("16px", tokens["global"]["radius"]["projectLogo"])
        self.assertEqual(
            "#E6212F", tokens["global"]["color"]["dark"]["textBrand"]["$value"]
        )
        self.assertEqual(
            "#FFFFFF",
            tokens["global"]["color"]["dark"]["textHighContrast"]["$value"],
        )
        self.assertEqual(
            "#E6212F", tokens["global"]["color"]["light"]["textBrand"]["$value"]
        )
        self.assertEqual(
            "#161617",
            tokens["global"]["color"]["light"]["textHighContrast"]["$value"],
        )

        css = (SKILL_ROOT / "tokens" / "design-tokens.css").read_text(
            encoding="utf-8"
        )
        for value in (
            "--team1-font-alternative",
            "--team1-space-0-5: 2px",
            "--team1-space-1-5: 6px",
            "--team1-space-3-5: 14px",
            "--team1-space-20: 80px",
            "--team1-radius-project-logo: 16px",
            "--team1-radius-pill: 9999px",
            "--team1-z-tooltip: 90",
            "--team1-breakpoint-2xl: 1536px",
            "--team1-motion-entrance: 400ms cubic-bezier(0.16, 1, 0.3, 1)",
            "--team1-heading-h1-desktop: 36px",
            "--team1-heading-h1-mobile: 30px",
            "--team1-body-size: 16px",
            "--team1-font-weight-heading: 500",
            "--team1-page-padding-desktop: 24px",
            "--team1-page-padding-mobile: 16px",
            "--team1-light-surface-hover: #d8d9dc",
            "--team1-light-shadow",
            "--team1-ava-blue-hover: #264496",
        ):
            self.assertIn(value, css)

    def test_required_v2_reference_modules_exist(self):
        required = (
            "references/authority.md",
            "references/identity.md",
            "references/digital-and-web.md",
            "references/presentations.md",
            "references/social-and-content.md",
            "references/events-print-and-merch.md",
            "references/regional-and-localization.md",
            "references/photography-and-video.md",
            "references/voice-and-copy.md",
            "references/governance-and-qa.md",
        )
        for relative in required:
            self.assertTrue((SKILL_ROOT / relative).is_file(), f"missing {relative}")

    def test_clean_room_handoff_contracts_are_explicit(self):
        web = (SKILL_ROOT / "references" / "digital-and-web.md").read_text(
            encoding="utf-8"
        )
        for value in (
            "#3055B3",
            "#058AFF",
            "Aeonik",
            "2, 4, 6, 8, 12, 14, 16, 20, 24, 32, 40, 48, 64, and 80 px",
            "red text on a dark surface",
            "monochrome",
            "square",
            "PFP",
            "physical mobile-device check",
        ):
            self.assertIn(value, web)
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("red text on a dark surface", skill)

        presentation = (
            SKILL_ROOT / "references" / "presentations.md"
        ).read_text(encoding="utf-8")
        for value in (
            "40 exemplar slides",
            "20 inherited layout parts",
            "active content",
            "external file relationships",
        ):
            self.assertIn(value, presentation)

        regional = (
            SKILL_ROOT / "references" / "regional-and-localization.md"
        ).read_text(encoding="utf-8")
        for value in (
            "approved Team1/country route",
            "Do not translate protected names or URLs",
            "Do not infer or claim chapter status",
        ):
            self.assertIn(value, regional)

    def test_official_logo_and_favicon_families_are_indexed(self):
        index = json.loads(
            (SKILL_ROOT / "assets" / "asset-index.json").read_text(encoding="utf-8")
        )
        paths = {asset["path"] for asset in index["assets"]}
        required = {
            "assets/identity/wordmark/Team1_MAIN_WHITE.svg",
            "assets/identity/wordmark/Team1_BLACK_MAIN.svg",
            "assets/identity/wordmark/Team1_WHITE_ALTERNATIVE.svg",
            "assets/identity/wordmark/Team1_BLACK_ALTERNATIVE.svg",
            "assets/identity/wordmark/Team1_RED_ALTERNATIVE.svg",
            "assets/identity/symbol/Team1_Symbol_Main.svg",
            "assets/identity/symbol/Team1_Symbol_Black_AvaRed.svg",
            "assets/identity/symbol/Team1_Symbol_Black.svg",
            "assets/identity/symbol/Team1_Symbol_White.svg",
            "assets/identity/symbol/Team1_Symbol_AvaRed.svg",
            "assets/identity/favicon/favicon.ico",
            "assets/identity/favicon/icon.png",
            "assets/identity/favicon/apple-icon.png",
        }
        self.assertTrue(required.issubset(paths), sorted(required - paths))

    def test_all_chapter_vectors_are_indexed_as_contextual(self):
        index = json.loads(
            (SKILL_ROOT / "assets" / "asset-index.json").read_text(encoding="utf-8")
        )
        by_path = {asset["path"]: asset for asset in index["assets"]}
        chapter_paths = {
            str(path.relative_to(SKILL_ROOT))
            for path in (SKILL_ROOT / "assets" / "chapters").rglob("*.svg")
        }
        self.assertEqual(16, len(chapter_paths))
        self.assertTrue(chapter_paths.issubset(by_path), sorted(chapter_paths - by_path.keys()))
        for path in chapter_paths:
            asset = by_path[path]
            self.assertNotEqual("global-current", asset["status"])
            combined = " ".join(
                str(asset.get(field, ""))
                for field in ("status", "authority", "rights", "role")
            ).lower()
            self.assertIn("chapter", combined)

    def test_portable_package_excludes_sensitive_and_stale_payloads(self):
        forbidden_directories = (
            "assets/photography",
            "assets/metrics",
            "assets/icons",
            "assets/backgrounds",
            "assets/graphics",
            "assets/logos",
        )
        for relative in forbidden_directories:
            self.assertFalse((SKILL_ROOT / relative).exists(), f"unexpected {relative}")

        forbidden_suffixes = {".ttf", ".otf", ".woff", ".woff2", ".mp3", ".wav", ".mp4", ".mov"}
        offenders = [
            str(path.relative_to(SKILL_ROOT))
            for path in SKILL_ROOT.rglob("*")
            if path.is_file() and path.suffix.lower() in forbidden_suffixes
        ]
        self.assertEqual([], offenders)

    def test_current_template_pdf_page_count(self):
        pdf = SKILL_ROOT / "templates" / "Team1 Current Presentation Template.pdf"
        data = pdf.read_bytes()
        self.assertTrue(data.startswith(b"%PDF-"))
        self.assertEqual(40, len(re.findall(rb"/Type\s*/Page\b", data)))
        for forbidden in (
            b"/FontFile",
            b"/JavaScript",
            b"/OpenAction",
            b"/EmbeddedFile",
            b"/Launch",
            b"/URI",
        ):
            self.assertNotIn(forbidden, data)

    def test_current_master_contact_sheet_is_packaged(self):
        preview = (
            SKILL_ROOT
            / "previews"
            / "current-presentation-master-contact-sheet.png"
        )
        self.assertTrue(preview.is_file())
        self.assertGreater(preview.stat().st_size, 100_000)
        self.assertFalse(
            (SKILL_ROOT / "previews" / "current-presentation-master.webp").exists()
        )

        root_readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        package_readme = (SKILL_ROOT / "README.md").read_text(encoding="utf-8")
        for text in (root_readme, package_readme):
            self.assertIn("current-presentation-master-contact-sheet.png", text)

    def test_templates_have_no_embedded_fonts_or_active_content(self):
        forbidden_legacy = (
            SKILL_ROOT / "templates" / "Team1 Legacy Overview Reference.pptx"
        )
        self.assertFalse(forbidden_legacy.exists())
        self.assertFalse(forbidden_legacy.with_suffix(".pdf").exists())

        expected_slides = {"Team1 Current Presentation Template.pptx": (40, 20)}
        for filename, (expected_count, expected_layouts) in expected_slides.items():
            template = SKILL_ROOT / "templates" / filename
            with self.subTest(template=filename), zipfile.ZipFile(template) as archive:
                names = archive.namelist()
                self.assertFalse(any(name.startswith("ppt/fonts/") for name in names))
                self.assertFalse(any(name.endswith("vbaProject.bin") for name in names))
                self.assertFalse(any("activeX" in name for name in names))
                self.assertFalse(any("embeddings" in name for name in names))
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
                self.assertEqual(expected_count, len(slides))
                layouts = [
                    name
                    for name in names
                    if re.fullmatch(
                        r"ppt/slideLayouts/slideLayout[0-9]+\.xml", name
                    )
                ]
                self.assertEqual(expected_layouts, len(layouts))

    def test_pptx_templates_contain_no_personal_metadata(self):
        forbidden_fields = (
            b"<dc:creator>",
            b"<cp:lastModifiedBy>",
        )
        for template in (SKILL_ROOT / "templates").glob("*.pptx"):
            with self.subTest(template=template.name), zipfile.ZipFile(template) as archive:
                core = archive.read("docProps/core.xml")
                for field in forbidden_fields:
                    if field in core:
                        value = core.split(field, 1)[1].split(b"<", 1)[0].strip()
                        self.assertIn(
                            value,
                            (b"", b"Team1 Design System", b"Walnut Exporter"),
                        )


if __name__ == "__main__":
    unittest.main()
