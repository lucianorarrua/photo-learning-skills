# Photo Learning Skills

A collection of agent skills for guided photography editing and RAW development, using [LightCraft](https://github.com/storytold/lightcraft) through its [Model Context Protocol (MCP) server](https://github.com/storytold/lightcraft/blob/main/docs/mcp.md).

The goal is to help people understand their editing decisions, build photographic judgment, and gradually become more independent. An agent should explain, demonstrate, ask questions, and review the learner's work—not simply produce an automatic edit.

## Intended experience

1. Run setup to confirm your language, intent, operation preference, and editing readiness; add equipment and experience when useful.
2. Keep that configuration in local files that other skills read as shared context.
3. Invoke a guided lesson, a focused exercise, or a review of your own edit.
4. Use LightCraft's MCP tools to inspect settings, obtain previews, make controlled adjustments, and compare results.
5. Save concise learning notes so future sessions can build on previous practice.

Example requests:

> Help me understand exposure and shadows using this photo. Change one thing at a time and let me make a decision before continuing.

> Review my edit before changing anything. Ask what I was trying to achieve, then explain the trade-offs.

## Design direction

- **Configurable:** camera systems, lenses, language, experience, and goals belong to each user's configuration.
- **Agent-portable:** target Claude Code, OpenCode, Codex, and Pi, with client-specific setup guidance where necessary.
- **Learning-first:** teach transferable concepts rather than slider recipes or a single aesthetic.
- **Context-aware:** use local Markdown configuration, progress summaries, and session notes, loading only what the current skill needs.
- **LightCraft-backed:** reuse its MCP capabilities rather than building another editor or MCP server.

The setup-first pattern is inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), particularly the explicit configuration and shared-context approach in its [setup skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md).

## Status

**Agreed experiments with learner, agent, or mixed operation.** Install `setup-photo-learning` and `photo-learning` together using the [OpenCode guide](docs/opencode-setup.md). Setup confirms a minimal profile and desktop/photo/image readiness; the lesson guides prediction, bounded adjustment, observation, explanation, and decision. Agent turns use an [experiment protocol](skills/photo-learning/references/experiments.md) to recheck state and preserve intervening learner work. The shared [context contract](skills/setup-photo-learning/references/context.md) defines profile, compact progress, and detailed session records for fresh-conversation recovery. See [setup validation](docs/setup-validation.md), [learner-operation validation](docs/lesson-validation.md), and [experiment validation](docs/experiment-validation.md) for observed results and limits.

LightCraft is an evolving alpha project. Its available MCP tools, camera compatibility, and rendering behavior must be checked against the installed version. Sharing skill content across agents does not guarantee identical tool or image support in every client/model combination.

## Next milestone

Validate each target client (OpenCode, Claude Code, Codex, and Pi) before declaring it supported, and extend live learner-participation evidence across operation preferences.

The [initial implementation specification](https://github.com/lucianorarrua/photo-learning-skills/issues/1) defines the learner-facing skills, context responsibilities, and acceptance criteria. [Issue #2](https://github.com/lucianorarrua/photo-learning-skills/issues/2) covers the setup journey delivered here.
