# Issue tracker: GitHub

Issues and specs live in GitHub Issues for
`lucianorarrua/photo-learning-skills`. Use the `gh` CLI.

## Conventions

- Create: `gh issue create --title "..." --body "..." --label spec`.
- Read: `gh issue view <number> --json number,title,body,labels,comments`.
- List: `gh issue list --state open --json number,title,body,labels`.
- Comment: `gh issue comment <number> --body "..."`.
- Apply or remove labels: `gh issue edit <number> --add-label "..."`
  or `--remove-label "..."`.
- Close: `gh issue close <number> --comment "..."`.

Run commands from this clone so `gh` resolves the repository from
the Git remote.

## Ticket labeling

Every ticket published by the engineering skills carries `spec`.
Keep it when changing triage state; it is independent of the five
triage roles in `docs/agents/triage-labels.md`.

When a skill says "publish to the issue tracker", create a GitHub
issue with `spec`. When it says "fetch the relevant ticket", read
the referenced GitHub issue.

## Pull requests as a triage surface

**PRs as a request surface: no.**

## Parent issues and dependencies

Link child tickets using GitHub sub-issues. With `gh` 2.94+:
`gh issue edit <parent> --add-sub-issue <child>`.

If sub-issues are unavailable, put `Part of #<parent>` at the top
of each child body and list children in the parent's task list.

Use native issue dependencies for blocking edges:

```bash
gh api --method POST \
  repos/lucianorarrua/photo-learning-skills/issues/<child>/dependencies/blocked_by \
  -F issue_id=<blocker-db-id>
```

Get the blocker's database ID with
`gh api repos/lucianorarrua/photo-learning-skills/issues/<number> --jq .id`.
This is the database ID, not the issue number or node ID.

If native dependencies are unavailable, use a `Blocked by: #<number>`
line at the top of the child body. A ticket is unblocked when all
its blockers are closed.

## Wayfinding operations

- Map: an issue labeled `spec` and `wayfinder:map`, holding the
  Notes / Decisions-so-far / Fog body.
- Child: a ticket linked to the map, labeled `spec` and
  `wayfinder:<type>` (`research`, `prototype`, `grilling`, or `task`).
- Frontier: inspect open children in map order; select the first
  with no open blockers and no assignee.
- Claim: `gh issue edit <number> --add-assignee @me`.
- Resolve: comment with the answer, close the ticket, and append
  a concise finding and link to the map's Decisions-so-far.
