# Verify LightCraft readiness

Use read-only capabilities of the installed version. Setup does not authorize
changing settings, selection, view, library, files, or application configuration.
Distinguish tool facts, visual observations, and suggestions. Never invent
measurements, decoder/fallback identity, focus judgments, or color fidelity.

## Ordered gates

1. **Discover.** Record client/model, application and CLI/server versions and
   actual tools/resources. Read versions with installed `--version` commands when
   available; MCP initialization reports server version/backend. Prefer native
   registered MCP. Documentation names are
   candidates until discovered; tool listing alone does not prove access.
2. **Connect to the desktop.** Check backend/endpoint and read library identity
   (`library.info` via the discovered read-only command interface in 0.8.0).
   Recent-library UI entries and photo counts alone do not prove the current path.
   Headless/demo owns a different session and cannot certify desktop readiness.
   Obtain learner confirmation of the intended library. If control is absent,
   explain installed `--control`/`--connect` options and let the learner decide
   how to reopen normally. Never restart automatically or change configuration.
3. **Bind photo and settings.** Read active identity and full development settings
   together where possible (`lightcraft://photo/active` in 0.8.0). Compare ID/source
   with the intended photo; clarify ambiguity. Save this baseline without switching
   selection. Confirm the intended photo with the learner.
4. **Retrieve a fresh image.** Attempt available supported read-only routes before
   attachment fallback. In 0.8.0 candidates are `render_preview` (`id`, `max_side`,
   `format`), `render_photo` (`id`, `size`, `format`, omit `path`), and desktop
   `ui_screenshot`/`screenshot` (omit output path; keep current view). Use discovered
   schemas for exact arguments. If native delivery fails, try an available supported
   shell-mediated MCP/CLI route and local image-capable reader. Decode image content
   into excluded temporary storage when necessary. Label this fallback explicitly:
   it does not validate native image delivery.
5. **Inspect and recheck.** Actually open the image with a model-visible image
   interface, then reread active identity/settings. Require agreement with the
   baseline and returned image photo ID where available. Inspect pending/failure
   render status if exposed. Discard stale/mismatched results and repeat from
   step 3 against the learner's current choice. Bound retries; ask the learner
   to pause editing if state keeps changing. A filename, base64, hash, successful
   RPC, or learner description alone cannot prove the model inspected an image.
6. **Deliver to the learner.** Show the image through the client or an accessible
   local file/application view tied to the same state. Request confirmation of
   visibility and represented appearance. Resolve inaccessible remote paths through
   a supported delivery route. Model access alone does not prove learner visibility.

## Attachment branch

Record each available direct route attempted and its real failure. List unsupported
routes with the discovered reason. Then request a current preview/screenshot.
Establish photo identity, capture time, and represented development state; compare
with current application state where available. Missing control/settings remain
blocked even if attachment discussion is possible. Request a new image after
changes requiring assessment. A text-only model needs an image-capable model or
route; another inaccessible attachment cannot fix that blocker.

## Blockers and resumption

| Failure | Outcome and next step |
| --- | --- |
| Missing control | Block control; report endpoint/error and learner-coordinated enablement instructions |
| Wrong library/photo | Block identity; ask learner to choose/confirm intended state, then re-read |
| Render error/pending | Report actual status; try supported read-only alternatives; no assessment of missing pixels |
| Model cannot inspect | Block model gate; try supported reader/transport or an image-capable model |
| State changes during retrieval | Mark stale; get a consistent snapshot without undoing learner work |
| Learner cannot see image | Visibility pending; deliver an accessible image and request confirmation |

Report the specific failed gate instead of generic “MCP unavailable.” Resume failed
gates while refreshing time-sensitive state. A saved pass is historical evidence;
later practice must refresh identity, settings, and image.
