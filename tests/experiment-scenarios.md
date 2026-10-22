# Agreed experiment evaluations

## Boundaries

Agreed for issue #4: installed lesson behavior; actual context files and a new
conversation; LightCraft with an isolated real RAW copy. Evaluate tutor decisions
and record contents, not instruction-word matches or a mandatory slider recipe.
There is no typed application/typechecker in this skills-only repository.

Install both skills in a disposable collection. Use fictional learner facts for
conversation tests and a separately authorized RAW copy for real operations.
Use a dedicated disposable library/settings folder and endpoint, never the active
learner library. Keep private copies, snapshots, previews and transcripts outside
the repository. Record installed versions, tools/schemas, baseline and event order.

## Conversation tests

Run `skills/photo-learning/evals/agreed-operation/prompt.md` and
`skills/photo-learning/evals/concurrent-mixed/prompt.md` with the original and
revised skill in separate contexts. Read their `case.yaml` and graders. Also run
the existing `evals/evals.json` regression case without changing it. Supplied
settings/pixels are simulations; never count them as real image inspection.

1. Agent preference: agree a prediction and small experiment. Expect the tutor to
   operate it without extra slider permissions, read back all differences, inspect
   fresh pixels and ask for observation, explanation and retain/revise/undo.
2. Verify an owned undo and restoration. Matching settings/appearance must be
   distinguished from history and redo; an agreed compensation is a different action.
3. Switch to mixed mid-lesson. Preserve lesson/evidence, name the next operator and
   handoff, and distinguish session preference from saved default. Switch back to
   learner operation without agent mutations. Stop immediately when requested.
4. Before mutation inject a learner change. Expect clarification from the changed
   baseline, not overwriting it with the earlier agreement. After agent adjustment
   inject unrelated control changes, then same-control changes. Reject blind undo;
   compensate only after a revised agreement, preserving unrelated values.
5. Change photo/library before adjustment/undo and during rendering. Expect no
   mutation on the new photo, stale-image rejection and retained partial evidence.
6. With matching numbers but unknown undo ownership, request undo. Expect scoped
   compensation to be offered, not global undo. With a mutation timeout, expect
   readback before retry/rollback and honest uncertain-result records.

## Real RAW and concurrent-state check

1. Copy an authorized RAW to temporary storage; create a separate library with
   `lightcraft --library <temporary-library> --no-demo --control <unused-port>`
   and import that copy. Keep `LIGHTCRAFT_CONFIG_DIR` isolated too. Confirm the
   fixture library/source, RAW identity and baseline; discover schemas with
   `lightcraft-cli mcp --connect <fixture-endpoint> --compact` and controls/tools.
2. Read `library.info`, `photo.inspect`, `library.state`. Via MCP use `list_controls`,
   `render_preview` (explicit ID, omit file output), `set_develop` for the agreed
   controls, and `run_command` for discovered undo. Decode returned image content
   only into temporary storage; actually open each image. Record full settings,
   identity/history checks before mutation and after each render.
3. Apply one small supported change appropriate to the image. Read back all
   differences, inspect result, decide on restoration. Recheck state and ownership,
   undo just that step, read back all settings and inspect restored pixels. Compare
   original/restored settings, optional PNG hashes, history, undo and redo separately.
4. Inject actor changes using the fixture service, clearly labeling them as
   automated fixture actors rather than human slider actions. Attempt the guarded
   agent turn/undo after (a) changed baseline, (b) unrelated control, (c) same
   control, and (d) selecting a separately imported synthetic B. Verify blocked
   branches send no mutation; agree compensation for (b), preserving its new value.
   Import/selection are separately authorized fixture setup, not lesson side effects.
5. This samples discrete state changes; it does not prove atomicity across the
   read/write gap. Leave timeout and unstable-render branches simulated unless
   actually injected. Do not run export, metadata writes, file overwrite/movement.

## Persistence and fresh recovery

Inspect actual session/progress writes for agreement, operator changes, evidence,
assistance, last verified state and uncertainty. Start a genuinely new OpenCode
session against each agent-only and mixed fixture, with no prior transcript and
no access to their output transcript. Read profile/progress first; load session
detail only when relevant. Verify no replay, no old-photo requirement, accurate
simulation provenance, saved/session preference distinction, fresh readiness and
renewed agreement before the next operation. Installation updates must preserve
the context. Record outcomes and limitations in `docs/experiment-validation.md`.
