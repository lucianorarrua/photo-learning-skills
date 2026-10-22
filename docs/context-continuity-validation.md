# Context continuity validation: issue #5

## Scope and environment

Executed in the issue #5 isolated worktree, starting from `2581111`, with OpenCode
**1.18.35**, model **openai/gpt-6.1-sol**, Linux and Python `unittest`. All profiles,
camera names, learning evidence and photo references were fictional. No real
LightCraft connection, original image or learner record was used. A moved `.png`
was a text placeholder, not a rendered image.

The instruction change makes existing continuity rules explicit and adds a shared
[continuity workflow](../skills/setup-photo-learning/references/continuity.md).
The confirmed verification boundaries were installed-skill behavior with actual
fictional records, and the real OpenCode installation/discovery interface.

## Observed results

| Boundary | Evidence |
| --- | --- |
| Setup revisit | Confirmed mixed default and borrowed ExampleCam Q persisted; metadata ExampleCam P did not become ownership; manual note and original session files preserved |
| Same-day sessions | A third timestamped session continued the same lesson; earlier prompted evidence retained its own link; assistance correction amended the same encounter and compact entry, without another outcome |
| Missing old source | Recovery proposed exposure practice on B without locating A or treating historical preview evidence as a current observation |
| Independent contexts | A/B kept separate profiles and histories; B's French profile stayed unchanged when C corrected A's shared default |
| Complete-context sharing | A real C → A context symlink was followed for the profile write; both root associations survived; the target and C link stayed intact during an actual temporary rename/dangling-link test |
| Occupied destination | Existing B context preserved; unresolved sharing choice surfaced rather than merged or overwritten |
| Explicit organization | Placeholder actually moved once; compact and detailed references retained historical paths plus dated verified relocation; LightCraft mapping left unverified; later setup caused no move |
| Pending repair and deletion | Prepared completed-move note reconciled with actual file writes and readback before clearing; no repeated move; placeholder then actually deleted by fixture actor; learner's deletion report retained as such, with historical evidence still usable for B |
| Instruction update/discovery | Three deterministic tests passed, including fresh CLI discovery in three non-Git roots after folder replacement, separate B records, and an unchanged shared symlink/target |
| Actual fresh client recovery | Two new CLI sessions loaded the installed skill after an old → new instruction replacement; recovered corrected mixed preference and prompted evidence from profile/progress only; one resolved C to A's complete context |
| Current verification | Both fresh sessions left readiness blocked with no service; proposed a new B lesson/operator agreement rather than replaying an old turn; records remained byte-identical |

The behavioral evaluation passed **8/8 new assertions** and **10/10 regression
assertions** (legacy 6, agreed-operation 2, concurrent-mixed 2). The old instruction
baseline also passed **8/8** new assertions. These authored compound cases confirm
usable behavior under supplied events, not a measured improvement or a general
success rate. No failing baseline was manufactured to claim a red/green result.

## Method, artifacts and limitations

Baseline and revised runs used separate installed instruction copies and actual
fictional file writes/moves. The evaluation agents performed and graded their
scenarios inline; the revised executor did not inspect old response outputs before
running its cases. This is not blind grading or a human learner demonstration.
Prompts include recovery expectations, which limits their ability to discriminate
between instruction revisions. One executor audit restored an initially expanded
historical path to its exact fixture wording, keeping relocation separate.

Local evidence under the worktree's ignored `.photo-learning/evaluation/`:

- `iteration-1/<case>/{old_skill,with_skill}/`: responses, actions, resulting records,
  graders and instruction preparation evidence.
- `iteration-1/benchmark.{json,md}` and `review.html`: generated skill-creator
  comparison (100% versus 100%; no measured improvement). No human feedback claimed.
- `regression/`: unchanged legacy and operation-case records and grading.
- `context-continuity-fresh.jsonl`, `shared-context-fresh.jsonl` and their summaries:
  actual new client invocations. The first recovers both linked exposure samples
  and their corrected prompting; the second resolves C's explicit shared target.

The fresh client fixtures were prepared outside Git under `/tmp/opencode/` from
the saved fictional records, with fixture root associations adapted explicitly.
Original simulated runs nested under the worktree inherit its Git boundary; local
exclusions were checked. The deterministic CLI tests and final fresh-client probes
use truly non-Git roots.

Initial nested CLI probes inherited the outer agent's tool/root context and failed
to find the locally installed skill even when launched with a temporary cwd. Their
zero exit codes were not treated as success. Retrying with an explicit `--dir`,
`--pure`, and without inherited `OPENCODE`/`OPENCODE_PID` produced correct local
skill loads and record reads. The logs retain those failed probes; the individual
cause among those environment changes was not isolated. This is a harness setup
finding, not a demonstrated OpenCode Git-discovery defect.

No application typechecker is configured: this repository ships Markdown skills
and Python installation checks. The single test file and installed link checks
passed during implementation. At completion,
`python -m unittest discover -s tests -v` passed all three tests, and
`git diff --check` passed. See
[reproduction scenarios](../tests/context-continuity-scenarios.md).

The reference-repair case starts from a prepared pending note; a filesystem failure
was not injected to produce it. Neither fixture understanding nor pixel fidelity
was measured. No synchronization,
partial-sharing service, concurrent-writer guarantee or mandatory runtime script
was introduced. Cross-client and live learner validation retain their prior limits.

## Review

Two-axis review used baseline `2581111` and the complete staged implementation.
The specification axis reported zero findings. The standards axis found duplicated
rules across instruction/guide pointers and duplicated test helpers. Rules were
consolidated into their authoritative workflows and the tests now reuse discovery
assertions and complete file snapshots. The same reviewer verified both findings
resolved; no findings remained pending.
