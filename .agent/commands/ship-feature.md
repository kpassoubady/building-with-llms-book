---
description: End-to-end feature delivery — runs the feature-factory chain, then syncs docs/examples, then hands off for PR. Single entry point so documentation never lags the code.
---

# Ship Feature

Wrapper that chains the build factory with this project's doc-update factory.
Use this instead of `/feature-factory` when you want docs/examples kept in lockstep.

Usage: `/ship-feature <feature description | path to a proposal/todo .md>`

## Steps

### 1. Build — feature-factory chain
Invoke the **feature-factory** skill with the given argument. Run the full chain
with all three human checkpoints (story → brief → hand-off). Do not skip them.
The chain ends after `07-validator.md` is written and Checkpoint 3 is presented.

Gate: only proceed to step 2 once the validator has **no open Critical findings**
and the user has accepted/deferred any Important ones at Checkpoint 3.

### 2. Docs — docs-sync
Run the **docs-sync** command. It diffs the feature branch against `main`,
finds new config keys and authoring features, and updates:
- `examples/*.json`
- `docs/llm-authoring-guide.md`
- `README.md` + the matching `docs/*.md`
- `CHANGELOG.md`

If docs-sync finds nothing user-facing changed, note that and continue.

### 3. Verify
Re-run the test suite (`pytest -q -m "not slow"`) to confirm the doc/example
edits (especially JSON) didn't break anything. Report pass/fail.

Refer to `dev/test-strategy.md` for the full test running strategy — when to
use the fast suite vs slow suite vs targeted module runs.

### 4. Hand off for PR
Summarize for the user: feature summary, files changed (code + docs split),
tests added, validator findings, the branch name, and a suggested PR title.

**Stop here. Do NOT open the PR** — the human reviews the diff and runs
`gh pr create` (or `/create-feature-pr`). This mirrors the feature-factory rule.

## Loop control
Inherit feature-factory's iteration limits. If docs-sync surfaces a config key
with no obvious example value or doc home, pause and ask the user rather than guess.
