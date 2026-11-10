import pytest
from pages.side_menu.accounts_payments_page import AccountsPaymentsPage

@pytest.mark.side_menu
@pytest.mark.android
def test_accounts_payments_qr_default_account(driver):
    """
    TC-ID: TC-SIDE-007
    Validates QR default account.
    """
    page = AccountsPaymentsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
