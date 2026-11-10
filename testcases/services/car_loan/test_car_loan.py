import pytest
from pages.services.car_loan_page import CarLoanPage

@pytest.mark.services
@pytest.mark.android
def test_car_loan_application(driver):
    """
    TC-ID: TC-SRV-001
    Validates Car loan application.
    """
    page = CarLoanPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
