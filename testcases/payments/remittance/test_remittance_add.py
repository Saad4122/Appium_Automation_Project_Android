import pytest
from pages.payments.remittance_page import RemittancePage

@pytest.mark.payments
@pytest.mark.android
def test_remittance_add_beneficiary(driver):
    """
    TC-ID: TC-PAY-024
    Validates Add remittance beneficiary.
    """
    page = RemittancePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
