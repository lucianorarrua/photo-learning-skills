# Setup validation: issue #2

## Scope

Run on 2026-10-19, Linux, OpenCode **1.18.35**, model
**openai/gpt-6.1-sol**, installed LightCraft application/CLI and MCP server **0.8.0**, MCP protocol
**2025-06-18**. Application/CLI versions were obtained from `--version`; the
MCP initializer reported server version and remote backend. The remote desktop
process version was not independently queried. No private photos,
previews, absolute personal paths, or full transcripts are published here.

This is setup evidence, not lesson-quality certification or four-client support.
The disposable collection held fictional preferences; the separate existing
desktop library was inspected read-only. Its selection/settings were not changed
to create a synthetic desktop fixture. After the first run kept human gates
pending, the learner explicitly confirmed intended desktop library/photo and
current image visibility through the question tool. A subsequent native refresh
passed every readiness gate; the dated local record now reports ready.

## Observed results

| Boundary | Evidence | Outcome / limit |
| --- | --- | --- |
| Non-Git collection installation | Copied complete `skills/setup-photo-learning` into a temporary `.agents/skills/`; `opencode debug skill` returned its exact installed path | Pass; no Git initialization or personal files created by discovery |
| Skill invocation | Fresh OpenCode run with explicit `--dir` called `skill` with `setup-photo-learning` successfully | Pass; the installed body and relative references were loaded |
| Minimal profile | Fictional English / understand exposure / learner-operated preferences supplied with explicit record confirmation | `profile.md` saved; equipment, time, pace and experience unknown; no progress/demonstrated understanding invented |
| Native registration | Collection-local `opencode.json` registered `lightcraft-cli mcp --connect 127.0.0.1:7980 --compact`; `opencode mcp list` showed connected | Pass for registration; listing alone was not treated as image evidence |
| Native desktop/image route | Native library/UI reads, `lightcraft://photo/active`, `render_preview` JPEG 1024 × 684, and `ui_screenshot` JPEG 1200 × 705 succeeded in the selected model session | Model described actual image pixels; preview and screenshot content agreed; no shell image fallback in this run |
| Snapshot consistency | Full active-photo settings captured before preview, then read again; ID/source/settings matched; UI reported no pending/failed render | Pass for observed snapshots, not concurrency guarantees or RAW fidelity |
| Readiness persistence | Saved a local `readiness.md` with full settings baseline, route, observations and gate outcomes | Initially kept human gates pending; after explicit learner confirmation and a fresh native check all gates passed |
| Fresh-session recovery | A second independent run loaded the skill and read existing profile/progress without chat continuity | Recovered English, exposure intent and learner-operated preference; unknowns stayed unknown; readiness required refresh |
| Manual records | Added a fictional manual profile note and pending progress before recovery | Preserved; recovery made no writes and invented no demonstrated understanding |
| Nested Git collection privacy | Separate disposable Git root with a nested collection; agent appended root-anchored context/original/export rules before saving the fictional profile | `git check-ignore -v` confirmed all three destinations; existing local exclusion rule preserved; no progress invented |
| Shell-mediated route | Separately initialized MCP over stdio to the same remote desktop, obtained PNG 1024 × 684, opened it with an image-capable reader, then compared identity/settings/history | Pass for this fallback route; not used as evidence of native delivery |
| Missing control | `lightcraft-cli run --connect 127.0.0.1:17980 library.info` on an unused port | Failed with connection refused and explicit `--control 17980` guidance; no restart or configuration changes |

The initial native output included a recent-library entry without proving the
current catalog path. The final native refresh used discovered read-only
`library.info` before and after preview retrieval, establishing stable library
path/persistence identity. Full photo identity/settings also matched. It resolved
an album-count difference through read-only `albums.list`: one API includes the
folder entry while the other counts only albums. No application mutation was
needed. The instructions explicitly point to `library.info` and version queries.

The final refresh ran at 13:58:57–13:59:16 local time (UTC−03:00). The actual native
preview was inspected again; learner visibility was confirmed in the desktop
view of the same unchanged photo/settings. Only the disposable readiness record
was updated; the fictional profile/manual note/progress were preserved.

## Failed evaluation and correction

An initial `opencode run` without explicit `--dir` executed against the harness's
current project rather than the intended temporary collection. Skill/native MCP
discovery therefore failed. It also wrote fictional evaluation files despite an
unresolved Git exclusion gate. Those newly created evaluation files were removed;
no existing learner data was overwritten. The skill now requires absolute context
paths and explicitly stops personal writes when privacy prerequisites cannot be
verified. The successful rerun used `--dir` and an explicit absolute collection.
A separate nested Git-backed conversational rerun subsequently created and
verified exclusions before saving its fictional profile, preserving the existing
local exclusion rule. That run deliberately left desktop readiness pending.

## Reproduce

1. Run `python -m unittest discover -s tests -p test_collection_installation.py -v`.
   This requires the OpenCode CLI; without it the integration check is skipped.
2. Follow `docs/opencode-setup.md` in a disposable collection. For CLI evaluations,
   use `opencode run --dir /absolute/disposable/collection --model <image-model>`.
3. Use the prompts and observable outcomes in `tests/setup-scenarios.md`. Confirm
   only fictional profile facts, explicitly identify the desktop fixture, and
   inspect the actual preview through the model and learner routes.
4. Reopen a fresh client session and request existing setup recovery. Keep raw
   logs/images local; publish only redacted outcomes and remaining limitations.

There is no typed application to typecheck. The automated suite checks actual
OpenCode discovery and installed reference resolution; conversational outcomes
above were live checks, not automated test assertions.

## Pending behavioral coverage

Reproducible scenarios for wrong/changed photo, failed render, inaccessible model
images, stale attachment, and learner visibility are documented in
`tests/setup-scenarios.md`; they are not reported as executed passes. Tracked
destinations, existing shared contexts, correction writes, and update-preservation
scenarios also remain explicit evaluation work. Nested Git-backed initialization
and fresh-session preservation were exercised as recorded above.
No automatic restart, setting change, import, export, or lesson
experiment was used to obtain this setup evidence.
