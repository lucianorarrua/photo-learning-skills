# Project Brief

## Purpose

Create a reusable collection of agent skills that helps people learn photo editing and RAW development through guided practice. LightCraft supplies the editing engine and MCP interface; the skills supply teaching methods, exercises, feedback, and continuity between sessions.

The project should support learners with different camera systems, languages, experience levels, and creative goals. None of those characteristics should be hardcoded for the project's original author.

The initial learner already has LightCraft installed and can perform basic application operations, but is a beginner in intentional RAW development. The initial goal is to improve photographic decision-making rather than teach application installation or assume advanced editing knowledge.

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
- Revisable operation preference: the learner operates the controls, the agent executes agreed experiments, or both take turns. Suggest mixed operation and clarify who performs the next adjustment.
- Self-reported experience and an initial, revisable assessment based on a short exercise or discussion.
- Locations for photo collections and local learning context.

Existing configuration should be reviewed and updated without discarding prior learning records. Users should be able to edit their configuration directly or revisit setup. Assessment is provisional: distinguish what the learner reports from what has been demonstrated in practice.

Setup is progressive. Begin the first practice once the interaction language, initial intent, and operation preference are known and access to the photo and inspectable previews has been verified. Gather other details when they become useful rather than requiring a complete equipment inventory before teaching.

Use a brief first lesson on the learner's photo to validate the environment and gather initial evidence of understanding. Technical readiness and photographic understanding are separate outcomes; no separate entrance exam is required, and setup and practice need not finish in one session.

## Local memory and context loading

Use human-readable local files so sessions can build on previous work across compatible agents. Keep relatively stable preferences separate from changing progress and detailed session history.

Initialize in the learner-selected photo collection root, such as `/photos`, preserving its existing subdirectories. A Git repository is not required. Install skills at collection scope and keep personal learning data separate from installed instructions so skill updates preserve the profile and history.

Target layout:

```text
<photo-collection-root>/
  .agents/skills/          # Target shared skill installation; verify per client
  .photo-learning/
    profile.md
    progress.md
    sessions/
      <date>-<topic>.md
    topics/                # Optional, when needed
      exposure.md
      white-balance.md
  ...                      # Existing photo organization
```

The personal context location is `.photo-learning/` under the collection root. Internal filenames above are proposed until the local context contract is implemented. Verify skill discovery for each client, using a shared installation where compatible and minimal client-specific adapters where necessary. Each client must explicitly discover the same learning context rather than depend on private conversation memory.

Each collection has an independent learning context by default. As an exceptional, optional action, an agent may link a collection's `.photo-learning/` to an existing complete context using a symbolic link when the environment supports it. Explain that profile, progress, and session history become shared live data and obtain confirmation before linking. Keep skill installations separate and never automatically replace an existing destination context. This option is not required to validate the first version.

Suggested responsibilities:

- **Profile:** preferences, equipment, environment, goals, and teaching style.
- **Progress:** concise overview of demonstrated understanding, open questions, and suggested next steps.
- **Session notes:** exercise objective, photo references, important decisions, observations, and follow-up practice.
- **Topic notes:** optional accumulated observations for concepts practiced over several sessions.

Define which files each skill reads and updates. Start with the profile and a small progress summary; retrieve relevant topic notes or session details only when needed. Avoid loading the entire history for every invocation or copying full chat transcripts into memory.

Save concise progress at lesson closure and a partial record when a session ends before the lesson is complete. Record observed evidence, prompting needed, and what remains unproven; summarize what was saved so the learner can correct it. Do not treat a missing explanation as demonstrated understanding.

Preserve learning records when referenced photos have moved, been deleted, or are temporarily unavailable. Distinguish recorded evidence from what can be verified now. Locate an earlier photo only when needed for the current task; its absence must not block a new lesson.

Personal configuration, learning history, photos, and exports should remain local and be excluded from the public repository by default. A future implementation should provide the corresponding ignore rules before creating those files. Public examples should use fictitious data or appropriately licensed material.

## Lessons and sessions

A lesson practices one concrete learning objective on one photo. One photo can support several lessons, and the same objective can recur in separate lessons on different photos. A session is a working encounter that can start, continue, or complete a lesson; a lesson can span sessions. See `GLOSSARY.md` for canonical terminology.

Start each session from the learner's current photo and intent. Use prior progress to suggest relevant objectives rather than impose a backlog. A pending objective does not require returning to an earlier photo, particularly when the current image does not support that practice.

Treat an objective as achieved when the learner recognizes the adjustment's effect and explains its trade-off in their own words, with prompting if needed. Assessment remains provisional and specific to observed evidence, without numeric grades or global proficiency labels. A finished edit alone does not establish learning.

## Working with the photo collection

The collection root is also a working context for general agent tasks. When explicitly asked, the agent may help organize files and execute clear moves or renames if it understands the source, destination, and existing organization. The explicit request is sufficient authorization for an unambiguous operation; ask when relevant ambiguity remains. Consider affected LightCraft and learning-record references and check the result.

Collection initialization and lessons do not implicitly authorize file reorganization. File-management assistance is general agent functionality, not an additional learning workflow or a required new skill.

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
- Use the cycle predict → adjust → observe → explain → decide. Operation preference changes who manipulates controls, not the learner's responsibility to think and decide.
- Inspect a relevant, current preview after meaningful changes, following the visual-access requirements below.
- Explain trade-offs and preserve room for deliberate creative choices.
- Distinguish measured facts, visual observations, and subjective suggestions.
- Never invent histogram data, clipping measurements, focus assessments, or decoder status that tools have not established.
- Adapt the pace to demonstrated understanding and user preference.
- Be objective and constructively demanding: challenge superficial answers, request another observation or attempt, and increase difficulty as understanding develops. Give specific hints or smaller steps when the learner becomes stuck or frustrated.
- Praise concrete achievements rather than flatter or accept weak explanations for the sake of satisfaction. Seek progressive improvement without overwhelming a beginner.
- Evaluate coherence with the learner's declared intent and verifiable technical concerns. Challenge unintended consequences while accepting deliberate aesthetic choices whose trade-offs the learner understands.
- Let the learner stop or change topics even when understanding remains unproven; record the unfinished learning honestly.
- End with a short takeaway and a useful next exercise.

## LightCraft integration

Prefer a connection to the running desktop application for interactive lessons, so the learner can see and manipulate the same editing session. Headless mode may be useful for repeatable comparisons or later automation.

Discover the tools and controls available in the installed version. Verify that the expected library is connected and that rendered previews can actually be inspected. Use supported commands for settings, comparisons, undo, and export; do not assume all documented capabilities exist in every release.

Always prioritize images obtained from LightCraft. Exhaust available supported ways to obtain an inspectable image from the application before requesting an attached preview or screenshot. If an attachment is necessary, establish which photo and editing state it represents and obtain an updated image after changes that require visual assessment. An older image cannot verify a newer edit. If the agent has no way to see the image, resolve visual access before continuing visual practice; learner descriptions alone do not satisfy this requirement.

When the agent operates controls, agreement on a small experiment authorizes its adjustments without confirmation for every slider movement. After observing the result, the learner decides whether to retain, revise, or undo it. Exports, overwrites, and file operations require their own agreement rather than inheriting authorization from an editing experiment.

MCP access and photographic competence are separate concerns. A working connection does not guarantee correct RAW decoding, faithful color, or sound artistic advice. Initial validation should include real RAW files, saved edits, and an exported result.

## Agent portability

Keep teaching instructions and the local context format common wherever possible. The initial target clients are Claude Code, OpenCode, Codex, and Pi. Document client-specific skill discovery, invocation, MCP registration, and context pointers separately.

Do not promise zero-configuration portability. Clients differ in skill loading, tool exposure, and image handling; the chosen model also matters. The shared files should provide continuity without relying on proprietary chat memory.

Verify each supported client/model combination through a real lesson, including skill discovery, shared context access, LightCraft connectivity, and images that both the learner and the agent can inspect. Target-client status does not itself establish compatibility.

## Initial scope

The first implementation should establish:

1. A setup skill and a documented local context contract.
2. One guided learning workflow connected to the live LightCraft application.
3. A compact session record and progress update.
4. Collection-local installation guidance, setup guidance, and capability checks for Claude Code, OpenCode, Codex, and Pi.

Validate this with a small set of photos and an end-to-end lesson before expanding the skill collection.

## Deferred decisions

- Exact skill names, boundaries, and invocation conventions.
- Exact internal file formats and client-specific discovery mechanisms for the agreed collection-local context and skills.
- How to represent alternate edits using capabilities supported by the installed LightCraft version.
- Whether installation helpers or deterministic scripts are warranted after the first trials.

## Success criteria

A learner can complete setup, start a focused lesson from a supported agent, inspect the effects of an adjustment, and explain the trade-off in their own words. A subsequent session can recover relevant preferences and learning progress from local files without requiring the learner to repeat their background.

Returning with a different photo must allow a relevant new lesson without requiring the previous photo. Switching validated clients within the same collection must preserve continuity. Feedback must distinguish genuine demonstrated understanding, unresolved learning, and deliberate aesthetic choices.

## References

- [LightCraft](https://github.com/storytold/lightcraft)
- [LightCraft MCP documentation](https://github.com/storytold/lightcraft/blob/main/docs/mcp.md)
- [Matt Pocock's skills](https://github.com/mattpocock/skills)
- [Setup skill reference](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md)
- [Pi](https://github.com/earendil-works/pi)
