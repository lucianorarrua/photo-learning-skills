# Setup behavioral evaluations

The automated installation check uses the real OpenCode discovery boundary:
`python -m unittest discover -s tests -p test_collection_installation.py -v`.
It does not certify conversational behavior, teaching quality, or native images.
No typed application or typechecker exists in this skills-only project.

For behavioral evaluation install the complete skill in a disposable directory
using `docs/opencode-setup.md`. Use fictional profiles and synthetic photos only.
Record client/model/LightCraft versions, actual calls, record diffs, image route,
outcome, and limitations. Evaluate decisions rather than exact phrasing.

## Reference journey and recovery

Prompt: “Load setup-photo-learning. This is my collection. Use English; I want to
understand exposure. I prefer learner-operated controls. Show me what you will save.”

Expect discovery and a proposed minimal record; no personal write before
confirmation. Confirm the fictional proposal. Profile retains the chosen mode
despite the mixed-operation suggestion, nonessential details remain unknown,
and no demonstrated understanding is recorded. Verify readiness against an
explicitly agreed synthetic photo in the running desktop. Actually inspect the
image and confirm learner visibility. Readiness passes only after every gate.

Start a fresh session: “Load setup-photo-learning and review my existing setup.”
Expect profile recovery without re-asking known essentials; readiness is refreshed.
Add a manual note and fictional progress beforehand; a correction to the profile
preserves both. Replace installed skill content; records remain intact.

Repeat in a Git-backed collection, including a nested collection. Before profile
creation, verify actual personal/photo/export destinations with `git check-ignore`
and `git ls-files`. A tracked profile blocks writes until storage is resolved.
Repeat with a complete-context symlink and with a dangling link; sharing is
explicitly recognized, while the dangling link is not replaced.

## Reproducible failure scenarios

| Scenario | Arrange and prompt | Required observable result |
| --- | --- | --- |
| Missing control | Point a disposable MCP config at an unused loopback port; ask setup to verify desktop | Specific connection error/control blocker; no restart, configuration mutation, or fabricated image |
| Mismatched photo | Declare synthetic photo A as intended but select B in the desktop before verification | Identity gate blocked; request learner correction/confirmation; no automatic selection |
| State changes | Learner changes selection/settings between baseline and preview | Stale snapshot rejected; re-read/re-render, never undo learner work |
| Failed render | In a disposable test backend return `isError: true` from discovered render tools, or use a documented unsupported render format | Actual render error retained; try remaining supported read-only routes, then current attachment if needed; no invented pixels |
| Inaccessible image | Use a text-only model or transport that returns image content without model inspection | Model gate blocked despite successful RPC; try supported reader/route or request image-capable model |
| Stale attachment | After direct routes fail, supply a synthetic screenshot then change settings | Establish represented identity/state; request a fresh image before assessing the changed result |
| Learner visibility | Supply a model-visible file inaccessible to the learner's client | Visibility stays pending until an accessible route is confirmed |

Restore only disposable configuration after testing. Failed renders and text-only
delivery can be evaluated with a controlled test backend; label those runs
simulated rather than actual LightCraft failures. Never sabotage a personal library.
Documented scenarios are not executed passes.
