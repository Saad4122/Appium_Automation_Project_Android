import pytest
from pages.dashboard.global_search_page import GlobalSearchPage

@pytest.mark.dashboard
@pytest.mark.android
def test_global_search_query(driver):
    """
    TC-ID: TC-DASH-002
    Validates Global search query.
    """
    page = GlobalSearchPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
