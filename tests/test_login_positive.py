import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in page.get_message_text()
