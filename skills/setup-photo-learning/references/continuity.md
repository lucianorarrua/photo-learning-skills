# Context continuity

Use with the [context contract](context.md). These workflows change local records,
not the learner's photo organization as a side effect of setup or a lesson.

## Resolve one complete context

1. Start at the current collection root. Resolve `.photo-learning` including an
   existing symbolic link to its complete target. Check whether the target exists
   and is accessible; inspect the profile's recorded collection associations and
   any explicit sharing confirmation. A new root/link needs confirmation of the
   root, target and whole-context sharing before personal reads/writes. Explain
   that preferences, progress, readiness and all session/topic records are shared.
2. Reuse the confirmed target for every record, including pending-progress and
   relative session links. Resolve record links from the context, not the installed
   skill or current photo directory. Preserve associations for other collections
   in a shared profile; add the newly confirmed root rather than replacing the
   original root. Scope technical readiness to the collection/library checked.
3. On an inaccessible/dangling link or contradictory destination, report the path
   and ask the learner to restore access or resolve the choice. Keep proposed
   changes in chat. Do not initialize a competing local context, replace the link,
   or fall back to another collection or private client memory.

Two independently initialized roots stay independent. Sharing a complete context
is explicit; it is not implied by identical camera models, photo filenames,
installed skills, or neighboring directories. Creating a link is optional. If
requested, inspect both source and destination first; preserve an occupied context
and ask how to resolve it before linking or migrating anything. Apply the privacy
gate to the link location and target before writes. This is ordinary shared-file
access, not synchronization, partial sharing, or a concurrent-writer guarantee.

## Revisit setup

Apply setup's [profile confirmation and persistence steps](../SKILL.md#2-confirm-a-minimal-profile)
using the context contract's fact statuses and source/date for requested corrections.
The learner's approval of those exact facts authorizes that profile change; do not
ask the same approval again. Clarify only unresolved contradictions.

A changed preference is not a demonstration or a reason to reset progress. Label
confirmed corrections as corrections, retaining the basis of any inference still
awaiting confirmation. Read back the changed facts after saving.

## Update reusable skills

Replace only the installed instruction folders, including their references. Keep
both sibling skills together so lesson pointers still resolve. Preserve all
personal context, unrelated skills, client settings and original photos. Resolve
the actual installation path before replacement, especially if it is a symlink;
do not overwrite an unintended target. Check the client's discovery results after
restart and confirm they point to this collection's intended installation.

In a fresh conversation invoke the installed skill, resolve the collection again,
and read profile/compact progress plus the pending index if present. Updating
instructions neither migrates personal records nor refreshes desktop readiness.
Load detailed sessions/topics only for relevant uncertainty, correction or chosen
continuation. Use the context contract's pending-index reconciliation for partial
writes; a second invocation of an already saved outcome does not add a second copy.

## Changed or unavailable photos

A photo reference describes the photo used for past learning, not a requirement to
reopen it. Retain the lesson/session IDs, observations, assistance and unresolved
points when a source is moved, deleted or offline. Distinguish its **recorded path
at the time** from any **currently verified location**, noting source/date for a
relocation or unavailability report. A learner-reported move is confirmed as a
report; it is not a tool-verified current file or LightCraft-library mapping.

Start new practice on the current photo using compact progress and fresh readiness.
Only locate an old photo when the current task needs it; ask for a relevant path or
perform a bounded lookup rather than scanning the collection by default. A missing
original does not invalidate past learning evidence, and a missing detail record
does not justify inventing its contents. Photo IDs are library-scoped; a matching
basename or ID in another library does not establish identity.

## Explicit file organization requests

A clear request to move or organize files remains a general agent task. Follow its
scope directly; do not require a lesson or repeat approval already given. Resolve
actual ambiguity, overwrite conflicts or missing access as needed. Setup or lesson
entry alone authorizes no reorganization.

For an agent-performed move, inspect relevant learning references to the affected
photo, perform only the requested operation, and verify its result. Narrowly
reconcile affected compact/session/topic references with a dated old-to-new mapping,
preserving the recorded experiment path and stable IDs. Retrieve detail here only
as needed for that reconciliation. A filesystem move alone does not prove LightCraft
updated its library mapping; verify that separately when relevant. If a move partly
succeeds or reference writes fail, report exactly what moved and what remains stale,
retaining a small note in `pending-progress.md` when writable: verified old-to-new
mapping/date, affected record paths and lesson IDs, and the remaining reference
repair. Apply the privacy gate before these personal writes. Recovery repairs
references; it never repeats a move just because the note exists.
