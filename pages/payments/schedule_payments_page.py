import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.payments.schedule_payments_locators import SchedulePaymentsLocators

class SchedulePaymentsPage(BasePage):
    """Page object for Schedule Payments flow."""

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 15)

    def _clear_and_type_ios(self, locator, text):
        """Finds an element, clears any pre-filled data using backspaces, and types text."""
        # TODO(android): needs Android page source (iOS specific backspace clearing)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        
        current_value = element.get_attribute("value")
        if current_value and current_value not in ["Username", "Password", "0"]:
            for _ in range(len(current_value)):
                element.send_keys("\b")
        element.send_keys(text)
        time.sleep(0.5)

    def _click_element(self, locator):
        """Helper to wait for an element to be clickable and click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        time.sleep(0.5)

    def handle_quick_login(self, username, password):
        """Temporary helper to handle login fields before the core flow."""
        # TODO(android): needs Android page source (replaces XCUIElementTypeTextField)
        username_field = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="username"]')
        # TODO(android): needs Android page source (replaces XCUIElementTypeSecureTextField)
        password_field = (AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@name="password"]')
        login_button = (AppiumBy.ACCESSIBILITY_ID, "Login Button")
        
        self._clear_and_type_ios(username_field, username)
        self._clear_and_type_ios(password_field, password)
        self._click_element(login_button)

    def execute_schedule_transfer_flow(self, amount="1000"):
        """Executes the scheduled transfer sequence."""
        # 1. Navigate through dashboards
        self._click_element(SchedulePaymentsLocators.PAYMENTS_NAV_BUTTON)
        self._click_element(SchedulePaymentsLocators.SCHEDULE_PAYMENTS_OPTION)
        self._click_element(SchedulePaymentsLocators.CREATE_SCHEDULE_BUTTON)
        
        # 2. Select Beneficiary
        self._click_element(SchedulePaymentsLocators.SELECT_BENEFICIARY_DROPDOWN)
        self._click_element(SchedulePaymentsLocators.FIRST_BENEFICIARY_ITEM)
        
        # 3. Handle Amount Field
        self._clear_and_type_ios(SchedulePaymentsLocators.AMOUNT_INPUT_FIELD, amount)
        
        # 4. Set Schedule Parameters
        self._click_element(SchedulePaymentsLocators.FREQUENCY_SELECT)
        self._click_element(SchedulePaymentsLocators.MONTHLY_FREQUENCY_ITEM)
        
        self._click_element(SchedulePaymentsLocators.START_DATE_SELECTOR)
        self._click_element(SchedulePaymentsLocators.END_DATE_SELECTOR)
        
        # 5. Trigger Actions & Finalize
        self._click_element(SchedulePaymentsLocators.PROCEED_BUTTON)
        self._click_element(SchedulePaymentsLocators.CONFIRM_OTP_BUTTON)
        
        # 6. Verify success banner state
        return self.wait.until(EC.presence_of_element_located(SchedulePaymentsLocators.SUCCESS_BANNER)).is_displayed()
