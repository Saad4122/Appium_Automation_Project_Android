import pytest
from pages.payments.digital_invoice_page import DigitalInvoicePage

@pytest.mark.payments
@pytest.mark.android
def test_digital_invoice_payment(driver):
    """
    TC-ID: TC-PAY-025
    Validates Digital invoice payment.
    """
    page = DigitalInvoicePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
