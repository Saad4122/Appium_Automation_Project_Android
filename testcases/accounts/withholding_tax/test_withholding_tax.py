import pytest
from pages.accounts.withholding_tax_page import WithholdingTaxPage

@pytest.mark.accounts
@pytest.mark.android
def test_withholding_tax_certificate(driver):
    """
    TC-ID: TC-ACC-017
    Validates Withholding tax certificate.
    """
    page = WithholdingTaxPage(driver)
    pytest.skip("TODO: Implement test flow once Android page source is captured")
