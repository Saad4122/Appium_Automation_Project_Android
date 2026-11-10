---
name: pytest-journey-test
description: Write pytest test cases for a UBL Digital banking journey (login, Pay Anyone, bill payment, etc.) using fixtures and page objects. Use when the user shares manual test cases or asks to automate a journey.
---

# Pytest journey test

## Goal
Readable tests that describe banking behaviour, use page objects, assert meaningful
results, and can run repeatedly without breaking test data.

## Before writing
1. Get the manual test cases (IDs + steps + expected results). If none, ask.
2. Confirm page objects exist for every screen in the journey (`page-object` skill if not).
3. Classify the data for each test and tell the user:
   - **reusable**: can run any number of times (e.g. viewing a statement)
   - **consumable**: uses limits/attempts/balance (mark `consumable`)
   - **state_changing**: creates/changes records (beneficiary, payment, card block)
     (mark `state_changing`)
4. Decide what the test needs at start (logged in? on Payments tab? existing beneficiary?)
   and which fixture provides it. Put shared setup in the nearest `conftest.py`
   (`testcases/payments/conftest.py` for all payments, feature folder for one feature).

## Rules
- Location: `testcases/<area>/<feature>/test_<feature>_<topic>.py`.
- Name = behaviour: `test_pay_anyone_rejects_amount_above_limit`.
- Docstring: one line of behaviour + `TC-ID: <id>`.
- Markers: always `android` + module marker; add `smoke`/`regression`,
  `state_changing`/`consumable` as applicable. Only registered markers.
- Test data from `test_data/<area>/<feature>.json` (non-secret) or fixtures.
  Credentials only from `config.settings.get_credentials()`.
- Tests call page methods only; no `find_element`, no locators.
- One behaviour per test. Asserts with a message:
  `assert review.is_loaded(), "Review screen did not open after tapping Next"`.
- No try/except around the test body. No sleeps. No order dependency.
- For transactions also consider: back from review, cancel, double tap on confirm,
  repeating the same payment. Add them as separate tests or list them as TODO.
- Do not assert exact balances on shared accounts. Assert change, using `Decimal`.
- A UI "success" message is not proof of settlement. Name asserts honestly
  (`success_screen_shown`, not `payment_completed`).

## Template
```python
# testcases/payments/pay_anyone/test_pay_anyone_review.py
import pytest

from pages.payments.pay_anyone_page import PayAnyonePage


@pytest.mark.android
@pytest.mark.pay_anyone
@pytest.mark.regression
def test_pay_anyone_shows_review_screen_after_valid_amount(payments_home):
    """Valid amount + Next opens the review screen. TC-ID: TODO"""
    page = PayAnyonePage(payments_home)
    page.enter_amount("100")
    page.tap_next()
    assert page.is_review_shown(), "Review screen did not open after tapping Next"
```

## After writing
- Run `pytest --collect-only <path>` and show the output.
- Do NOT run it (state-changing/login) unless the user says "run it".
- Give the exact run commands: by file, by node id, by marker.

## Reply must include
- Test list: name | TC-ID | data type | markers
- Fixtures used/created and where
- Scenarios not automated and why (better as manual/API, or blocked)
