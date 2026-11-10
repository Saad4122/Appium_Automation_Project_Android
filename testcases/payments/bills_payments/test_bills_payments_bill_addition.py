import pytest
from pages.payments.bills_payments_page import BillsPaymentsPage

@pytest.mark.payments
@pytest.mark.android
def test_bills_payments_bill_addition(driver):
    """
    TC-ID: TC-PAY-005
    Validates Bill addition.
    """
    page = BillsPaymentsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
