import pytest
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage

@pytest.mark.regression
def test_secure_area_elements(driver):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    secure_page = SecureAreaPage(driver)

    # 2. Verificări FUNCȚIONALE pe pagina securizată
    assert "Secure Area" in secure_page.get_header_text()
    assert secure_page.is_logout_button_visible() is True
    assert "You logged into a secure area!" in secure_page.get_message()
