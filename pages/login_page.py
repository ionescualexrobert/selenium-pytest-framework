from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.radius")
    MESSAGE = (By.ID, "flash")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_message_text(self):
        return self.wait_for_visibility(self.MESSAGE).text

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()

    def is_username_field_visible(self):
        return self.wait_for_visibility(self.USERNAME).is_displayed()