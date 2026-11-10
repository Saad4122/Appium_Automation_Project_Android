import pytest
from pages.accounts.list_of_accounts_page import ListOfAccountsPage

@pytest.mark.accounts
@pytest.mark.android
def test_list_of_accounts_manage_account(driver):
    """
    TC-ID: TC-ACC-015
    Validates Manage linked account.
    """
    page = ListOfAccountsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
