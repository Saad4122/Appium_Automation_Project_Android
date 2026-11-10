import pytest
from pages.payments.pay_anyone_page import PayAnyonePage

@pytest.mark.payments
@pytest.mark.android
def test_pay_anyone_raast_transfer(driver):
    """
    TC-ID: TC-PAY-004
    Validates Raast payment.
    """
    page = PayAnyonePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
