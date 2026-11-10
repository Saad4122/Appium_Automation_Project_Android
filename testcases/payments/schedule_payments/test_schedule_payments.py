import pytest
from config.settings import get_credentials
from pages.payments.schedule_payments_page import SchedulePaymentsPage

@pytest.mark.payments
@pytest.mark.android
@pytest.mark.state_changing
def test_schedule_transfer_successfully(driver):
    """
    TC-ID: PAY-SCHED-001
    Validates schedule payment transfer sequence using standard element locators.
    """
    schedule_page = SchedulePaymentsPage(driver)

    # 1. Complete the temporary login sequence with env credentials
    credentials = get_credentials()
    schedule_page.handle_quick_login(credentials["username"], credentials["password"])

    # 2. Run the actual structured element flow
    schedule_page.execute_schedule_transfer_flow(amount="5000")
