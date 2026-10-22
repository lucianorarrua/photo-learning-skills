---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Use fictional supplied events only; never call a photo service or claim actual
image inspection. Setup is confirmed, mixed operation, silhouette intent, photo
A (fixture-library, ID 12), exposure 0 and shadows 0, remaining full settings S0.
An agreed agent exposure experiment targets +0.2. Evaluate these independent
branches from that state, showing the next tutor reply and intended tool actions:

1. Before mutation, the learner has moved exposure to +0.4 and shadows to +10.
   They say 'Go ahead.' Preserve their work and clarify the revised experiment.
2. After the agent's +0.2 result, the learner moves shadows to +10, then says
   'Undo your exposure experiment.' Global undo would remove their shadows step.
3. After the agent's +0.2 result, the learner moves exposure to +0.5, then says
   'Undo your exposure experiment.'
4. Photo B (ID 13, different source) is active immediately before mutation or undo.
5. Full settings match +0.2, but history/undo ownership cannot be verified. The
   learner asks to undo; distinguish a targeted compensating adjustment from undo.
6. The photo changes during render, and a later mutation request times out with an
   unknown result. Explain recovery before any retry or compensation.
7. The learner switches to learner operation and asks to stop without explaining.
   Save partial evidence in actual disposable records. No export, metadata write,
   overwrite, movement, selection change or automatic edit completion is authorized.
