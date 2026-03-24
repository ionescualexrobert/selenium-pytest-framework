import pytest
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage

@pytest.mark.e2e
def test_e2e_login_and_logout(driver):
    # 1. Deschidem site-ul
    login_page = LoginPage(driver)
    login_page.open()

    # 2. Facem login
    login_page.login("tomsmith", "SuperSecretPassword!")

    # 3. Verificăm că suntem logați
    secure_page = SecureAreaPage(driver)
    assert "You logged into a secure area!" in secure_page.get_message()

    # 4. Facem logout
    secure_page.logout()

    # 5. Verificăm că ne-am delogat
    assert "You logged out" in secure_page.get_message()
