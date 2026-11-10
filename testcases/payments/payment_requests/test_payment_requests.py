import pytest
from pages.payments.payment_requests_page import PaymentRequestsPage

@pytest.mark.payments
@pytest.mark.android
def test_payment_requests_creation(driver):
    """
    TC-ID: TC-PAY-018
    Validates Payment request.
    """
    page = PaymentRequestsPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
