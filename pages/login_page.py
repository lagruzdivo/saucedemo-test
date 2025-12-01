from .base_page import BasePage
from .locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, INVENTORY_ITEMS

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.get(self.BASE_URL)
        self.input_text(USERNAME_FIELD, username)
        self.input_text(PASSWORD_FIELD, password)
        self.click(LOGIN_BUTTON)
        self.wait_for_element(INVENTORY_ITEMS)

