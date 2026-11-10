import pytest
from pages.payments.qr_pay_page import QrPayPage

@pytest.mark.payments
@pytest.mark.android
def test_qr_pay_receive_static(driver):
    """
    TC-ID: TC-PAY-013
    Validates Receive static QR.
    """
    page = QrPayPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
