import pytest
from pages.accounts.card_management_page import CardManagementPage

@pytest.mark.accounts
@pytest.mark.android
def test_card_management_request_physical(driver):
    """
    TC-ID: TC-ACC-004
    Validates Request physical debit card.
    """
    page = CardManagementPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
