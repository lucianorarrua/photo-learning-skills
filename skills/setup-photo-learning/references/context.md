# Collection learning context contract

Paths are relative to the confirmed photo collection root, independently of
installed skills. Each collection owns `.photo-learning/` by default. Resolve the
absolute root and the actual context destination before accessing records. An
existing profile's confirmed association with that root can establish the choice;
ask when missing or contradictory rather than reconfirming unchanged facts each
session. Chat memory and the installed skill's directory do not choose a collection.
For a linked context, setup revisit, skill update, or changed photo location, read
[continuity.md](continuity.md) for destination and reconciliation rules.

## Storage and ownership

| File | Read | Write |
| --- | --- | --- |
| `profile.md` | Setup and lessons, first | Setup after learner confirmation; learner may edit directly |
| `progress.md` | Setup and lessons, if present | Lessons: evidence, assistance, unproven points, next practice |
| `readiness.md` | Setup and lessons as historical evidence | Setup or a fresh readiness check; update previous gate results |
| `sessions/<unique-id>.md` | Only relevant details | Lessons; timestamp/topic plus suffix on collision |
| `pending-progress.md` | If present, after profile/progress | Temporary record links awaiting evidence/reference reconciliation |
| `topics/` | Only when relevant | Optional, lazy lesson notes |

Installed skills are reusable instructions, never personal storage. Updates
leave `.photo-learning/` untouched. Setup creates only `profile.md` and
`readiness.md`; absent progress means no recorded demonstration, not a proficiency
rating. Preserve existing progress and sessions. Lessons use the record procedure
below; setup does not manufacture learning evidence.

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

## Lesson records

Use Markdown, not a database or a full transcript. The profile remains owned by
setup and the learner: lesson evidence belongs in progress and sessions. Ask setup
to reconcile a changed preference rather than overwriting unrelated profile facts.

### Compact progress: `progress.md`

Use one heading per learning objective and concise lesson bullets beneath it:

```markdown
# Learning progress
## Explain exposure's effect on subject/background balance
- Lesson: lesson-20261021T140000Z-a; photo: fixture-a.png (library ID 12).
- Evidence: recognized brighter background; explained lost silhouette emphasis
  after the region-comparison prompt. Self-report remains in profile, not evidence.
- Assistance: region-comparison prompt; no independent transfer observed.
- Unproven: predicting the competing effect on another photo.
- Outcome: demonstrated for this experiment with prompting.
- Next practice: predict subject/background trade-off on a different current photo.
- Record: sessions/20261021T140000Z-a.md; updated: 2026-10-21T14:10:00Z.
```

The example is fictional. Keep evidence/assistance/unproven/next practice plus
stable lesson and record references. Use `pending`, `interrupted`, or `demonstrated
for this experiment` with scope and assistance, not numeric grades or global
proficiency labels. Retain separate lessons on different photos under the same
objective. Merge repeated observations of the same lesson/outcome instead of
appending duplicate progress. Keep each lesson bullet compact; details stay in
sessions. Older entries may be compressed to a short evidence/remaining-practice
summary with record links, preserving distinct evidence and unresolved work.
When another session adds evidence to the same lesson, summarize the development
and retain links to each supporting session (for example, earlier prompted
recognition followed by a later independent explanation). The latest sample does
not erase earlier assistance or turn it into independent evidence. A correction
amends its existing sample; a new observed encounter gets a new session reference.

### Detailed session: `sessions/<unique-id>.md`

Create only when there is session evidence or an interruption to preserve. Include:

- **Session ID and date:** stable timestamp plus suffix if needed; never date alone.
- **Lesson ID and objective:** stable objective/photo identity, independent of the
  session ID; a continued lesson keeps its ID across sessions. If a session covers
  several lessons, use a separate lesson section for each with its own photo,
  experiment, evidence, assistance, outcome and next practice. Preserve earlier
  sections when a later lesson closes in the same session.
- **Photo reference and intent:** library identity, active ID and source/path when
  available, creative intent. Mark moved/unavailable references without deleting
  learning evidence. Do not embed originals or previews.
- **Experiment:** prediction, before/after settings or local snapshot references,
  changed controls, relevant capture times and image route/inspection, learner's
  retain/revise/undo decision. Mark unperformed steps explicitly.
- **Operation and recovery:** preference and revisions (session-only or saved),
  operator per turn, agreed scope, last verified identity/settings and any pending
  or uncertain mutation. Capture intervening changes and the clarification used.
  For restoration distinguish undo from targeted compensation, settings/preview
  verification from history/redo state. Fresh recovery refreshes readiness and
  agreement; a saved pending operation is never an instruction to replay it.
- **Learner evidence:** specific observation and explanation in their own words
  (short quotation or faithful paraphrase); distinguish self-report, tutor
  explanation, and learner demonstration.
- **Assistance:** prompts, hints, smaller steps, or direct explanations actually
  supplied; distinguish independent from assisted answers.
- **Outcome and unresolved understanding:** what this experiment supports and what
  is pending; an interrupted lesson can include partial recognition without a
  demonstrated explanation.
- **Next practice:** actionable exercise, usable on a different current photo.

### Read/write procedure

1. Start with profile and compact progress, then read `pending-progress.md` if
   present. This small index contains session paths/IDs and lesson IDs awaiting
   a compact-progress update, or a verified-move reference-repair note, not a history
   copy. For each pending link, read that
   named session and reconcile its entry using the existing IDs; an already matching
   entry needs no duplicate. Report a missing referenced record without inventing
   its evidence. Otherwise retrieve only the record linked to relevant evidence,
   an unresolved point, a correction, or a chosen continuation.
   A missing old photo or record does not block a new lesson; retain the available
   evidence and report the missing detail if needed.
   A verified-move note uses the continuity workflow to repair references, never
   to replay the file operation; clear it only after checking the repaired links.
2. At closure/interruption apply the privacy gate, then re-read the destination
   records before narrow edits. Check for existing session/lesson IDs to preserve
   manual notes and avoid duplicate writes. A second session on the same day gets
   a different timestamp/suffix; test destination existence and choose another
   suffix rather than overwriting. A retry within the same session updates that
   session's existing record.
3. Before the evidence writes, re-read and add the chosen session path/ID and lesson
   IDs to `pending-progress.md`, preserving other pending links. If this index
   cannot be written, report the blockage and keep the proposed evidence in chat.
   Write the session first, then update only its relevant progress entry, linking
   the saved record. Read both back to verify evidence and links; only then remove
   its pending-index entry, preserving other entries (an empty index may be removed).
   If only the session saved, report partial persistence: a fresh invocation can
   find its index link and repair progress without creating another outcome. These
   are ordinary file writes, not a concurrent multi-writer or abrupt-process
   recovery guarantee.
4. Summarize saved evidence, assistance, unresolved understanding, and next practice
   for correction. On correction, re-read and amend both the affected session and
   compact entry; distinguish a learner correction from newly observed evidence.
   Preserve unrelated content and earlier session records. If storage is blocked,
   give the unsaved note in chat and report that recovery is not yet available.
