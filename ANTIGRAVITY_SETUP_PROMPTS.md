# UBL Digital Android Automation: Antigravity Setup Prompts

How to use this file:
1. Put this file in your project root.
2. Paste **Prompt 0 (Ground Rules)** first, in a new Antigravity chat.
3. Then paste Prompts 1 to 7 **one at a time**. Do not paste the next one until you have checked the result with the "You check" list under each prompt.
4. Commit after each prompt that passes your check, so you can undo one step without losing the others.

Before you start (things only you can do):
- [ ] Change the password of the account that was committed to GitHub.
- [ ] Have `adb devices` showing your Galaxy A51.
- [ ] Have the app open on the login screen in Appium Inspector (needed for Prompt 5).

---

## Prompt 0: Ground rules (paste first, once per chat)

```
You are working in my Appium + Python + Pytest mobile automation framework for the
UBL Digital banking app. Read these rules and follow them for every task in this chat.

PROJECT FACTS
- Platform: ANDROID ONLY. Driver: UiAutomator2. Device: Samsung Galaxy A51 (real device).
- App package: app.com.brd
- App activity: app.com.brd.presentation.main.MainActivity
- Architecture: Page Object Model. Folders: locators/, pages/, testcases/, utils/, reports/.
  Each of locators/, pages/, testcases/ is split into payments/ and accounts/.
- Remove anything iOS-specific (XCUITest, XCUIElementType*, mobile: touchAndHold,
  bundleId, iPhone coordinates) when you touch a file. Do not add iOS support.

HARD RULES
1. Never write passwords, PINs, OTPs, usernames or tokens into any file. Credentials come
   only from environment variables loaded from a gitignored .env file.
2. Never print or log a sensitive value. Log "[REDACTED]" instead.
3. Never invent locators, resource-ids or accessibility ids. If you do not have the real
   Android page source XML for a screen, put a clearly named TODO placeholder and tell me.
4. Do not run any test or script that logs into the app or performs a payment unless I
   explicitly say "run it". You may run: python -m py_compile, pytest --collect-only,
   pip list, and other read-only checks.
5. Do not git push. Do not rewrite git history. You may stage and commit only if I ask.
6. Before deleting or moving any file, list what you will delete/move and wait for my "ok".
7. Make small, focused changes. Do not reformat files you are not otherwise changing.
8. Use explicit waits (WebDriverWait + expected_conditions). No time.sleep() in pages or
   tests. No implicit waits. No bare "except:".
9. Do not use screen coordinates when an element locator is possible.
10. Use the deprecated-free APIs: W3C actions and "mobile:" commands. No TouchAction.

AFTER EVERY TASK, REPLY WITH
- Files created / changed / deleted (full paths)
- What you changed in each file and why (1-2 lines each)
- Commands you ran and their output
- Anything you could not do, and what you need from me
- Status: say IMPLEMENTED (code written) unless you actually ran it on the device.

Reply "Rules understood" and then wait for my first task.
```

---

## Prompt 1: Inspect only (no changes)

```
TASK 1: Inspect the project. Do NOT change any file.

1. Print the full folder tree (ignore .git, __pycache__, appium_env, .DS_Store).
2. For every .py file, tell me: empty or not, and one line on what it does.
3. List every place that contains: hardcoded credentials, iOS-specific code,
   time.sleep, screen coordinates, bare "except:", or duplicated capabilities.
   For credentials, show only the file and line number, NEVER the value.
4. Run: python3 --version, pip list (only appium, selenium, pytest, python-dotenv lines),
   and if available: appium -v, appium driver list --installed.
5. Report which files import from which (pages -> locators, tests -> pages, etc.).
```

**You check:** the report matches what you know. Note the versions, because you'll need them for `ENVIRONMENT.md`.

---

## Prompt 2: Security cleanup and config

```
TASK 2: Security cleanup and configuration.

1. List these for deletion and wait for my ok:
   - the root file named "test" (old iOS prototype, no extension)
   - config.py (contains hardcoded credentials)
   - pages/payments/login_page.py (empty duplicate of pages/login_page.py)
   - all .DS_Store files
   - report.html and reports/*.html (generated reports, may contain account data)

2. Create config/__init__.py (empty) and config/settings.py that:
   - loads a .env file using python-dotenv (add python-dotenv to requirements.txt)
   - exposes a function get_credentials() that returns (username, password) from
     env vars UBL_USERNAME and UBL_PASSWORD
   - raises a clear RuntimeError naming the missing variable if either is missing
   - never prints the values

3. Create .env.example in the project root with:
   UBL_USERNAME=
   UBL_PASSWORD=
   (no real values)

4. Replace .gitignore with one that covers (deduplicated):
   appium_env/, venv/, .venv/, __pycache__/, *.pyc, .env, .DS_Store,
   report.html, reports/*.html, screenshots/, logs/, page_source/, *.mov, *.mp4,
   .pytest_cache/

5. Update every file that imported from the old config.py to use
   config.settings.get_credentials() instead. Remove any hardcoded username/password
   passed directly in tests (e.g. in testcases/payments/test_06_schedule_payments.py).

6. Create requirements.txt from the versions actually installed (pip freeze filtered to
   Appium-Python-Client, selenium, pytest, python-dotenv). Pin exact versions. Do not guess.

7. Run python -m py_compile on every changed .py file.
```

**You check:**
- [ ] `grep -rn "password" --include=*.py .` shows no real password.
- [ ] You created your own `.env` (copied from `.env.example`) and filled it in. **Don't commit it.**
- [ ] `git status` does **not** list `.env`.

---

## Prompt 3: Driver, root conftest, pytest.ini

```
TASK 3: Driver setup, fixtures and pytest configuration.

1. Make utils/driver_setup.py Android-only with exactly this content:

from appium import webdriver
from appium.options.android import UiAutomator2Options

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

ANDROID_CAPS = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "Galaxy A51",
    "appium:udid": "PUT_ADB_SERIAL_HERE",
    "appium:appPackage": "app.com.brd",
    "appium:appActivity": "app.com.brd.presentation.main.MainActivity",
    "appium:noReset": True,
    "appium:newCommandTimeout": 300,
    "appium:disableWindowAnimation": True,
    "appium:autoGrantPermissions": False,
}


def get_driver():
    """Initializes and returns the Appium Android driver session."""
    options = UiAutomator2Options().load_capabilities(ANDROID_CAPS)
    print("Connecting to Appium Server and launching Android session...")
    return webdriver.Remote(APPIUM_SERVER_URL, options=options)

   Run "adb devices". If exactly one device is listed, replace PUT_ADB_SERIAL_HERE with
   its serial. Otherwise leave the placeholder and tell me.

2. Create conftest.py in the PROJECT ROOT with a function-scoped "driver" fixture:
   - calls get_driver()
   - yields the driver
   - always calls driver.quit() in teardown (wrap quit in try/except Exception)
   Add short comments explaining yield and teardown (I am learning).

3. Create pytest.ini in the project root:
   - testpaths = testcases
   - pythonpath = .   (requires pytest 7+; check the installed version and tell me
     if it is older)
   - addopts = -v --strict-markers
   - register these markers with one-line descriptions:
     smoke, regression, critical, android,
     auth, payments, accounts,
     pay_anyone, bill_payment, mobile_topup, qr_payments, schedule_payments,
     donation_zakat, global_remittance, digital_invoices, payment_groups,
     payment_requests, mobile_packages, beneficiary_mgmt,
     list_of_accounts, statement, card_management, cheque_management,
     certificates, saving_investments, digital_transactions, digital_impact,
     state_changing (test changes data/balance - run only when selected),
     consumable (uses limited data such as limits or attempts),
     quarantined (unstable - must have owner and reason in docstring)

4. Remove any sys.path.append hacks from test files (pythonpath in pytest.ini replaces them).

5. Create testcases/test_00_driver_smoke.py with one test:
   test_driver_starts_android_session(driver) that asserts
   driver.current_package == "app.com.brd". Mark it @pytest.mark.smoke and android.

6. Run: pytest --collect-only  and show me the output. Do NOT run the tests.
```

**You check:** start Appium in another terminal, then run it yourself:
```bash
pytest testcases/test_00_driver_smoke.py
```
Expected: the app opens on the A51 and the test shows `PASSED`.

---

## Prompt 4: Upgrade BasePage (Android)

```
TASK 4: Rewrite pages/base_page.py as an Android BasePage. Keep the class name BasePage
and the constructor signature __init__(self, driver).

Include these methods, each with a short docstring:
- __init__(self, driver, timeout=15): store driver and a WebDriverWait
- find(self, locator): wait for presence, return element
- find_visible(self, locator): wait for visibility, return element
- click(self, locator): wait for clickable, then click
- type_text(self, locator, text, sensitive=False): wait clickable, click, clear,
  send_keys. Log "Typing into <locator>: [REDACTED]" when sensitive=True, otherwise
  log the text. Never log sensitive values.
- get_text(self, locator)
- is_displayed(self, locator, timeout=5): return True/False, never raise
- long_press(self, locator, duration_ms=5000): use
  driver.execute_script("mobile: longClickGesture", {"elementId": el.id, "duration": duration_ms})
- hide_keyboard_if_shown(self): only hide if driver.is_keyboard_shown()
- scroll_to_text(self, text): use AppiumBy.ANDROID_UIAUTOMATOR with
  new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("..."))
- tap_coordinate(self, x, y): keep the existing W3C implementation, but add a docstring
  saying it is a LAST RESORT only.

Remove long_press_bypass (iOS mobile: touchAndHold).
Use the standard logging module (logger = logging.getLogger(__name__)), not print.
Use type hints. No time.sleep. No bare except.

Then update pages/payments/schedule_payments_page.py so that SchedulePaymentsPage
inherits BasePage and uses its click/type_text instead of its own _click_element and
_clear_and_type_ios helpers. Remove handle_quick_login from it (login belongs to
LoginPage). Move the final assert out of the page: the page method should return
True/False (e.g. is_success_banner_displayed()), and the test should assert.
Leave its locators as TODO (the locators file is empty; do not invent values).

Run py_compile on changed files.
```

**You check:** read `base_page.py` and make sure you understand every method. Ask me about any you don't.

---

## Prompt 5: Restructure testcases into feature folders

```
TASK 5: Restructure testcases/ into one folder per feature. Pages and locators stay where
they are. First show me the full old-path -> new-path mapping and wait for my ok.

Target layout (each folder gets an empty __init__.py):

testcases/
  conftest.py                      (empty for now, with a comment: shared fixtures go here)
  test_00_driver_smoke.py          (stays)
  auth/
    test_login.py                  (from testcases/test_01_auth.py)
  payments/
    conftest.py                    (placeholder comment: logged-in + Payments tab fixture)
    pay_anyone/test_pay_anyone.py
    bill_payment/test_bill_payment.py
    mobile_topup/test_mobile_topup.py
    qr_payments/test_qr_payments.py
    schedule_payments/test_schedule_payments.py
    donation_zakat/test_donation_zakat.py
    global_remittance/test_global_remittance.py
    digital_invoices/test_digital_invoices.py
    payment_groups/test_payment_groups.py
    payment_requests/test_payment_requests.py
    mobile_packages/test_mobile_packages.py
    beneficiary_mgmt/test_beneficiary_mgmt.py
  accounts/
    conftest.py                    (placeholder comment)
    list_of_accounts/test_list_of_accounts.py
    statement/test_statement.py
    card_management/test_card_management.py
    cheque_management/test_cheque_management.py
    certificates/test_certificates.py
    saving_investments/test_saving_investments.py
    digital_transactions/test_digital_transactions.py
    digital_impact/test_digital_impact.py

Rules:
- Use "git mv" so history is kept.
- Drop the number prefixes (test_02_, test_accounts_03_ ...).
- Test file names must be unique across the whole project (feature name in the file name).
- Do not change test logic in this task, only move/rename and fix imports.
- Run pytest --collect-only at the end and show the output.
```

**You check:** `pytest --collect-only` shows no errors, and `git status` shows the files as *renamed*, not deleted and re-added.

---

## Prompt 6: Android login (needs page source)

Before pasting: open the login screen in Appium Inspector and save the page source as `page_source/login.xml`. That folder is gitignored. **Blank out any real username or account number in it first.**

```
TASK 6: Convert login to Android.

Use ONLY page_source/login.xml (Android page source of the UBL login screen) for locators.
If an element I need is not in that file, stop and tell me; do not guess.

1. Rewrite locators/auth_locators.py (class AuthLocators) for Android.
   Locator priority: resource-id (AppiumBy.ID) > accessibility id > UiAutomator > XPath.
   Needed: landing screen element for the long-press (if the landing screen exists),
   USERNAME_FIELD, PASSWORD_FIELD, SIGN_IN_BUTTON, and one DASHBOARD_MARKER element that
   only appears after successful login (if not in this XML, leave a TODO and tell me
   I must capture the dashboard page source).
   For each locator add a comment saying which attribute in the XML it came from.

2. Rewrite pages/login_page.py (class LoginPage(BasePage)) for Android:
   - unlock_landing_screen(): BasePage.long_press on the landing element (no coordinates)
   - login(username, password): type_text username, hide_keyboard_if_shown,
     type_text password with sensitive=True, click sign in
   - is_dashboard_displayed() -> bool
   No sleeps, no coordinates, no prints of credentials.

3. Rewrite testcases/auth/test_login.py as a real pytest test:
   - uses the "driver" fixture from the root conftest
   - gets credentials from config.settings.get_credentials()
   - test_login_with_valid_credentials_shows_dashboard: unlock, login, assert dashboard
   - markers: smoke, android, auth
   - docstring with a placeholder for the manual test case ID: "TC-ID: TODO"
   - no try/except swallowing failures; let pytest report failures
   - remove the old manual report-building code from this test (we will hook reporting
     into conftest later)

4. Run py_compile and pytest --collect-only. Do NOT run the test.
```

**You check:** run it yourself:
```bash
pytest testcases/auth/test_login.py
```
If it fails, send me the error, the Appium server log around the failure and the page source. Then we debug together.

---

## Prompt 7: Project documents

```
TASK 7: Create these markdown files in the project root, based ONLY on what actually
exists now. Write [CONFIRM] for anything you do not know. No secrets.

- ARCHITECTURE.md: folder tree, what each layer does (locators -> pages -> tests),
  BasePage method list, driver fixture lifecycle, where config/credentials live.
- ENVIRONMENT.md: Python, Appium, UiAutomator2, Appium-Python-Client, selenium, pytest
  versions (from what you checked), device model, Android version, app package/activity,
  how to run (Appium start command, pytest commands by folder and by marker).
- TEST_AUTOMATION_STATUS.md: table of every feature with status, one of:
  NOT STARTED / IMPLEMENTED / EXECUTED / VERIFIED. Only I can mark EXECUTED or VERIFIED.
  Include known blockers (locators TODO, dashboard marker TODO, etc.).
- DECISIONS.md: record these decisions with reason and alternatives:
  1. Android-only for now (iOS code removed)
  2. One page/locator file per screen; test folders per feature
  3. Credentials via .env + env vars only
  4. Explicit waits only; no sleeps or implicit waits
  5. noReset=True because of device binding; each test must reach a known start screen
```

---

## After setup: how to run

```bash
appium                                         # terminal 1
pytest                                         # everything
pytest testcases/auth                          # one folder
pytest -m smoke                                # by marker
pytest -m "payments and not state_changing"    # safe payment tests only
pytest testcases/auth/test_login.py::test_login_with_valid_credentials_shows_dashboard
```

## If Antigravity does something wrong

- It invented a locator → tell it: "Rule 3: remove invented locators, use TODO."
- It added a password to a file → `git checkout -- <file>`, then repeat Rule 1.
- It changed many unrelated files → `git restore .` and paste the prompt again with
  "only change the files listed".