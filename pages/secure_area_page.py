from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecureAreaPage(BasePage):

    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button.secondary.radius")
    MESSAGE = (By.ID, "flash")
    HEADER = (By.CSS_SELECTOR, "h2")

    def logout(self):
        self.click(self.LOGOUT_BTN)

    def get_message(self):
        return self.get_text(self.MESSAGE)

    def get_header_text(self):
        return self.get_text(self.HEADER)

    def is_logout_button_visible(self):
        return self.wait_for_visibility(self.LOGOUT_BTN).is_displayed()