from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:
    """Locator definitions for UBL Digital Sign-In / Login screen."""
    # TODO(android): needs Android page source (replaces XCUIElementTypeTextField)
    USERNAME_FIELD = (AppiumBy.CLASS_NAME, "XCUIElementTypeTextField")
    # TODO(android): needs Android page source (replaces XCUIElementTypeSecureTextField)
    PASSWORD_FIELD = (AppiumBy.CLASS_NAME, "XCUIElementTypeSecureTextField")
    SIGN_IN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Sign In")

# Backward compatibility alias
AuthLocators = LoginLocators
