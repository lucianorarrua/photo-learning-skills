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
    def discover_skills(self, root):
        # A regular file avoids CLI exit truncating a large piped catalog.
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
            return json.load(catalog)

    def assert_local_skills(self, root):
        skills = self.discover_skills(root)
        for name in SKILLS:
            matches = [s for s in skills if s["name"] == name]
            self.assertEqual(len(matches), 1)
            self.assertEqual(
                Path(matches[0]["location"]), root / ".agents/skills" / name / "SKILL.md"
            )

    def snapshot_context(self, context):
        return {p.relative_to(context): p.read_bytes()
                for p in context.rglob("*") if p.is_file()}

    @unittest.skipUnless(shutil.which("opencode"), "OpenCode CLI is required")
    def test_non_git_collection_discovers_complete_local_skill(self):
        with tempfile.TemporaryDirectory(prefix="photo-learning-") as directory:
            root = Path(directory)
            destination = root / ".agents/skills"
            for name in SKILLS:
                shutil.copytree(SOURCE / name, destination / name)
            self.assert_local_skills(root)
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
            before = self.snapshot_context(context)
            for name in SKILLS:
                destination = root / ".agents/skills" / name
                shutil.copytree(SOURCE / name, destination)
                # Execute the documented replacement boundary, including stale content.
                (destination / "obsolete.md").write_text("Previous installed instructions\n")
                shutil.rmtree(destination)
                shutil.copytree(SOURCE / name, destination)
                self.assertFalse((destination / "obsolete.md").exists())
            after = self.snapshot_context(context)
            self.assertEqual(before, after)

    @unittest.skipUnless(shutil.which("opencode"), "OpenCode CLI is required")
    def test_fresh_discovery_after_update_keeps_collection_and_shared_target(self):
        with tempfile.TemporaryDirectory(prefix="photo-learning-roots-") as directory:
            roots = [Path(directory) / name for name in ("A", "B", "C")]
            a, b, c = roots
            fixture = Path(__file__).parent / "fixtures/learning-context"
            for root in (a, b):
                shutil.copytree(fixture, root / ".photo-learning")
            with (b / ".photo-learning/profile.md").open("a") as profile:
                profile.write("\nIndependent collection B: French.\n")
            c.mkdir()
            shared = c / ".photo-learning"
            shared.symlink_to(a / ".photo-learning", target_is_directory=True)
            before = {
                root.name: self.snapshot_context(root / ".photo-learning")
                for root in roots
            }
            for root in roots:
                destination = root / ".agents/skills"
                for name in SKILLS:
                    installed = destination / name
                    shutil.copytree(SOURCE / name, installed)
                    (installed / "SKILL.md").write_text("Obsolete instruction fixture\n")
                    shutil.rmtree(installed)
                    shutil.copytree(SOURCE / name, installed)
                self.assert_local_skills(root)
                for name in SKILLS:
                    self.assertEqual((destination / name / "SKILL.md").read_bytes(),
                                     (SOURCE / name / "SKILL.md").read_bytes())
                after = self.snapshot_context(root / ".photo-learning")
                self.assertEqual(before[root.name], after)
                self.assertFalse((root / ".git").exists())
            self.assertTrue(shared.is_symlink())
            self.assertEqual(shared.resolve(), a / ".photo-learning")
            self.assertNotEqual(before["A"], before["B"])


if __name__ == "__main__":
    unittest.main()
