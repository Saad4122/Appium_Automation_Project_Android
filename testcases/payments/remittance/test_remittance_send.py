import pytest
from pages.payments.remittance_page import RemittancePage

@pytest.mark.payments
@pytest.mark.android
def test_remittance_send(driver):
    """
    TC-ID: TC-PAY-023
    Validates Send remittance.
    """
    page = RemittancePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
