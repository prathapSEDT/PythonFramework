import pytest
from frameworkutils import WebLibrary
from applicationpages import HomePage,Authentication
@pytest.mark.order(1)
def test_Application():
    driver=WebLibrary.launchBrowser()
    HomePage.clickSignLink(driver)
    Authentication.validateAuthenticationHeader(driver)
