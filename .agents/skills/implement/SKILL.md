---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Before implementation edits, create a dedicated branch and isolated Git worktree
for this task. Inspect repository status and existing worktrees, choose an unused
branch and sibling directory, and create the worktree from the intended starting
commit. If this invocation already has a dedicated task worktree, verify and reuse
it. Report its path and branch, then run every edit, check, review, and commit in
that worktree. Preserve the source checkout's branch and uncommitted changes;
do not stash, reset, or copy unrelated work into the task. Resolve an ambiguous
starting point before editing. Git worktrees isolate files and branches, not
external services; use disposable fixtures for integration checks.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "code-review" to review the work.

Commit your work to the task branch in its isolated worktree.
