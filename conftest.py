import pytest
from utils.driver_setup import get_driver

@pytest.fixture(scope="function")
def driver():
    """
    Function-scoped driver fixture.
    Initializes an Android Appium session before each test and guarantees
    that driver.quit() is called upon test completion.
    """
    appium_driver = get_driver(platform="android")
    try:
        yield appium_driver
    finally:
        try:
            appium_driver.quit()
        except Exception:
            pass

