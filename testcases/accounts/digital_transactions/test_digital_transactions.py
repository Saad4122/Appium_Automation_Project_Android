import pytest
from pages.accounts.digital_transactions_page import DigitalTransactionsPage

@pytest.mark.accounts
@pytest.mark.android
def test_digital_transactions_history(driver):
    """
    TC-ID: TC-ACC-006
    Validates Digital transactions history.
    """
    page = DigitalTransactionsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
