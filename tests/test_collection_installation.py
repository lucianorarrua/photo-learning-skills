"""Exercise installed skill discovery through the real OpenCode CLI."""

import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "skills"
SKILLS = ("setup-photo-learning", "photo-learning")


class CollectionInstallationTest(unittest.TestCase):
    @unittest.skipUnless(shutil.which("opencode"), "OpenCode CLI is required")
    def test_non_git_collection_discovers_complete_local_skill(self):
        with tempfile.TemporaryDirectory(prefix="photo-learning-") as directory:
            root = Path(directory)
            destination = root / ".agents/skills"
            for name in SKILLS:
                shutil.copytree(SOURCE / name, destination / name)
            # A regular file also avoids CLI exit truncating a large piped catalog.
            with tempfile.TemporaryFile(mode="w+") as catalog:
                subprocess.run(
                    ["opencode", "debug", "skill"],
                    cwd=root,
                    stdout=catalog,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=60,
                    check=True,
                )
                catalog.seek(0)
                skills = json.load(catalog)
            for name in SKILLS:
                matches = [s for s in skills if s["name"] == name]
                self.assertEqual(len(matches), 1)
                self.assertEqual(Path(matches[0]["location"]), destination / name / "SKILL.md")
            self.assertFalse((root / ".git").exists())
            self.assertFalse((root / ".photo-learning").exists())
            # The installed body must be self-contained, not tied to the checkout.
            for document in destination.rglob("*.md"):
                for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", document.read_text()):
                    if "://" not in link:
                        self.assertTrue((document.parent / link).is_file(), link)

    def test_updating_installed_skills_preserves_learning_context(self):
        with tempfile.TemporaryDirectory(prefix="photo-learning-update-") as directory:
            root = Path(directory)
            context = root / ".photo-learning"
            shutil.copytree(Path(__file__).parent / "fixtures/learning-context", context)
            before = {p.relative_to(context): p.read_bytes() for p in context.rglob("*.md")}
            for name in SKILLS:
                destination = root / ".agents/skills" / name
                shutil.copytree(SOURCE / name, destination)
                # Execute the documented replacement boundary, including stale content.
                (destination / "obsolete.md").write_text("Previous installed instructions\n")
                shutil.rmtree(destination)
                shutil.copytree(SOURCE / name, destination)
                self.assertFalse((destination / "obsolete.md").exists())
            after = {p.relative_to(context): p.read_bytes() for p in context.rglob("*.md")}
            self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
