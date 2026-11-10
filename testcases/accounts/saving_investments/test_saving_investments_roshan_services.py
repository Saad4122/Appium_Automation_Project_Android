import pytest
from pages.accounts.saving_investments_page import SavingInvestmentsPage

@pytest.mark.accounts
@pytest.mark.android
def test_saving_investments_roshan_services(driver):
    """
    TC-ID: TC-ACC-020
    Validates Roshan Digital Account services.
    """
    page = SavingInvestmentsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
