import pytest
from pages.side_menu.manage_page import ManagePage

@pytest.mark.side_menu
@pytest.mark.android
def test_manage_bank_account_details(driver):
    """
    TC-ID: TC-SIDE-002
    Validates Manage bank account details.
    """
    page = ManagePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
