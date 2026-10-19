# Collection learning context contract

Paths are relative to the confirmed photo collection root, independently of
installed skills. Each collection owns `.photo-learning/` by default. Resolve
an existing symlink to its complete context and confirm the shared destination
before reading/writing. Creating a link is optional, requires informed agreement,
and must preserve an existing destination.
Stop on a dangling link or ambiguous destination instead of creating another context.

## Storage and ownership

| File | Read | Write |
| --- | --- | --- |
| `profile.md` | Setup and lessons, first | Setup after learner confirmation; learner may edit directly |
| `progress.md` | Setup and lessons, if present | Lessons: evidence, assistance, unproven points, next practice |
| `readiness.md` | Setup and lessons as historical evidence | Setup or a fresh readiness check; update previous gate results |
| `sessions/<unique-id>.md` | Only relevant details | Lessons; timestamp/topic plus suffix on collision |
| `topics/` | Only when relevant | Optional, lazy lesson notes |

Installed skills are reusable instructions, never personal storage. Updates
leave `.photo-learning/` untouched. Setup creates only `profile.md` and
`readiness.md`; absent progress means no recorded demonstration, not a proficiency
rating. Preserve existing progress and sessions. Lesson record formats are outside
this setup milestone.

Label facts **confirmed** (learner statement or named tool result with date),
**unknown**, or **inferred** (basis stated, awaiting confirmation). Keep self-report
separate from observed learning evidence. The learner can correct either.
Environment observations expire: reverify readiness for the current session/photo.

## Privacy gate before personal writes

1. Detect whether the collection is inside a Git worktree, including a nested
   collection. Git is optional; other collections need no initialization.
2. Establish exclusions for `.photo-learning` (including a symlink), transient
   previews/exports, and actual photo locations. Prefer local `info/exclude` for
   personal exclusions. Find it with `git rev-parse --git-path info/exclude` to
   support worktrees; append without replacing rules. Anchor patterns relative
   to the Git root. Directory-only rules do not cover symlinks.
3. Verify representative destinations using `git check-ignore -v -- <paths>`
   and check already tracked material with `git ls-files -- <paths>`. Ignore
   rules cannot protect tracked files. Report tracked personal destinations and
   resolve storage with the learner before writing; never silently untrack them.
4. Check a shared context target's worktree too. If protection cannot be verified,
   keep proposals in chat until resolved. Do not commit originals, previews,
   exports, personal records, or equipment details to this public project.

Choose photo exclusions from the actual layout: RAW extensions alone miss JPEG
originals and unusual formats. Avoid hiding unrelated project files. Transient
images belong outside the public repository or in explicitly excluded storage
such as `.photo-learning/previews/`. Public examples use fictional data.

## Readiness record

Use concise human-readable Markdown with these sections:

- **Checked at**: timestamp and collection/context location (local only).
- **Environment**: OS, application and CLI/server versions, client version,
  selected provider/model identifier. Unavailable versions remain unknown.
- **Connection**: native MCP or shell-mediated, endpoint, reported backend,
  expected library and identity evidence. No credentials.
- **Photo and state**: active ID/source, captured full development settings or
  local snapshot reference, read/render times, final identity/settings recheck.
- **Image route**: attempted supported routes/outcomes, successful tool or
  attachment, actual model inspection, learner-visible location/confirmation.
- **Gates**: control, intended library/photo, settings, fresh render, model
  inspection, learner visibility; each pass/pending/blocked with evidence.
- **Outcome and next step**: ready only when all gates pass; otherwise the real
  blocker and next action. Note any unverified native route separately.

Save large settings snapshots locally, preserving enough state to identify the
render. Re-read before updates and preserve unrelated learner notes. Summarize
saved changes; avoid full transcripts, numeric grades, and global proficiency labels.
