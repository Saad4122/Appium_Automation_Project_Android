---
name: android-locators
description: Build or update Android locator classes in locators/ from Appium page source XML for a UBL Digital screen. Use when the user shares page source, asks for locators, or a page object needs new elements.
---

# Android locators from page source

## Goal
Produce a locator class for ONE screen, using only elements that really exist in the
Android page source XML the user provided.

## Inputs you need
- Page source XML for the screen (e.g. `page_source/<screen>.xml`). If missing, STOP and
  ask for it. Tell the user: Appium Inspector -> open the screen -> "Copy XML Source" ->
  save to `page_source/<screen>.xml` -> blank out real names, account numbers, balances.
- The list of elements the journey needs (ask if unclear).

## Steps
1. Read the XML. For each element needed, find its node and note: `resource-id`,
   `content-desc`, `text`, `class`, `clickable`, `password`, `bounds`.
2. Pick the locator using this priority:
   1. `resource-id` (unique) -> `(AppiumBy.ID, "app.com.brd:id/xyz")`
   2. `content-desc` (unique) -> `(AppiumBy.ACCESSIBILITY_ID, "...")`
   3. UiAutomator -> `(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("...").instance(0)')`
      only if nothing above is unique
   4. XPath with attributes, never pure index paths
3. Check uniqueness: the chosen value must appear once in the XML. If it appears more
   than once, say so and pick a more specific strategy.
4. Flag weak elements: no resource-id and no content-desc, or text-only.
   These go in the "Testability gaps" list in your reply.
5. Write the file `locators/<area>/<screen>_locators.py`:

```python
# locators/payments/pay_anyone_locators.py
from appium.webdriver.common.appiumby import AppiumBy


class PayAnyoneLocators:
    """Pay Anyone screen. Source: page_source/pay_anyone.xml"""

    # resource-id
    AMOUNT_INPUT = (AppiumBy.ID, "app.com.brd:id/et_amount")
    # content-desc
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Next")
    # TODO: not in page source - need XML of the review screen
    REVIEW_TITLE = (AppiumBy.ID, "app.com.brd:id/TODO_review_title")
```
(The ids above are examples of FORMAT only. Never copy them.)

6. Constant names: UPPER_SNAKE, `<ELEMENT>_<TYPE>`: `_INPUT`, `_BUTTON`, `_LABEL`, `_LIST`, `_ITEM`.
7. Above each locator, a one-line comment saying which attribute it came from.

## Constraints
- Never invent ids. Unknown = `TODO_` placeholder + note in reply.
- Never put data (names, amounts, account numbers) in a locator.
- Do not use `bounds` coordinates as locators.
- If the screen is a WebView (class `android.webkit.WebView` with little inside), say so;
  native locators will not work there.

## Reply must include
- Table: constant | strategy | value | uniqueness OK? | source attribute
- Testability gaps (elements needing a resource-id from developers)
- TODOs and which page source is still needed
