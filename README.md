# Photo Learning Skills

A planned collection of agent skills for guided photography editing and RAW development, using [LightCraft](https://github.com/storytold/lightcraft) through its [Model Context Protocol (MCP) server](https://github.com/storytold/lightcraft/blob/main/docs/mcp.md).

The goal is to help people understand their editing decisions, build photographic judgment, and gradually become more independent. An agent should explain, demonstrate, ask questions, and review the learner's work—not simply produce an automatic edit.

## Intended experience

1. Run a setup skill to establish your equipment, preferred language, goals, current experience, and editing environment.
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

**Design and technical validation stage.** The [project brief](BRIEF.md) and [domain glossary](GLOSSARY.md) capture the agreed learning experience. A [live LightCraft validation report](docs/lightcraft-validation.md) records desktop image retrieval, a reversible demo adjustment, and detection of learner-operated adjustments on a real NEF. There are no implemented photo-learning skills or installers yet; engineering workflow skills are available for developing the project.

LightCraft is an evolving alpha project. Its available MCP tools, camera compatibility, and rendering behavior must be checked against the installed version. Sharing skill content across agents does not guarantee identical tool or image support in every client/model combination.

## Next milestone

Specify and implement the setup conversation and local learning context contract, then validate one short guided lesson and cross-session continuity. Validate each target client (OpenCode, Claude Code, Codex, and Pi) before declaring it supported.

The [initial implementation specification](https://github.com/lucianorarrua/photo-learning-skills/issues/1) defines the learner-facing skills, context responsibilities, and acceptance criteria. Implementation tickets will be derived from that specification.
