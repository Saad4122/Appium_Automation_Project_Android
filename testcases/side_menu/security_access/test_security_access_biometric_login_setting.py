import pytest
from pages.side_menu.security_access_page import SecurityAccessPage

@pytest.mark.side_menu
@pytest.mark.android
def test_security_access_biometric_login_setting(driver):
    """
    TC-ID: TC-SIDE-012
    Validates Biometric login setting.
    """
    page = SecurityAccessPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
