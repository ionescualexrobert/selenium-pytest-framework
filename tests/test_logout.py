from pages.login_page import LoginPage

def test_logout(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")
    page.logout()

    assert "You logged out" in page.get_message_text()
