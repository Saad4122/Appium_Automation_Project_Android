import time
from pages.base_page import BasePage
from locators.pre_signin.login_locators import LoginLocators

class LoginPage(BasePage):
    """Page object representing UBL Digital Sign-In / Login Screen."""
    
    def unlock_secure_landing_screen(self):
        """Bypasses application landing splash mask using coordinate anchor."""
        # TODO(android): needs Android page source (replaces coordinate bypass 201, 205)
        print("Executing 5-second long press to unlock login layout...")
        self.long_press_bypass(201, 205, duration=5.0)
        time.sleep(2.5)

    def execute_secure_login(self, username: str, password: str):
        """Inputs user credentials, manages keyboard state, and triggers submission."""
        # 1. Focus and input username field
        # TODO(android): needs Android page source (replaces tap coordinate 186, 194)
        print("Entering username...")
        self.tap_coordinate(186, 194)
        time.sleep(0.5)
        self.driver.find_element(*LoginLocators.USERNAME_FIELD).send_keys(username)
        
        # 2. Keyboard dismissal fallback handling logic
        try: 
            self.driver.hide_keyboard()
        except Exception:
            # TODO(android): needs Android page source (replaces tap coordinate 5, 100)
            self.tap_coordinate(5, 100) 
        time.sleep(1)

        # 3. Focus and input secure password field
        # TODO(android): needs Android page source (replaces tap coordinate 48, 370)
        print("Entering password...")
        self.tap_coordinate(48, 370)
        time.sleep(0.5)
        self.driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        time.sleep(0.5)

        # 4. Trigger target submission button click handler
        print("Clicking the Sign-In button...")
        self.driver.find_element(*LoginLocators.SIGN_IN_BUTTON).click()
        time.sleep(8)
