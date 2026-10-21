# Learner-operated lesson validation: issue #3

## Environment and scope

Executed on 2026-10-21, Linux, OpenCode **1.18.35**, model
**openai/gpt-6.1-sol**, installed LightCraft application/CLI **0.8.0**.
All committed learner examples are fictional. Real desktop photo references,
images, settings snapshots and raw logs remain outside the repository.

This report distinguishes automated installation checks, authored conversational
simulations, actual fresh model invocation, and live desktop observations. It is
not four-client certification or a statistical measure of teaching effectiveness.
There is no typed application/typechecker in this skills-only project.

## Observed results

| Boundary | Evidence and result |
| --- | --- |
| Installation red → green | Extended the existing public OpenCode discovery test to both skills; first failed because `photo-learning` was absent, then passed with both complete installed folders and resolving relative Markdown links |
| Update preservation | Replaced both installed skill folders in a disposable non-Git collection; obsolete instructions removed, fictional profile/progress/two same-date session records remained byte-identical |
| Native setup and invocation | Separate OpenCode CLI session loaded installed `setup-photo-learning`, read shared references, saved an explicitly confirmed fictional profile in a disposable collection, then loaded `photo-learning` |
| Desktop readiness | Initial default-port connection was refused. After the learner reopened LightCraft with `--control 7980`, native library/UI/settings/photo reads, `render_preview` and `ui_screenshot` succeeded. Actual pixels inspected; full settings and active identity rechecked. Human confirmed intended photo and desktop visibility; fresh readiness record marked those gates passed |
| Learner-operated adjustment | Tutor asked a region-specific prediction, then learner manually increased exposure 0 to +0.30 EV. Native full-settings reads showed only exposure changed on the same photo; fresh direct preview actually inspected and identity/settings rechecked stable. Tutor separated visible brightening from unestablished clipping and requested intent-relative explanation |
| Live evidence and closure | An initial preference for 0 EV elicited a concrete follow-up, not an automatic pass. Learner then identified the face as too white at +0.30 and preferred the appearance at 0. Saved recognition and reasoned aesthetic choice **with prompting**, independent/background explanation unproven, and intended restoration unverified. Learner later chose to stop; no further explanation or adjustment was required |
| Actual saved lesson recovery | A further genuinely new OpenCode conversation loaded profile/compact progress and historical readiness, without session detail or prior chat. Recovered assisted recognition, specific prompts, scoped partial outcome, chosen 0 EV versus last verified +0.30 EV, and a transfer exercise for a different future photo. No service calls, writes, new pixels or readiness claims |
| Superficial answer | Simulated with-skill branch asked a specific outline/background question, leaving recognition/explanation unproven |
| Deliberate aesthetics | Simulated branch respected silhouette intent while checking separation/competing emphasis, without automatic correction |
| Increased challenge | Simulated branch recognized a reasoned trade-off and asked a harder competing-priority question |
| Difficulty | Simulated branch narrowed the comparison to one outline/background region and preserved assistance as assistance |
| Interruption and actual file writes | Simulated immediate stop accepted without another required answer. Actual fictional Markdown session written first, compact progress linked it, and both read back. Prediction/adjustment/preference remained partial evidence, explanation and final edit choice unresolved |
| Fresh conversation recovery | A genuinely separate OpenCode session with no earlier transcript loaded only profile/compact progress plus skill references. Recovered preferences, prompting and interrupted status; proposed a new lesson for supplied synthetic B with A unavailable. No session detail read, demand to reopen A, write, service call, or fabricated B readiness |
| Partial-write reconciliation | A separate fresh OpenCode invocation found an actual pending index pointing to one fictional saved session missing from progress. Read only that named session, repaired compact progress under the same IDs, verified records, then cleared the index. Byte comparisons confirmed unchanged profile, both same-date sessions, existing evidence and manual note; no duplicate lesson added |

The live setup initially spanned CLI invocations that exceeded terminal timeouts;
the same client session resumed and completed local records. The later low-variant
lesson invocation finished normally. The timeout is not reported as an application
failure or evidence that abrupt-process recovery is guaranteed.

## Behavioral simulation comparison

The public eval prompt and six observable assertions live in
`skills/photo-learning/evals/evals.json`. Two separate evaluation agents produced
with-skill and without-skill responses under `/tmp/opencode/issue-3-eval/behavior/`.
They used supplied synthetic scene/settings/learner events, **not actual image
inspection or live adjustment detection**. Branches were independent; only the
interruption branch was persisted. The initial recovery demonstration in each
agent was same-process and is distinguished from the separate OpenCode recovery
invocation above.

Inspection of outputs found 6/6 behavioral assertions in the with-skill example
and 5/6 in the baseline: the baseline did not increase challenge after reasoned
understanding. It also chose JSON records instead of the project's Markdown
contract. Most behaviors also passed without the skill; this small authored
comparison does not establish a general improvement rate. Grading was performed
by the implementation agent, not an independent blind grader. Worker token/timing
metrics were unavailable from the tool responses and were not invented.

A static reviewer was generated using skill-creator's `eval-viewer/generate_review.py`
at `/tmp/opencode/issue-3-eval/review.html`. Outputs and grading are local, not a
published learner history.

## Reproduce

1. Run `python -m unittest discover -s tests -p test_collection_installation.py -v`.
   OpenCode is required for discovery; that check skips without it. The independent
   update-preservation check runs without the CLI.
2. Install both folders per `docs/opencode-setup.md` in a disposable collection.
   Use `opencode run --dir /absolute/collection --model <image-capable-model>` for
   isolated client runs. Explicitly consent only to fictional profile facts.
3. Follow `tests/lesson-scenarios.md` for the real learner-operated journey and
   its distinct conversational/persistence branches. Keep private images/logs local.
4. For a simulated teaching check, run the public eval with and without the skill
   in separate agents, label supplied observations simulated, inspect actual record
   files and grade observable decisions rather than exact phrasing.
5. Start a separate client invocation against saved records, without the previous
   transcript. Supply a different current photo and verify bounded loading, honest
   readiness, new lesson identity and practice choice.

## Remaining coverage

The live journey reached saved partial assisted learning evidence and fresh-session
recovery. The learner chose to stop before restoration verification or another
desktop photo. Returning to 0 EV was chosen but not confirmed; +0.30 EV remains
the last verified state. No automatic restoration was performed. The different-photo
recovery check used synthetic B as a recovery-only input; the later actual-record
recovery proposed practice for a different future photo. Neither was an actual B
render/experiment, and independent transfer remains unproven.

Documented but not yet executed: photo switching during a render, multi-slider
attribution, no detected change, same-session write retry/deduplication, correction
of both actual session/progress, missing record, symlink and
tracked-destination lesson writes. Two same-day fictional session fixtures survive
installation updates, but that is not a runtime collision-creation test.
Other clients, agent/mixed-operated experiments, abrupt process recovery and
concurrent writers remain outside this ticket's demonstrated learner-operated path.

## Review finding and repair

The specification review found that a session-only write could not be discovered
in a new conversation when its progress link had failed to save. The contract now
uses a small `pending-progress.md` index, written before evidence and cleared only
after session/progress readback. Recovery loads only its named records and reuses
their existing identifiers. A missing referenced record remains an explicit blocker,
not an invented outcome. This is bounded reconciliation, not full-history loading
or a crash-safety guarantee.

The spec reviewer rechecked the fix and reported the finding resolved with no new
defect. The separate standards reviewer found no actionable violations. Later
validation updates record the learner's assisted explanation/decision, save and
fresh recovery; the choice to stop and unverified restoration remain explicit.
