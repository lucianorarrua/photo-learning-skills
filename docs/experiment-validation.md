# Agreed experiment validation: issue #4

## Environment and provenance

Executed during the 2026-10-21 session (UTC logs continue into 2026-10-22), Linux,
OpenCode **1.18.35**, model **openai/gpt-6.1-sol**, LightCraft application/CLI
**0.8.0**. Shell-mediated MCP used protocol **2025-06-18**, connecting to a
separate desktop on **127.0.0.1:7981**, with isolated library and configuration.
Native MCP registration/image delivery was not exercised by this run.

The authorized real NEF was copied into temporary storage. Its original and the
learner's existing desktop library were not used for mutations. The fixture was
reported as RAW/NEF, 6016 × 4016. Private source details, copies, images and logs
remain outside the repository. Public evaluation prompts describe fictional data.
This is behavioral/technical evidence, not a claim that a real learner demonstrated
new understanding in the fixture run.

## Observed checks

| Boundary | Executed outcome |
| --- | --- |
| Red before implementation | Original skill rejected an authorized agent adjustment and undo, requiring learner operation; first operation-cycle criterion failed |
| Discovery | Installed MCP initialization, tool schemas and `list_controls` succeeded. `set_develop` uses `values`; `render_preview` used explicit ID, `max_side: 1024`, `format: png`; `run_command` reached library/photo/state and `edit.undo` |
| RAW baseline | Bound fixture library/source/ID 1 and full settings/history; inspected direct 1024 × 684 PNG, then reread matching state |
| Actual adjustment | Guarded exposure 0 → +0.2 EV; complete settings comparison showed only exposure changed (floating-point readback within tolerance). Inspected fresh pixels: modest brightening in compared regions, with already bright areas also brighter; no clipping measurement claimed |
| Actual restoration | Fresh identity/full-settings/history checks matched the owned next step. `edit.undo` restored every development setting and active photo history; the restored PNG was actually inspected and byte-identical to baseline. Undo still named the fixture import; redo named Exposure. Equal settings/pixels did not erase redo |
| Changed baseline | Fixture actor injected exposure +0.4 and shadows +10. Pre-mutation comparison rejected the outdated experiment; state remained unchanged by the blocked attempt |
| Unrelated learner-control scenario | After agent exposure +0.2, fixture actor injected shadows +10. Guard rejected global undo. Explicit test agreement authorized exposure-only compensation; full settings matched baseline except retained shadows +10. Fresh compensated image inspected; compensation adds history |
| Same-control conflict | Fixture actor changed exposure to +0.5. Undo from the older agent snapshot was blocked; actor state preserved |
| Actual photo switch | Separately authorized fixture import/selection selected synthetic PNG B (ID 2). Both old-photo mutation and undo attempts were blocked, without changing B. B's direct image inspected |
| Revised skill behavior | Separate evaluation agent ran both new conversational cases plus legacy regression: 2/2, 2/2 and 6/6 grader criteria passed. These are supplied-event simulations with actual fictional Markdown writes, not live pixel inspection |
| Actual fresh agent recovery | New OpenCode invocation loaded installed skill, profile/progress and bounded references, without session detail or prior transcript. Recovered assisted simulated explanation, agent default, restored S0/redo and no pending authorization; required fresh agreement on B |
| Actual fresh mixed recovery | Another new invocation loaded profile/progress and the one relevant session to disambiguate preference. Recovered agent saved default versus mixed session-only preference, learner's completed shadows turn, last simulated 0/+10 values and unknown later undo/redo. No future agent adjustment was inferred authorized |
| Installation/update | Existing public CLI discovery/link and context-preservation tests passed with the new reference installed |

The integration guard is a temporary driver applying this protocol, not a new
production plugin or an atomicity guarantee supplied by LightCraft. Fixture actor
injection exercises real app state; it is **not an observed human mixed lesson**.
The independent conversational runs exercise tutor decisions and actual context
files. The fresh client runs recover those files. These forms of evidence are
complementary, not interchangeable.

## Evaluation artifacts and interpretation

Temporary evaluation root: `/tmp/opencode/issue-4-eval/`. Under `iteration-1/`,
each case has `with_skill` and `old_skill` outputs/grading plus metadata. Original
baseline instructions were read from commit `c9e86f8`. The two new case folders
and unchanged legacy `evals/evals.json` are the reproducible public inputs.

The original skill passed 1/2, 0/2 and 6/6 criteria respectively; the revised skill
passed 2/2, 2/2 and 6/6. The generated aggregate's **case-mean** rates are 50% and
100%, not a general success estimate. Legacy criteria pass in both versions; they
check regression rather than discriminate new operation support. Single authored
runs, supplied events, compound rubrics and non-blind grading limit inference.
Agent timing/token metrics were unavailable and were not invented.

The skill-creator viewer was generated at
`/tmp/opencode/issue-4-eval/review.html`, with outputs and quantitative comparison
available for human feedback. No human feedback or blind comparison is claimed.
New native client recovery traces are `agent-recovery-run.jsonl` and
`mixed-recovery-run.jsonl`, with readable summaries beside them.

Live temporary evidence: `/tmp/opencode/issue-4-live/` contains discovery, exact
before/after/restored snapshots, images, trace files and the fixture driver. The
initial driver tried `run_command("commands")`, which returned unknown command;
discovery was corrected to installed `lightcraft-cli commands --json`. No mutation
occurred in that failed discovery attempt. Commands/schema availability must be
rediscovered on other versions rather than assumed from this report.

## Reproduce and remaining limits

Follow `tests/experiment-scenarios.md` for service isolation, public case prompts,
exact interfaces and recovery procedure. Run the installation test with
`python -m unittest discover -s tests -p test_collection_installation.py -v` and
the full suite with `python -m unittest discover -s tests -v`. No typed application
or typechecker is present; Python tests and installed Markdown link checks apply.

No export, metadata/sidecar write, original overwrite, or file movement was run as
part of the lesson check. Copying the RAW and importing/selecting B were explicit
fixture preparation. Normal temporary-library journaling occurred.
After testing, a read-only check of the original desktop confirmed its same active
photo, exposure and history-entry count as at entry. Only the separate fixture
desktop was terminated; temporary evidence files remain available locally.

Live state checks are polling snapshots; an edit between read and mutation can
still race. No conditional revision-bound write was discovered in this route.
History labels alone are not unique operation IDs: the uninterrupted fixture
sequence establishes ownership here, not a reliable arbitrary-concurrency token.
Real mid-render switches, mutation timeout/partial-group failures, persistent
preference changes, abrupt-process recovery and additional clients remain unproven
by the live run. Timeout/stale-render branches were conversational simulations.
Restored image equality establishes this preview result, not decoder or color
fidelity. Human visibility and real learner understanding were not assessed for
the disposable fixture; existing learner-operated evidence remains in
`docs/lesson-validation.md`.

## Review

The independent specification reviewer reported no missing, incorrect or unasked
requirements. The standards reviewer found one duplicated teaching instruction
in the technical protocol. It was replaced with a pointer to the lesson's existing
Explain/Decide steps, retaining the fresh-baseline rule for revision. The OpenCode
installation guide was also updated to describe the three implemented preferences.
