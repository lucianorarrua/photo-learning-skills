---
name: photo-learning
description: Practice intentional photo editing with the current LightCraft photo, review an adjustment, or resume learning from saved evidence. Guide prediction, observation, explanation, and decision with learner, agent, or mixed operation; execute agreed small experiments while preserving intervening learner work and recoverable progress.
metadata:
  opencode/slash: "true"
---

# Learn from the current photo

## 1. Recover context

Read the shared [context contract](../setup-photo-learning/references/context.md)
before accessing records and [teaching reference](references/teaching.md) before
practice. Confirm the absolute collection/context destination, recognizing an
existing complete-context link. Read `profile.md` and compact `progress.md` first;
load a referenced session only to resolve a relevant uncertainty or continue that
lesson. If `pending-progress.md` exists, read that small reconciliation index and
repair its named records using the context contract before proposing duplicate
practice. Prior chat and the full history are unnecessary.

If essentials or storage confirmation are missing, invoke `setup-photo-learning`
using its [setup workflow](../setup-photo-learning/SKILL.md). Preserve existing
records. A saved readiness pass is historical: execute the shared
[readiness gates](../setup-photo-learning/references/readiness.md) against the
current desktop photo, settings, and actually inspectable preview.

Completion: confirmed profile/context and fresh readiness, or a specific blocker
with its next action. Resolve the blocker before visual practice.

## 2. Agree one objective

Ask for the current image's creative intent and propose one achievable learning
objective based on that intent, the visible photo, relevant evidence, and available
time. Agree the objective and who operates the next adjustment. Self-reported
experience helps choose an opening question; observed understanding sets challenge.

Honor the operation preference: learner operates, agent executes agreed small
experiments, or mixed turns. In mixed mode name who performs the **next adjustment**
and the handoff signal. The learner always predicts, observes, explains and decides.
Allow preference changes at any time without restarting the lesson or discarding
evidence. Confirm whether a change is for this turn/session or the saved default;
use setup's narrow profile reconciliation for a persistent change. Retain the
current in-session preference even if saving fails, reporting that limitation.
On recovery distinguish the saved default from a previous session-only preference
or completed turn; confirm the new session's operator rather than replaying a handoff.

Assign a stable lesson ID for this objective/photo pair, checking relevant pending
entries before minting another. Multiple objectives on one photo are separate
lessons. The same objective on a different photo starts a new lesson; previous
pending work never requires reopening the old image. Continue an existing lesson
only when its photo/objective still match and the learner chooses to continue.

Completion: learner agrees one objective, current photo, and the next operator.

## 3. Run a controlled experiment

1. **Predict and agree.** With current full settings and an inspected preview as
   baseline, ask what a small adjustment should change in a named region and what
   it may cost elsewhere. Agree the supported control(s), bounded change and useful
   comparison, not a universal recipe. Before an agent turn, read the
   [experiment protocol](references/experiments.md); it governs discovery,
   authorization, mutation, concurrent changes, revision and restoration.
2. **Adjust.** Name the operator. On a learner turn ask them to operate LightCraft
   and signal readiness; keep agent calls read-only, including selection/view and
   undo. On an agent turn execute only the agreed small experiment under the
   protocol. The agreement authorizes its bounded changes without repeated
   slider-by-slider permission. A control explanation alone is not authorization.
3. **Observe.** Re-read active identity and settings, retrieve a fresh direct
   LightCraft preview and inspect it, then recheck identity/settings as in readiness.
   Compare the stable before/after snapshots. These are polling snapshots, not a
   stream of intermediate slider values. If several controls changed, report the
   observed differences and reduce the next experiment rather than attributing
   everything to one control. With no detected change, ask what happened.
4. **Explain.** Ask the learner to name the visible effect and explain its trade-off
   in their own words. Compare with their prediction. Apply the teaching reference
   to superficial answers, demonstrated understanding, or difficulty; record hints
   actually given. Another experiment is useful only when it serves this objective.
5. **Decide.** Ask whether the learner wants to retain, revise, or undo the result
   and why it suits their intent. Name who performs revision/undo; for an agent
   turn follow the protocol's fresh checks and conflict branches. Refresh settings
   and actually inspect the image before assessing that result too. A decision to
   keep ends this experiment; it does not authorize a complete automatic edit.

On a changed photo, pause attribution and confirm its identity and intent. Preserve
the earlier lesson's partial evidence; offer a new lesson on the new photo. On
unstable state or failed image access, use readiness recovery and leave assessment
pending. Never infer a visual effect from slider values alone.

Completion: record what was actually recognized/explained, assistance needed, and
the learner's decision; sufficient evidence or a request to stop leads to closure.
A finished edit or following instructions alone does not complete the objective.

## 4. Preserve and close

At closure, interruption, or a topic change, follow the shared
[record procedure](../setup-photo-learning/references/context.md#lesson-records).
Save concise evidence and unresolved understanding, including partial work when
the learner stops before explaining. Let them leave immediately; no explanation
or successful answer is a condition for stopping. Use `pending`/`interrupted`
honestly rather than manufacturing success.

Summarize what was actually saved and where; invite correction without blocking
departure. Offer one takeaway grounded in the observed experiment and one useful
next practice. If writing fails, report the unsaved state and provide a compact
copyable note; do not claim persistence. At a fresh invocation, begin at step 1
and adapt practice to the new current photo.
