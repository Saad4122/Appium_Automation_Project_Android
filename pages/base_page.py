import time
from typing import Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

class BasePage:
    """Base class for all Page Objects in the UBL Digital automation framework."""
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, locator: Tuple[str, str]):
        """Finds a single element after waiting for its presence."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: Tuple[str, str]):
        """Waits for an element to be clickable and performs a click."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator: Tuple[str, str], text: str, sensitive: bool = False):
        """
        Clears existing content and inputs text. Redacts logs for sensitive data.
        """
        log_text = "[REDACTED]" if sensitive else text
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def is_element_displayed(self, locator: Tuple[str, str]) -> bool:
        """Returns True if the element is visible on the screen, False otherwise."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except Exception:
            return False

    def tap_coordinate(self, x: int, y: int):
        """W3C standard touch interaction mapping coordinate-based tap."""
        # Coordinate tap retained for legacy flows; replace with locators when Android XML is available.
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def long_press_bypass(self, x: int, y: int, duration: float = 5.0):
        """Native gesture runner to bypass secure system landing screens."""
        # TODO(android): needs Android page source (replaces iOS mobile: touchAndHold)
        long_press_params = {"x": x, "y": y, "duration": duration}
        self.driver.execute_script("mobile: touchAndHold", long_press_params)
