import pytest
from pages.payments.remittance_page import RemittancePage

@pytest.mark.payments
@pytest.mark.android
def test_remittance_receive(driver):
    """
    TC-ID: TC-PAY-022
    Validates Receive remittance.
    """
    page = RemittancePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
