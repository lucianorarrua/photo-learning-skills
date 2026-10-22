# Agreed experiments

Use this protocol whenever the agent will adjust, revise, or restore development
settings, including its turns in mixed operation. Keep the prediction/observation
cycle in the lesson; agreement grants a small experiment, not creative control.

## Bind and authorize

1. Discover the installed controls, types/ranges and mutation schemas. In 0.8.0
   candidates are `list_controls`, `set_develop`, and `run_command`; discover the
   actual undo/history route too. Availability is not proof of successful operation.
2. Bind the intended library, active ID and source to full development settings,
   relevant history/undo/redo and an inspected fresh baseline image. Use the
   shared [readiness gates](../../setup-photo-learning/references/readiness.md).
   Record snapshots locally with capture times; do not rely on an old lesson's
   values or a filename alone. Establish whether the route targets a photo ID or
   implicitly uses current selection.
3. Agree intent, prediction, operator, exact supported controls and a small bounded
   change (target or delta/range), then wait for agreement. An agreed group of
   small changes needs no separate slider confirmations. New controls, a wider
   change, a different photo, or a changed baseline that alters the prediction
   need a revised agreement. A preference for agent operation is not agreement
   on a specific experiment.

## Apply and observe

1. Immediately before mutation re-read library/photo identity, **full settings**
   and history/undo state against the agreed baseline. If changed, use the conflict
   table below before sending anything. Ask the learner to pause manual editing
   for this short agent turn. Polling has a read/write race; use conditional or
   revision-bound mutation if discovered. Without it, explain the limitation,
   minimize the gap and verify afterward rather than claiming atomic protection.
2. Send only the agreed controls, preferably one supported grouped call. Preserve
   unrelated settings; avoid resets or full-baseline replacement. Retain the
   before snapshot and exact successful/uncertain calls. If a call errors or times
   out, read current identity/settings/history before retrying: the operation may
   already have applied. A partly applied group is partial, not a reason for blind
   rollback. Stop and clarify any uncertain result.
3. Read back full settings and history, compare **all** differences, then obtain
   and actually inspect a fresh direct LightCraft image. Recheck identity/settings
   after rendering. A changed photo or unstable state invalidates attribution;
   repeat readiness or pause. A failed image leaves visual assessment pending,
   even if settings changed successfully. Do not keep adjusting to fix missing
   pixels. Record actual image route and limitations.
4. Return to the lesson's [Explain and Decide steps](../SKILL.md#3-run-a-controlled-experiment).
   For an agreed revision, establish a fresh baseline before mutation, keeping
   the same lesson when objective/photo still match.

## Restore without erasing learner work

An undo decision authorizes reversal of this experiment on its bound photo;
it does not authorize undoing the most recent unrelated action. Before restoration
repeat identity/full-settings/history checks, even when the decision was immediate.

| Current state | Action |
| --- | --- |
| Same bound photo, full settings match the agent result, and history/undo evidence proves its step is next | Use supported undo for that owned step, one checked step at a time if multiple calls were necessary; verify after each. Stop if the next step is not owned. |
| Same photo, unrelated controls changed after the experiment | Preserve those controls. Explain why global undo would reverse learner work; propose restoring only the experiment's controls to their captured pre-values. Obtain agreement to this compensating adjustment from the new baseline, then check/apply/read/render again. |
| An experiment control also changed, or current state/history is ambiguous | Show the conflict and ask whether to retain current values or agree a new target. Do not infer ownership from matching numbers or erase the learner's same-control change. |
| Settings match but undo ownership is unavailable or uncertain | Offer an explicitly agreed targeted compensation; matching settings alone cannot authorize global undo. |
| Library, photo ID or source changed | Send no mutation or undo. Preserve partial evidence; confirm the learner's current choice. Returning to the earlier photo requires their choice and fresh checks. Never switch back automatically. |

After undo/compensation, read full settings, retrieve and inspect the restored
image, then recheck identity/settings. Compare against the original baseline
when untouched, or the agreed merged target when preserving learner changes.
Report separately: development settings equality, preview appearance/byte equality
if measured, active history, undo and redo. Restored values or equal preview bytes
do not establish an identical history, discarded redo, decoder identity or color
fidelity. A compensating adjustment usually adds history; label it honestly.

## Scope and recovery

Export, sidecar/metadata writes, file overwrite/movement, selection changes and
comparison-view changes are separate operations needing their own explicit scope.
Do not bundle them into an editing experiment. Normal library edit journaling is
distinct from writing metadata beside an original or exporting an image.

At interruption save the operator/preference changes, agreement, before/last
verified settings, mutations, pending/uncertain results, learner evidence and
decision under the [context contract](../../setup-photo-learning/references/context.md#lesson-records).
After fresh-session recovery, treat these as history: refresh readiness and
re-establish agreement before mutation. Never replay a pending adjustment or undo
automatically. A request to stop ends work without requiring an explanation or
automatic restoration; record any unverified restoration as pending.
