# DECISIONS.md: UBL Digital Android Automation

Format: each decision has a date, the decision, the reason, the alternatives considered
and the impact. Add new decisions at the bottom; don't edit old ones. If a decision
changes, add a new entry that supersedes it.

---

## D-1: Separate Android and iOS repositories with the same structure
- **Date:** 2026-11-10
- **Decision:** Keep Android and iOS as two repositories with identical module/epic layouts.
- **Reason:** Simpler while learning; one driver and one locator style per repo.
- **Alternatives:** One combined repo with `locators/android` and `locators/ios`.
- **Impact:** BasePage, conftest and skeletons exist twice; a matching structure keeps a later merge possible.

## D-2: Seven modules mirrored across locators/, pages/ and testcases/
- **Date:** 2026-11-10
- **Decision:** Modules pre_signin, dashboard, payments, accounts, side_menu, account_opening, services; epics are folders under `testcases/<module>/`.
- **Reason:** Matches the module sheet (Module → Epic → Sub-feature).
- **Alternatives:** Only payments/accounts; one test file per epic.
- **Impact:** Features are easy to locate; tests can be selected by folder.

## D-3: One page and one locator file per screen; shared components
- **Date:** 2026-11-10
- **Decision:** Pages and locators are per screen, flat inside the module folder; reusable UI lives in `components/`.
- **Reason:** One screen is used by many tests (FT, IBFT and Raast share Pay Anyone screens).
- **Alternatives:** One page per test folder or sub-feature.
- **Impact:** Each UI change is fixed in one place. Add epic subfolders in `pages/` only when an epic has 3+ screens.

## D-4: Tests use pages only
- **Date:** 2026-11-10
- **Decision:** Tests never import locators or call `driver.find_element`; pages never assert.
- **Reason:** Separation of concerns; locator changes don't touch tests.
- **Alternatives:** Locators inside tests.
- **Impact:** Enforced by AGENTS.md and the page-object skill.

## D-5: Credentials only from .env via config/settings.py
- **Date:** 2026-11-10
- **Decision:** `get_credentials()` reads only the gitignored `.env`, and raises a clear error if a value is missing.
- **Reason:** Credentials had been committed in code; banking data must never be in Git.
- **Alternatives:** Shell environment variables; a secret manager.
- **Impact:** CI will need a `.env` file or a later change to also read environment variables.

## D-6: Explicit waits only
- **Date:** 2026-11-10
- **Decision:** `WebDriverWait` only; no implicit waits; no `time.sleep` in new code.
- **Reason:** Sleeps are slow and flaky; mixing waits gives unpredictable timing.
- **Alternatives:** Implicit wait; fixed sleeps.
- **Impact:** Existing sleeps in login and schedule are marked for removal.

## D-7: noReset true
- **Date:** 2026-11-10
- **Decision:** `appium:noReset: true`.
- **Reason:** The app uses device binding; clearing data would force registration/OTP every run.
- **Alternatives:** `noReset: false` / `fullReset`.
- **Impact:** Each test must bring the app to a known start screen itself.

## D-8: Function-scoped driver fixture
- **Date:** 2026-11-10
- **Decision:** A new Appium session per test, always quit in teardown.
- **Reason:** Isolation over speed while the suite is small.
- **Alternatives:** Class, module or session scope.
- **Impact:** Slower runs; skeletons must not request the fixture before skipping.

## D-9: payment_groups and digital_impact removed
- **Date:** 2026-11-10
- **Decision:** Deleted their empty test, page and locator files.
- **Reason:** Not in the module sheet.
- **Alternatives:** Keep as skeletons.
- **Impact:** The workbook still has a "Digital Impact" sheet. Revisit if the feature is in scope.

## D-10: Skeleton test per sub-feature
- **Date:** 2026-11-10
- **Decision:** One `pytest.skip("TODO")` test file per sub-feature from the module sheet.
- **Reason:** Makes the planned coverage visible in the structure.
- **Alternatives:** Create files only when a test is written.
- **Impact:** Skeletons are not coverage (see the status doc).

## D-11: Agent rules plus platform-specific skills
- **Date:** 2026-11-10
- **Decision:** `AGENTS.md` and `.agents/skills/`; `android-locators` here, `ios-locators` in the iOS repo.
- **Reason:** Consistent agent behaviour; locator rules differ by platform.
- **Alternatives:** Skills per module.
- **Impact:** Skills are per task type, not per module.

## D-12: Shared engineering principles kept identical in both repos
- **Date:** 2026-11-11
- **Decision:** The SHARED block in `AGENTS.md` is identical in Android and iOS, with a version line; platform rules sit below it.
- **Reason:** Two copies drift apart otherwise.
- **Alternatives:** A shared Git submodule.
- **Impact:** After editing the SHARED block, copy it to the other repo and check with `diff`.

## D-13: Git history rewritten into one clean commit
- **Date:** [CONFIRM]
- **Decision:** The repository history was replaced by a single commit (`a64d580`, "Initial clean commit without sensitive history").
- **Reason:** Earlier commits contained credentials.
- **Alternatives:** Keep history and only rotate credentials.
- **Impact:** Earlier commit hashes no longer exist. The leaked password must still be changed, because old clones and caches may hold it.
