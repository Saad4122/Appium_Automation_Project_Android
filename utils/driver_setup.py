from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

ANDROID_CAPS = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "Galaxy A51",
#    "appium:udid": "PUT_ADB_SERIAL_HERE",          # from: adb devices
    "appium:appPackage": "app.com.brd",
    "appium:appActivity": "app.com.brd.presentation.main.MainActivity",
    "appium:noReset": True,
    "appium:newCommandTimeout": 300,
    "appium:disableWindowAnimation": True,
    "appium:autoGrantPermissions": False,
}

def get_driver(platform: str = "android"):
    """
    Initializes and returns the Appium driver session.
    platform: "android" (default) or "ios"
    """
    platform = platform.lower()
    if platform == "android":
        options = UiAutomator2Options().load_capabilities(ANDROID_CAPS)
    print(f"Connecting to Appium Server and launching {platform} session...")
    return webdriver.Remote(APPIUM_SERVER_URL, options=options)