import pytest
from pages.account_opening.smart_account_page import SmartAccountPage

@pytest.mark.account_opening
@pytest.mark.android
def test_smart_account_onboarding(driver):
    """
    TC-ID: TC-OPEN-003
    Validates Asaan digital smart account onboarding.
    """
    page = SmartAccountPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
