import pytest
from pages.accounts.card_management_page import CardManagementPage

@pytest.mark.accounts
@pytest.mark.android
def test_card_management_request_virtual_wiz(driver):
    """
    TC-ID: TC-ACC-005
    Validates Request virtual Wiz card.
    """
    page = CardManagementPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
