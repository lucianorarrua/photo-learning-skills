---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Use a disposable fictional collection, installed skills and actual Markdown writes.
Copy tests/fixtures/learning-context into .photo-learning. Do not contact LightCraft.
The harness supplies the fixture and installed skill paths.

Fixture preparation: create a text placeholder at Keepers/synthetic-a.png. An
earlier general agent task already moved it from Originals/synthetic-a.png, but
reference reconciliation failed. Put a small entry in pending-progress.md with
that verified old-to-new mapping, date 2026-10-21, lesson IDs and both session paths
from the fixture, and explicitly label it 'reference repair only; move completed'.

Now invoke photo-learning in a fresh recovery: 'I want a new exposure lesson on B.
Recover my saved context and handle the pending note first.' Repair only what is
pending and retain original historical references. Do not replay the completed
move. Record the actual recovered state and leave no duplicate outcomes.

Next the fixture actor deletes Keepers/synthetic-a.png. I explicitly report:
'I deleted A permanently. Continue with B; I do not want to retrieve A.' Keep
the prior learning evidence and distinguish my deletion report from any current
library or pixel verification. Propose practice on B; no real service is available.

Save responses.md, actual context records and actions. Recovery does not authorize
an experiment. Do not create evidence of learning or readiness for this probe.
