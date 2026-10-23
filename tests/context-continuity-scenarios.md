# Context continuity scenarios

## Boundaries

Use fictional profiles/history and disposable collections only. Install both
complete sibling skills under each collection's `.agents/skills/`; do not exercise
these scenarios against personal collections or an existing LightCraft service.
Supplied image/settings events are simulated, not inspected pixels or a human
learning demonstration. Judge responses, actual file operations and resulting
records rather than instruction wording.

## Behavioral cases

Run these public prompts through the installed skills, with their two graders:

| Case under `skills/photo-learning/evals/` | Observable checks |
| --- | --- |
| `context-continuity/` | Revisit confirmed preferences/equipment; metadata does not establish ownership; preserve manual notes/history; save a third same-day session; correct assistance using stable IDs; recover for B without locating A |
| `shared-context/` | Separate A/B profiles and histories; C explicitly shares A's complete context through a real symlink; preserve both root associations; dangling link blocks replacement records; occupied destination survives |
| `photo-relocation/` | Execute an explicit move as a general task; reconcile references with an auditable mapping; no automatic library-update claim; offline A does not block B; setup entry causes no extra move |
| `reference-repair/` | Reconcile a completed-move pending note without replay; verify links before clearing; preserve evidence after actual fixture deletion and an explicit deletion report; propose B practice |

Keep an old-instruction snapshot for comparison, independent fixture roots per
configuration, `responses.md`, actual records, an operation trace and grading
evidence. Also rerun legacy `evals/evals.json` and the `agreed-operation` and
`concurrent-mixed` cases. Existing fixtures are fictional; do not put local paths,
photos or personal evidence into public results.

## Installation and actual fresh recovery

Run `python -m unittest discover -s tests -p test_collection_installation.py -v`.
The CLI tests construct genuinely non-Git collections, replace only installed skill
folders, check local discovery after replacement, preserve separate contexts and
retain a complete-context symlink and its target byte-for-byte. They test the real
installation/discovery boundary, not whether an instruction contains a phrase.

For model recovery, prepare a non-Git temporary collection from the resulting
fictional records, retaining confirmed root/context associations. Install old
instructions, replace only the two instruction folders with the new revision, then
start a genuinely fresh `opencode run` invocation using `--dir` for that collection.
Ask it to load `photo-learning`, recover saved preferences and assisted evidence,
and propose practice on B without contacting LightCraft or retrieving A. Repeat
from C with its explicit complete-context symlink to A. Check the tool trace:

- The skill loads from the intended collection.
- Only profile and compact progress are needed as personal reads in these cases.
- The shared target is resolved consistently and independent B is not read.
- Saved operation preference is not a new experiment authorization.
- Current readiness is blocked, and historical observations are not current facts.
- All records remain unchanged; this probe is not itself a lesson.

When nesting a CLI inside an agent harness, ensure it receives the intended working
directory and environment rather than the outer session's tools. A zero process
exit code alone does not establish successful recovery: inspect the skill call,
record paths and final response. Use a standalone CLI environment and `--pure`
where needed; do not change the learner's global configuration for a fixture.

## Additional recovery branches

- If the old source is reported deleted, retain the learning evidence with that
  dated report; do not infer deletion from a failed read. Begin practice on B.
- If a moved source is relevant, locate it with a learner path or bounded lookup;
  matching filenames alone cannot prove library identity.
- If a reference repair fails after a successful move, leave a small verified-move
  entry in `pending-progress.md` when possible. Fresh recovery repairs those links
  without replaying the move. If personal writes fail entirely, report the stale
  references and provide the unsaved note in chat.

The `reference-repair` case exercises a prepared pending note, not an injected
filesystem permission failure. Neither the main scenarios nor that recovery case
imply concurrent-writer, synchronization, crash recovery, real RAW rendering, or
cross-client support.
