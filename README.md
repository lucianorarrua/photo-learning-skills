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
- **Agent-portable:** target Claude Code, OpenCode, Codex, and other compatible agents, with client-specific setup guidance where necessary.
- **Learning-first:** teach transferable concepts rather than slider recipes or a single aesthetic.
- **Context-aware:** use local Markdown configuration, progress summaries, and session notes, loading only what the current skill needs.
- **LightCraft-backed:** reuse its MCP capabilities rather than building another editor or MCP server.

The setup-first pattern is inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), particularly the explicit configuration and shared-context approach in its [setup skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md).

## Status

**Concept stage.** This repository currently contains only this README and the [project brief](BRIEF.md). There are no implemented skills, installers, integrations, or user configuration files yet.

LightCraft is an evolving alpha project. Its available MCP tools, camera compatibility, and rendering behavior must be checked against the installed version. Sharing skill content across agents does not guarantee identical tool or image support in every client/model combination.

## Next milestone

Define the setup conversation and local context contract, then validate one short guided lesson with LightCraft's live application connection.
