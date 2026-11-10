import pytest
from config.settings import get_credentials
from pages.pre_signin.login_page import LoginPage

@pytest.mark.auth
@pytest.mark.smoke
@pytest.mark.android
def test_login_sign_in(driver):
    """
    TC-ID: AUTH-001
    Validates the standard sign-in flow using credentials from config settings.
    """
    login_page = LoginPage(driver)

    # 1. Bypass landing splash
    login_page.unlock_secure_landing_screen()

    # 2. Retrieve credentials securely from environment
    credentials = get_credentials()
    login_page.execute_secure_login(credentials["username"], credentials["password"])
