import pytest
from pages.side_menu.accounts_payments_page import AccountsPaymentsPage

@pytest.mark.side_menu
@pytest.mark.android
def test_accounts_payments_raast_link_unlink(driver):
    """
    TC-ID: TC-SIDE-010
    Validates Raast link unlink.
    """
    page = AccountsPaymentsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
