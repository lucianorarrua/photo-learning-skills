---
name: setup-photo-learning
description: Initialize photo learning in an existing collection, revisit learner preferences, or diagnose LightCraft readiness before practice. Confirm local context, save a minimal profile, and verify the current desktop photo and model-visible preview.
metadata:
  opencode/slash: "true"
---

# Set up photo learning

Read [context.md](references/context.md) before accessing personal records and
[readiness.md](references/readiness.md) before checking LightCraft. These shared
contracts also apply to subsequent photo-learning workflows.

## 1. Discover the collection

Confirm the learner-selected photo collection root; the working directory is
only a candidate. Resolve it to an absolute path and use that path for all context
operations; if the tools' working directory differs, resolve the mismatch before
writing. Preserve its organization. Apply the context contract's destination and
sharing rules before accessing `.photo-learning/`.

Read existing `profile.md` and `progress.md`, if present. Retrieve other records
only when relevant. Summarize known preferences and ask only for missing
essentials or requested corrections. Preserve manual notes and earlier records.

Completion: one confirmed collection/context destination and existing preferences
understood, or their absence established.

## 2. Confirm a minimal profile

Ask focused questions, together when nothing is known:

- Which interaction language and photographic terminology should we use?
- What do you want to achieve with this photo or initial practice?
- Who should operate controls: you, me executing agreed experiments, or both
  taking turns? Suggest mixed operation as a starting point, accept any choice,
  and explain that it is revisable. Agree who makes the next adjustment.

Equipment, time, pace, and self-reported experience are progressive context.
Ask when useful and leave unknown otherwise. Photo metadata does not establish
equipment ownership. Setup establishes readiness, not demonstrated understanding.

Show the exact proposed facts and destination, explain that the records are
editable local Markdown, and obtain confirmation before creating or changing
personal records. Let the learner correct the proposal.

Completion: confirmed language, initial intent, operation preference, and consent
to the proposed record. Keep an unconfirmed proposal in chat.

## 3. Persist without losing context

Apply the privacy gate in `context.md` before personal writes. If exclusions
cannot be established and verified, stop before writing and keep the proposal in
chat; confirmation of profile facts alone does not bypass this gate. Use
[profile-template.md](references/profile-template.md) for missing sections, filling
confirmed facts rather than copying placeholder claims. On revisits, re-read
before narrow edits; clarify contradictions. Preserve manual edits, unrelated
content, progress, and sessions. Summarize saved changes and invite corrections.

Completion: the confirmed profile can be read from the intended context, and
Git exclusions, when applicable, are verified. Unknown details remain explicit.

## 4. Verify the current photo

Execute the ordered gates in `readiness.md`. Inspect actual image content;
an image-shaped response or saved filename is insufficient. Keep readiness
separate from profile completion: confirmed preferences can be saved even when
access is blocked, with the blocker recorded honestly.

Completion: all gates have current evidence, or the exact blocked gate,
attempted routes, and next learner action have been reported.

## 5. Close setup

Save the readiness record defined in `context.md`. Show where the learner can
view the image and ask them to confirm the intended library/photo and current
appearance. Keep unconfirmed gates pending.

Report profile and readiness outcomes separately. When ready, offer the
[photo-learning workflow](../photo-learning/SKILL.md) for one brief practice
objective based on the current photo and intent; use its
[teaching reference](../photo-learning/references/teaching.md) when discussing that
practice. The lesson owns
prediction, adjustments, explanation, and evidence of understanding; setup does
not perform an automatic edit or manufacture progress. If blocked, give the
smallest useful next action and resume that gate after it is resolved.
