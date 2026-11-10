# TEST_AUTOMATION_STATUS.md: UBL Digital Android Automation

_Last reviewed against commit `a64d580` (2026-11-11). Update via the `session-handoff` skill._

## 1. Status legend

| Status | Meaning | Who may set it |
|---|---|---|
| NOT STARTED | Skeleton only (`pytest.skip`) or empty | agent |
| IMPLEMENTED | Test logic written | agent |
| STATICALLY REVIEWED | Code read and checked, not run | agent |
| EXECUTED | Actually run on the device | **user only** |
| VERIFIED | Run, and behaviour confirmed correct | **user only** |

Rules: a skeleton is not coverage. A test without an assertion is not a validated test.

## 2. Summary counts

| Measurement | Count | How counted |
|---|---|---|
| Test files | 89 | `testcases/**/test_*.py` |
| Test functions | 89 | `def test_` |
| Collected by pytest | [CONFIRM] | `python -m pytest --collect-only -q` |
| Skeleton tests (body is `pytest.skip`) | 86 | files containing `pytest.skip` |
| Tests with real interaction code | 3 | smoke, login, schedule payments |
| Tests containing an assertion | 1 | `test_00_driver_smoke.py` |
| EXECUTED | [CONFIRM] (none recorded) | user |
| VERIFIED journeys | 0 | user |

## 3. Status by module and epic

| Module / epic | Test file(s) | Status | Notes |
|---|---|---|---|
| (environment) | `test_00_driver_smoke.py` | IMPLEMENTED | Asserts `current_package == "app.com.brd"`. Not run yet. |
| pre_signin / login | `test_login_sign_in.py` | IMPLEMENTED: **not valid for Android** | iOS locators (`XCUIElementType…`), iPhone coordinates, `mobile: touchAndHold`, 8 sleeps, **no assertion**, **not skipped** |
| pre_signin / login | sign_up, forgot_password, authentication | NOT STARTED | skeletons |
| pre_signin / pre_signin_services | 7 files | NOT STARTED | skeletons |
| dashboard | menu, global_search, ai_voice_command | NOT STARTED | skeletons |
| payments / schedule_payments | `test_schedule_payments.py` | IMPLEMENTED: **not valid for Android** | Guessed accessibility IDs and `//TODO_` XPaths; iOS login inside the page; return value **not asserted**; **not skipped**; marked `state_changing` |
| payments / all other epics | 25 files | NOT STARTED | skeletons |
| accounts | 20 files | NOT STARTED | skeletons |
| side_menu | 22 files | NOT STARTED | skeletons |
| account_opening | 3 files | NOT STARTED | skeletons |
| services | 2 files | NOT STARTED | skeletons |

## 4. Known issues and blockers

| # | Issue | Impact |
|---|---|---|
| 1 | Skeleton tests request the `driver` fixture, so each one opens an Appium session before skipping | A full run starts 86 sessions; without Appium they show as ERROR, not SKIPPED |
| 2 | Login and schedule tests aren't skipped and contain iOS logic | A full run fails both |
| 3 | `BasePage.long_press_bypass` uses the iOS-only `mobile: touchAndHold` | The landing unlock fails on Android |
| 4 | No locator taken from Android page source yet | No journey can run |
| 5 | Real tests have no assertions | A "pass" proves nothing |
| 6 | `get_driver()`: dead iOS branch, unused `XCUITestOptions` import | Crash if called with "ios" |
| 7 | `appium:udid` commented out | Ambiguous with 2+ devices |
| 8 | Report modules not connected; device label says iPhone | No HTML report |
| 9 | No logging; `type_text` doesn't log; login bypasses `type_text` | No step trail; masking unused |
| 10 | No failure evidence (screenshot / page source) | Hard to debug |
| 11 | Priority markers (`critical`, `highest`, `medium`) and `consumable` registered but unused | Can't run by priority |
| 12 | Code TC-IDs (`TC-PAY-001`…) were made up; they don't match the manual workbook | No traceability |
| 13 | `Settings` class unused; capabilities duplicated in `driver_setup.py` | Two config sources |
| 14 | Hard-coded amounts in schedule test/page | Data not reusable |

## 5. Manual test case source

- File: `UBL 13 App TestCases.xlsx` (kept outside the repo, attached to the claude.ai Project).
- About 1,312 cases across 28 sheets.
- Known workbook issues:
  - **No Login / Sign-in sheet**
  - The **Schedule Payment** sheet is an exact copy of **Add Bills**
  - **Payment Request** and **Pay Bills** are empty
  - IDs aren't unique across sheets (`TC001`, `J1-TC001`, `TC_AB_001` repeat)
  - Each sheet uses its own ID style
  - `Status Android` column empty
- No automated test currently references a workbook ID.

## 6. Developer / testability dependencies

- None raised yet.

## 7. Next steps (in order)

1. Run the smoke test; record the result here (user marks EXECUTED).
2. Capture Android page source: landing, login, dashboard (`page_source/`, gitignored, redacted).
3. Fix BasePage for Android (long-press, logging with masking, get_text, scroll, keyboard).
4. Make skeleton tests skip without opening a session; skip login and schedule until converted.
5. Convert login (locators → `LoginPage` → test with assertion). Write Sign-in manual cases first.
6. Journeys by priority: Critical → Highest → Medium, mapped to workbook TC-IDs.
