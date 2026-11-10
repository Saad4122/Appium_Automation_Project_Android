import pytest
from pages.accounts.account_statement_page import AccountStatementPage

@pytest.mark.accounts
@pytest.mark.android
def test_account_statement_download(driver):
    """
    TC-ID: TC-ACC-002
    Validates Account statement download.
    """
    page = AccountStatementPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
