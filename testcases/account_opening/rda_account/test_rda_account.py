import pytest
from pages.account_opening.rda_account_page import RdaAccountPage

@pytest.mark.account_opening
@pytest.mark.android
def test_rda_account_onboarding(driver):
    """
    TC-ID: TC-OPEN-002
    Validates Roshan Digital Account onboarding.
    """
    page = RdaAccountPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
