# LightCraft Technical Validation

## Scope and provenance

This report records the live checks performed during the project's design session on 2026-10-19. Evidence was collected by a delegated validation agent through the installed CLI, JSON-RPC MCP calls, and direct inspection of rendered images, with learner participation for manual adjustments. This is a record of that run, not a reproducible automated test suite or a general compatibility certification.

No personal photos or previews are included. Temporary images used during validation were outside the repository. This report intentionally omits personal photo filenames, library paths, and image content descriptions.

## Environment

- Linux desktop; installed LightCraft application and CLI version **0.8.0**.
- MCP initialization reported protocol version **2025-06-18**.
- The initial desktop process did not enable control. Connecting to the default local control port failed with connection refused.
- The learner reopened the application with the intended persistent library and control enabled on port **7980**.
- Subsequent MCP initialization reported backend **remote 127.0.0.1:7980**; earlier isolated checks used **headless demo** mode.
- This OpenCode session used shell-mediated CLI/MCP calls. LightCraft was not registered as a native MCP tool provider in this client's configuration. Native tool discovery and native image-result delivery remain unverified.

Example desktop startup, substituting the actual executable and library locations:

```bash
lightcraft --library "/path/to/LightCraft Library" --control 7980
```

An existing application may need to be closed normally before restarting with control enabled. Reopening the application is a learner-coordinated action, not an automatic lesson prerequisite to execute without agreement.

## Live results

| Capability | Evidence | Scope and limits |
| --- | --- | --- |
| MCP discovery | Initialization, tool listing, and resource listing succeeded; the installed server exposed 17 tools and seven resources in the isolated check. | Catalog discovery does not prove every operation works. |
| Desktop connection | Connected to the running application after control was enabled. | Original launch without control was unreachable. |
| Library and active photo | Read library information, active selection, photo identity, source metadata, and development settings. The library gained a photo when the learner loaded a real NEF. | No need to switch photos from the agent. |
| Direct image access | Connected `render_preview` returned PNG image content, decoded to a temporary file and opened with an image-capable tool. The agent actually inspected desktop previews. | Validates this retrieval route, not every client's native MCP image handling. |
| Agent adjustment and undo | On the synthetic demo photo, applied exposure from 0.0 to +0.30 EV after explicit permission, read it back, inspected the new preview, and undid the change. | Full development settings, selection, and active history returned to baseline. Restored preview bytes matched the original; redo remained available. No agent adjustment was applied to the learner's RAW. |
| Real RAW identification | Active photo inspection reported a file source, RAW type, NEF format, Nikon D5300 metadata, and dimensions of 6016 × 4016. | These are reported metadata, not an independent decoder verification. |
| Real-photo render | Obtained and inspected a 1024 × 684 preview from the active NEF. Render state reported source `render`, no pending work, and no failure. Catalog `previewOnly` was null. | Null is not proof that embedded-preview fallback is impossible. Decoder identity and color fidelity were not established. |
| Learner adjustment detection | Learner manually changed exposure from 0.0 to +0.30 EV. Subsequent reads confirmed the same photo, the new value, unchanged other development settings, and an updated preview. | Polling establishes snapshots, not observation of every intermediate slider value. |
| Learner return to baseline | Learner manually returned exposure to 0.0. Complete development settings matched the recorded baseline; the restored PNG hash matched the original. | History contained three exposure entries rather than the initial empty history. Restoring values does not erase manual editing history. |

The demonstration and real-photo tests were separate. A synthetic demo proved the agent adjustment/undo loop; the real NEF proved identification, image retrieval, and the learner-operated feedback loop.

## Relevant interfaces

The installed interfaces used or inspected included:

- CLI/control commands: `library.info`, `library.state`, `photo.inspect`, `develop.get`, and `edit.undo`.
- MCP tools: `doc_inspect`, `get_develop`, `list_controls`, `set_develop`, `render_preview`, and `inspect_ui`.
- Active-photo resource: `lightcraft://photo/active`.

The server reported `subscribe: false`. Read identity and settings together, then poll as needed and recheck photo identity before applying an agreed operation. The run demonstrated stable snapshots and manual-change detection, not protection against every concurrent edit.

Before/after commands and export operations were present in the catalog, but were not executed. Documentation describes journal persistence separately from writing XMP metadata beside originals; neither should be confused with exporting a rendered image.

## Pending checks

| Check | Required evidence |
| --- | --- |
| Native client setup | Install/discover skills, connect tools, deliver inspectable images, and recover the same learning context in OpenCode, Claude Code, Codex, and Pi. Record version and model; do not infer compatibility from documentation. |
| Agent adjustment on a real RAW | Agree a small experiment, verify identity and baseline, inspect result, and verify restoration without overwriting intervening learner changes. |
| Before/after comparison | Exercise the installed supported comparison mode with agreement and restore the original view state. |
| Persistence | Agree a test edit and normal reopen, then verify the same settings are recovered. An empty pending-write queue alone is not a reopen test. |
| XMP metadata | If offered, test on an agreed fixture and verify exactly what is written without overwriting personal sidecars. This is not required for the initial guided lesson. |
| Export | Agree a photo, new destination, format, and conflict policy; export and inspect the result. No export was performed in this run. |
| RAW interpretation | Establish decoder/fallback facts from available diagnostics and investigate discrepancies against suitable references. A plausible-looking render alone cannot certify color fidelity or complete RAW decoding. |

## Consequences for the first implementation

1. A live application connection and a preview the agent can actually inspect are achievable on this installation.
2. Readiness must check the running application's control connection, not just the existence of the CLI or an MCP server.
3. Always attempt supported LightCraft image retrieval routes before requesting an attachment. This run did not need attachments.
4. Shared operation is feasible: the learner can move controls and the agent can observe the resulting state and image through polling.
5. Validate active-photo identity and current settings at each experiment boundary; changing the photo must not lead to edits on the wrong subject.
6. Record manual learning evidence separately from application history. An editing history step is not proof of understanding.
7. Keep capability claims specific to observed behavior, installed version, client, model, and image delivery route.

## Sources

- [LightCraft v0.8.0 MCP documentation](https://github.com/storytold/lightcraft/blob/v0.8.0/docs/mcp.md)
- [LightCraft v0.8.0 control protocol](https://github.com/storytold/lightcraft/blob/v0.8.0/docs/control-protocol.md)
- [LightCraft current MCP documentation](https://github.com/storytold/lightcraft/blob/main/docs/mcp.md) — consult installed-version evidence before relying on newer capabilities.
- [Pi MCP documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/mcp.md) and [skill documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md) — preliminary documentary review only; Pi was not tested live.
