---
description: Automate a new UBL Digital journey end-to-end (locators -> page -> tests -> docs)
---

# /new-journey

Use the user's message for: feature name, manual test cases, and page source file paths.

1. Read `AGENTS.md`.
2. Ask (max 3 questions) for anything missing: feature name, manual test case IDs and
   steps, page source XML for every screen in the journey.
3. Plan: list screens, page objects, locator files, fixtures and test files you will
   create or change. Classify test data (reusable / consumable / state_changing).
   **Wait for the user's "ok".**
4. Follow `.agents/skills/android-locators/SKILL.md` for each screen.
5. Follow `.agents/skills/page-object/SKILL.md` for each screen.
6. Follow `.agents/skills/pytest-journey-test/SKILL.md` for the tests.
7. Run `python -m py_compile` on changed files and `pytest --collect-only` on the
   feature folder. Do NOT run the tests.
8. Follow `.agents/skills/session-handoff/SKILL.md` to update TEST_AUTOMATION_STATUS.md.
9. Reply using AGENTS.md section 8, plus the exact command for the user to run the tests.
