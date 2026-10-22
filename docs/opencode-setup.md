# OpenCode: collection-local setup

This journey supplies `setup-photo-learning` and `photo-learning`. Choose an
image-capable model. See [setup evidence](setup-validation.md) and
[lesson evidence](lesson-validation.md) for tested boundaries and limits.

## Install in an existing collection

Keep the repository checkout separate from the collection. From the collection
root, substituting the checkout path, check that the destination does not already
exist and run:

```bash
mkdir -p .agents/skills
cp -R /path/to/photo-learning-skills/skills/setup-photo-learning .agents/skills/
cp -R /path/to/photo-learning-skills/skills/photo-learning .agents/skills/
```

Install both complete sibling folders: the lesson reads setup's shared references.
To update, replace only these two `.agents/skills/` folders from the new
checkout. Preserve other skills and `.photo-learning/`. No Git initialization,
photo moves, or global installation is required. Open OpenCode from the collection
root, avoiding nested-directory discovery ambiguity in a non-Git collection.

Quit and restart OpenCode after installing skills or changing configuration:

```bash
opencode --version
opencode debug skill
```

Find both skills with locations inside this collection. If your version
does not discover shared `.agents/skills/`, copy both complete sibling folders into
`.opencode/skills/` instead and remove the duplicate installation. Check skill
permissions and global name conflicts if absent.

Ask **“Load the setup-photo-learning skill and set up learning in this collection.”**
The agent should call `skill` with that name. Versions supporting `opencode/slash`
metadata also expose `/setup-photo-learning`; the explicit request is portable.
No root `AGENTS.md` adapter is needed in the tested version.

After setup, ask **“Load photo-learning and help me practice one objective on my
current photo. I will operate the controls.”** `/photo-learning` is also available
where slash metadata is supported. You can operate the controls, ask the agent to
execute an agreed small experiment, or take mixed turns. The tutor names the next
operator, checks current state before agent changes, then asks for observations,
explanations and your decision. Change the operation preference during a lesson
without losing progress. See [experiment validation](experiment-validation.md)
for tested behavior and the limits of polling-based concurrent-change protection.

At closure or interruption, the lesson writes `.photo-learning/progress.md` and a
unique Markdown record under `.photo-learning/sessions/`. It summarizes the saved
evidence and prompting so you can correct them. In a fresh conversation ask to
practice on the current photo: the tutor recovers profile and compact progress,
refreshes readiness, and opens detailed records only when relevant. Another photo
starts a separate lesson even when the objective recurs. You can stop at any time.

## Connect the running desktop

Use matching installed application/CLI versions. If control is absent, decide when
to close LightCraft normally and reopen the intended library, for example:

```bash
lightcraft --library "/path/to/intended/library" --control 7980
```

Do not run blindly against another open library. The agent explains missing access
and waits for your action rather than restarting anything.

In 0.8.0 the control channel is enabled by `--control PORT` or the
`LIGHTCRAFT_CONTROL_PORT` environment variable. A normal launcher entry without
either can open the editor successfully while leaving integration unavailable.
To keep using the launcher, add `--control 7980` to the user-local launcher entry's
existing command, preserving its executable, library arguments and file placeholders.
Quit normally and relaunch for that change to take effect. Setup does not edit
launcher configuration automatically. Keep the control connection on loopback.

For native MCP registration, merge this example into collection-local
`opencode.json`, preserving existing fields and substituting the absolute CLI path:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "lightcraft": {
      "type": "local",
      "command": ["/absolute/path/lightcraft-cli", "mcp", "--connect", "127.0.0.1:7980"],
      "enabled": true
    }
  }
}
```

Restart OpenCode, run `opencode mcp list`, then ask setup to inspect the intended
library, photo/settings and preview. A connected listing certifies neither desktop
identity nor native image delivery. Follow the shared
[readiness procedure](../skills/setup-photo-learning/references/readiness.md).
Headless `--demo` cannot replace this desktop check.

Supported shell-mediated read-only inspection can use:

```bash
lightcraft-cli run --connect 127.0.0.1:7980 library.info library.state photo.inspect develop.get
```

For images, use discovered MCP `render_preview`/`render_photo` and an image-capable
reader of decoded content. CLI JSON is not image inspection. Try available
supported read-only routes before attachment fallback; label the actual route.

## Personal records

Setup confirms language, intent, and revisable operation preference before saving
`.photo-learning/profile.md`. Equipment/time/experience can remain unknown.
`.photo-learning/readiness.md` separately records dated technical evidence; it
creates no learning evidence. Edit the profile or revisit setup to correct it.

In a Git collection verify exclusions before personal writes. For a collection
that is also the Git root, example local `info/exclude` additions are:

```gitignore
/.photo-learning
/Originals/
/Exports/
```

Adapt photo/export locations and preserve rules. For nested collections, shared
contexts, tracked files, and verification follow the
[privacy gate](../skills/setup-photo-learning/references/context.md#privacy-gate-before-personal-writes).
Ignore rules cannot remove tracked files. Keep private material outside the public
project; public evaluation profiles are fictional.

## References

- [OpenCode skills](https://opencode.ai/docs/skills/)
- [OpenCode MCP](https://opencode.ai/docs/mcp-servers/)
- [LightCraft 0.8.0 MCP](https://github.com/storytold/lightcraft/blob/v0.8.0/docs/mcp.md)
