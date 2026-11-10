import pytest
from pages.side_menu.manage_page import ManagePage

@pytest.mark.side_menu
@pytest.mark.android
def test_manage_account_opening_form(driver):
    """
    TC-ID: TC-SIDE-003
    Validates Account opening form.
    """
    page = ManagePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
