import pytest

@pytest.mark.smoke
@pytest.mark.android
def test_driver_starts_android_session(driver):
    """
    TC-ID: SMOKE-001
    Validates that the Appium driver initializes successfully on Android
    and the target banking application package is mounted in foreground.
    """
    assert driver.current_package == "app.com.brd"

