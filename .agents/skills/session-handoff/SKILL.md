---
name: session-handoff
description: Update ARCHITECTURE.md, ENVIRONMENT.md, TEST_AUTOMATION_STATUS.md and DECISIONS.md at the end of a work session so the next session can continue. Use when the user says "wrap up", "update docs", or a meaningful change was made.
---

# Session handoff

## Goal
Keep the four project documents true, so any agent or person can pick up the work later.

## Steps
1. List what changed this session (files, journeys, versions, decisions). Use `git status`
   and `git diff --stat` to check.
2. Update only the affected documents:
   - **ARCHITECTURE.md**: folder/structure changes, new BasePage methods, new fixtures.
   - **ENVIRONMENT.md**: version/capability/device changes (only confirmed values,
     unknown = `[CONFIRM]`).
   - **TEST_AUTOMATION_STATUS.md**: per feature: NOT STARTED / IMPLEMENTED /
     STATICALLY REVIEWED / EXECUTED / VERIFIED; known issues; FLAKY tests (with owner);
     blockers; developer dependencies (link testability requests).
   - **DECISIONS.md**: append `## D-<n>: <title>` with Date, Decision, Reason,
     Alternatives considered, Impact.
3. Only mark EXECUTED/VERIFIED if the user confirmed a real run.
4. Never write secrets, real account data or device UDIDs of personal devices into docs.
5. Show the user a diff of the doc changes before saving.

## Reply must include
- Which docs changed and a 1-line summary each
- Suggested commit message, e.g. `docs: update status after Android login conversion`
