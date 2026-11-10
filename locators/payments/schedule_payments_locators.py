from appium.webdriver.common.appiumby import AppiumBy

class SchedulePaymentsLocators:
    """Locators for Schedule Payments screen."""
    # TODO(android): needs Android page source (replaces placeholder locators)
    PAYMENTS_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Payments")
    SCHEDULE_PAYMENTS_OPTION = (AppiumBy.ACCESSIBILITY_ID, "Schedule Payments")
    CREATE_SCHEDULE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Create Schedule")
    SELECT_BENEFICIARY_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Select Beneficiary")
    FIRST_BENEFICIARY_ITEM = (AppiumBy.XPATH, "//TODO_FIRST_BENEFICIARY")
    AMOUNT_INPUT_FIELD = (AppiumBy.XPATH, "//TODO_AMOUNT_INPUT")
    FREQUENCY_SELECT = (AppiumBy.ACCESSIBILITY_ID, "Frequency")
    MONTHLY_FREQUENCY_ITEM = (AppiumBy.XPATH, "//TODO_MONTHLY_FREQUENCY")
    START_DATE_SELECTOR = (AppiumBy.ACCESSIBILITY_ID, "Start Date")
    END_DATE_SELECTOR = (AppiumBy.ACCESSIBILITY_ID, "End Date")
    PROCEED_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Proceed")
    CONFIRM_OTP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Confirm OTP")
    SUCCESS_BANNER = (AppiumBy.XPATH, "//TODO_SUCCESS_BANNER")

