import pytest
from pages.side_menu.manage_page import ManagePage

@pytest.mark.side_menu
@pytest.mark.android
def test_manage_invite_friends(driver):
    """
    TC-ID: TC-SIDE-004
    Validates Invite friends.
    """
    page = ManagePage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
