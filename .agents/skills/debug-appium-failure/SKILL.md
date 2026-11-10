---
name: debug-appium-failure
description: Diagnose a failing or flaky UBL Digital Android Appium test from the pytest error, Appium server log, page source and screenshot, then propose the smallest fix. Use when a test fails, hangs, or the session will not start.
---

# Debug an Appium failure

## Goal
Find the real root cause from evidence and fix it with the smallest change, without
hiding the failure.

## Evidence to collect (ask for what's missing)
- Full pytest output (traceback)
- Appium server log around the failure (start Appium with `appium --log-timestamp`)
- Page source XML at the moment of failure
- Screenshot (may be black, see FLAG_SECURE below)
- `adb devices`, Appium/driver versions from ENVIRONMENT.md

## Steps
1. **Identify:** which test, which page method, which locator/action, expected vs actual screen.
2. **Classify** into exactly one category:
   | Category | Typical signs |
   |---|---|
   | Session/driver | `SessionNotCreatedException`, port in use, device offline, UiAutomator2 server crash |
   | Locator | `NoSuchElementException`, id not in page source |
   | Synchronization | `TimeoutException` but element appears later; loader still visible |
   | Wrong screen/state | page source shows a different screen (popup, update prompt, session expired) |
   | Keyboard/overlay | element covered by keyboard or dialog |
   | Stale element | `StaleElementReferenceException` after screen refresh |
   | Python | `ImportError`, `NameError`, `TypeError`, `AttributeError` |
   | Test data | insufficient balance, limit reached, duplicate beneficiary |
   | App defect | app behaves against requirement (needs evidence) |
   | Security control | black screenshot (FLAG_SECURE), root/emulator detection, device binding, OTP, session limit |
   | Environment | UAT down, network, wrong build installed |
3. **Root cause:** quote the exact log line / XML node that proves it.
4. **Fix:** smallest reliable change. Prefer: correct locator, proper explicit wait,
   handling the real intermediate screen, fixing data setup.
5. **Verify:** give the exact command to re-run one test and what passing looks like.

## Never
- Add `time.sleep` as the fix.
- Wrap in try/except to make it pass, or delete/weaken an assert.
- Add blind retries. A test that passes on rerun is FLAKY: record it in
  TEST_AUTOMATION_STATUS.md.
- Try to bypass FLAG_SECURE, root detection, SSL pinning or device binding.
  Use the `testability-request` skill instead.
- Claim it is fixed unless it was re-run.

## Reply format
1. Error identification
2. Category + root cause (with evidence)
3. Fix (files + diff)
4. Re-run command
5. Status (IMPLEMENTED until the user confirms it passes)
