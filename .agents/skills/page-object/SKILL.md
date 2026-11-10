---
name: page-object
description: Create or update a UBL Digital page object class in pages/ that inherits BasePage and uses a locator class. Use when adding screen interactions or converting old script code into the POM.
---

# Page object

## Goal
One class per screen that exposes clear, reusable actions and state checks, built on
BasePage, with no asserts, no sleeps and no secrets.

## Before writing
1. Read `pages/base_page.py`. Use its methods (`click`, `type_text`, `find_visible`,
   `get_text`, `is_displayed`, `long_press`, `hide_keyboard_if_shown`, `scroll_to_text`).
   Do not re-implement them in the page.
2. Read the matching `locators/<area>/<screen>_locators.py`. If the locators do not
   exist yet, use the `android-locators` skill first.
3. Check the page file does not already have the method you plan to add.

## Rules
- `class XxxPage(BasePage):`, file `pages/<area>/<screen>_page.py`.
- Methods are **actions** (`enter_amount`, `tap_next`) or **state checks**
  (`is_loaded`, `is_error_shown`, `get_amount_text`). State checks return values, they don't assert.
- Every page has `is_loaded() -> bool` that checks one element unique to that screen.
- A method that navigates to another screen may return that screen's page object.
- Sensitive inputs (password, PIN, OTP, CNIC, account number) use
  `type_text(locator, value, sensitive=True)`.
- Amounts: return `decimal.Decimal` via the shared amount parser (if one doesn't exist,
  propose `utils/amounts.py` and ask before creating it).
- No `time.sleep`, no `print`, use `logging`. No `assert`. No bare `except`.
- No coordinates unless the user approves; then add a comment why.
- Use type hints and a one-line docstring per method.

## Template
```python
# pages/payments/pay_anyone_page.py
import logging
from decimal import Decimal

from pages.base_page import BasePage
from locators.payments.pay_anyone_locators import PayAnyoneLocators as L

logger = logging.getLogger(__name__)


class PayAnyonePage(BasePage):
    """Pay Anyone - enter amount screen."""

    def is_loaded(self) -> bool:
        """True when the Pay Anyone amount screen is shown."""
        return self.is_displayed(L.AMOUNT_INPUT)

    def enter_amount(self, amount: str) -> None:
        """Type the transfer amount."""
        self.type_text(L.AMOUNT_INPUT, amount)
        self.hide_keyboard_if_shown()

    def tap_next(self) -> None:
        """Go to the review screen."""
        self.click(L.NEXT_BUTTON)
```

## Reply must include
- Public methods added/changed (name, purpose)
- Which BasePage methods were reused
- Locators still TODO
- Status: IMPLEMENTED (unless actually executed)
