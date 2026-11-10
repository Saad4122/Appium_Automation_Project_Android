import pytest
from pages.payments.bills_payments_page import BillsPaymentsPage

@pytest.mark.payments
@pytest.mark.android
def test_bills_payments_bill_payment(driver):
    """
    TC-ID: TC-PAY-006
    Validates Bill payment.
    """
    page = BillsPaymentsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
