"""Exercise installed skill discovery through the real OpenCode CLI."""

import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "skills/setup-photo-learning"


@unittest.skipUnless(shutil.which("opencode"), "OpenCode CLI is required")
class CollectionInstallationTest(unittest.TestCase):
    def test_non_git_collection_discovers_complete_local_skill(self):
        with tempfile.TemporaryDirectory(prefix="photo-learning-") as directory:
            root = Path(directory)
            destination = root / ".agents/skills/setup-photo-learning"
            shutil.copytree(SOURCE, destination)
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
            matches = [s for s in skills if s["name"] == "setup-photo-learning"]
            self.assertEqual(len(matches), 1)
            self.assertEqual(Path(matches[0]["location"]), destination / "SKILL.md")
            self.assertFalse((root / ".git").exists())
            self.assertFalse((root / ".photo-learning").exists())
            # The installed body must be self-contained, not tied to the checkout.
            for document in destination.rglob("*.md"):
                for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", document.read_text()):
                    if "://" not in link:
                        self.assertTrue((document.parent / link).is_file(), link)


if __name__ == "__main__":
    unittest.main()
