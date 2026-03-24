import pytest
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage


@pytest.mark.regression
def test_logout_redirects_to_login_page(driver):

    # 1. Deschidem pagina de login
    login_page = LoginPage(driver)
    login_page.open()

    # 2. Facem login
    login_page.login("tomsmith", "SuperSecretPassword!")

    # 3. Ajungem în Secure Area
    secure_page = SecureAreaPage(driver)

    # 4. Facem logout
    secure_page.logout()

    # 5. Verificăm că apare mesajul de logout
    assert "You logged out" in secure_page.get_message()

    # 6. Verificăm că suntem înapoi pe pagina de login
    assert login_page.is_username_field_visible()