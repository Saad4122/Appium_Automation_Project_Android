import pytest
from pages.payments.mobile_payments_page import MobilePaymentsPage

@pytest.mark.payments
@pytest.mark.android
def test_mobile_payments_topup(driver):
    """
    TC-ID: TC-PAY-010
    Validates Mobile topup.
    """
    page = MobilePaymentsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
