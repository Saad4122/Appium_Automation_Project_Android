import pytest
from pages.payments.pay_anyone_page import PayAnyonePage

@pytest.mark.payments
@pytest.mark.android
def test_pay_anyone_interbank_transfer(driver):
    """
    TC-ID: TC-PAY-003
    Validates IBFT transfer.
    """
    page = PayAnyonePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
