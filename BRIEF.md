# Project Brief

## Purpose

Create a reusable collection of agent skills that helps people learn photo editing and RAW development through guided practice. LightCraft supplies the editing engine and MCP interface; the skills supply teaching methods, exercises, feedback, and continuity between sessions.

The project should support learners with different camera systems, languages, experience levels, and creative goals. None of those characteristics should be hardcoded for the project's original author.

## Why skills first

LightCraft already exposes editing commands, settings, rendered previews, exports, and live application controls through MCP. The initial opportunity is to organize those capabilities into useful learning experiences, rather than create another application or duplicate its tools.

A skills-first repository provides a small starting point, readable instructions, and a shared methodology across agents. Add scripts or other software later only when a real workflow demonstrates the need.

## Setup and shared user context

Provide an explicit, conversational setup skill inspired by the setup-first approach in [Matt Pocock's skills repository](https://github.com/mattpocock/skills). The relevant pattern is to discover existing context, ask focused questions, confirm what will be recorded, and persist configuration that other skills can consume.

Setup should establish, as applicable:

- Preferred interaction language and terminology.
- Cameras, lenses, file formats, and relevant capture settings.
- Operating system, installed LightCraft version, and MCP connection details.
- Agent/client and whether its selected model can inspect image tool results.
- Learning goals, photographic interests, available time, and preferred teaching pace.
- Self-reported experience and an initial, revisable assessment based on a short exercise or discussion.
- Locations for photo collections and local learning context.

Existing configuration should be reviewed and updated without discarding prior learning records. Users should be able to edit their configuration directly or revisit setup. Assessment is provisional: distinguish what the learner reports from what has been demonstrated in practice.

## Local memory and context loading

Use human-readable local files so sessions can build on previous work across compatible agents. Keep relatively stable preferences separate from changing progress and detailed session history.

A possible layout, to be decided during implementation:

```text
<local-context-root>/
  profile.md
  progress.md
  sessions/
    <date>-<topic>.md
  topics/
    exposure.md
    white-balance.md
```

These paths are illustrative, not an implemented contract. The context root should be explicitly discoverable by each client, rather than assumed from an agent's private conversation memory.

Suggested responsibilities:

- **Profile:** preferences, equipment, environment, goals, and teaching style.
- **Progress:** concise overview of demonstrated understanding, open questions, and suggested next steps.
- **Session notes:** exercise objective, photo references, important decisions, observations, and follow-up practice.
- **Topic notes:** optional accumulated observations for concepts practiced over several sessions.

Define which files each skill reads and updates. Start with the profile and a small progress summary; retrieve relevant topic notes or session details only when needed. Avoid loading the entire history for every invocation or copying full chat transcripts into memory.

Personal configuration, learning history, photos, and exports should remain local and be excluded from the public repository by default. A future implementation should provide the corresponding ignore rules before creating those files. Public examples should use fictitious data or appropriately licensed material.

## Candidate learning workflows

### Guided development

Discuss the learner's intent, inspect a photo, choose one learning objective, and work through a small number of adjustments. Pause for observations and decisions rather than performing a complete edit immediately.

### Review an existing edit

Ask what the learner wanted to achieve, compare relevant previews and settings, and explain possible improvements before making changes. Separate technical concerns from aesthetic preferences.

### Controlled comparison exercises

Compare exposure versus shadows, temperature versus tint, contrast versus curves, or other related controls. Change one variable at a time and ask the learner to describe what changed.

### Technical diagnosis

Help distinguish an editing decision from an unsupported RAW variant, embedded-preview fallback, color interpretation problem, or export discrepancy. State uncertainty when available tools cannot establish the cause.

These workflows may become separate skills or modes of a smaller skill set. Their final boundaries remain open.

## Teaching principles

- Begin with creative intent and an achievable objective.
- Teach transferable photographic concepts, not fixed slider values.
- Let learners predict, observe, decide, and explain.
- Show a relevant preview after meaningful changes when the client supports it.
- Explain trade-offs and preserve room for deliberate creative choices.
- Distinguish measured facts, visual observations, and subjective suggestions.
- Never invent histogram data, clipping measurements, focus assessments, or decoder status that tools have not established.
- Adapt the pace to demonstrated understanding and user preference.
- End with a short takeaway and a useful next exercise.

## LightCraft integration

Prefer a connection to the running desktop application for interactive lessons, so the learner can see and manipulate the same editing session. Headless mode may be useful for repeatable comparisons or later automation.

Discover the tools and controls available in the installed version. Verify that the expected library is connected and that rendered previews can actually be inspected. Use supported commands for settings, comparisons, undo, and export; do not assume all documented capabilities exist in every release.

MCP access and photographic competence are separate concerns. A working connection does not guarantee correct RAW decoding, faithful color, or sound artistic advice. Initial validation should include real RAW files, saved edits, and an exported result.

## Agent portability

Keep teaching instructions and the local context format common wherever possible. Document client-specific skill discovery, invocation, MCP registration, and context pointers separately for Claude Code, OpenCode, and Codex.

Do not promise zero-configuration portability. Clients differ in skill loading, tool exposure, and image handling; the chosen model also matters. The shared files should provide continuity without relying on proprietary chat memory.

## Initial scope

The first implementation should establish:

1. A setup skill and a documented local context contract.
2. One guided learning workflow connected to the live LightCraft application.
3. A compact session record and progress update.
4. Setup guidance and a capability check for the initial supported clients.

Validate this with a small set of photos and an end-to-end lesson before expanding the skill collection.

## Deferred decisions

- Exact skill names, boundaries, and invocation conventions.
- Configuration discovery and local context location.
- How to assess understanding without making onboarding burdensome.
- How to represent alternate edits using capabilities supported by the installed LightCraft version.
- Whether installation helpers or deterministic scripts are warranted after the first trials.

## Success criteria

A learner can complete setup, start a focused lesson from a supported agent, inspect the effects of an adjustment, and explain the trade-off in their own words. A subsequent session can recover relevant preferences and learning progress from local files without requiring the learner to repeat their background.

## References

- [LightCraft](https://github.com/storytold/lightcraft)
- [LightCraft MCP documentation](https://github.com/storytold/lightcraft/blob/main/docs/mcp.md)
- [Matt Pocock's skills](https://github.com/mattpocock/skills)
- [Setup skill reference](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md)
