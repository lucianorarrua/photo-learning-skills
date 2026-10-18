# Domain Docs

## Layout

This is a single-context repository:

```text
/
├── GLOSSARY.md
└── docs/
    └── adr/
        └── <number>-<decision>.md
```

## Before exploring

Read the root `GLOSSARY.md` and ADRs in `docs/adr/` relevant to
the area being explored.

If they do not exist, proceed silently. Domain modeling creates
them lazily when terms or decisions are resolved.

## Use the glossary's vocabulary

Use the glossary's defined terms in issue titles, proposals,
hypotheses, and test names.

If a needed concept is missing, reconsider whether it belongs to
the project's vocabulary or note the gap for `/domain-modeling`.

## Surface ADR conflicts

If a proposal contradicts an existing ADR, identify the ADR and
explain why the decision may need to be revisited.
