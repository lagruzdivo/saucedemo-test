from .base_page import BasePage
from .locators import LOGIN_LOCATORS

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.get(self.BASE_URL)
        self.input_text(LOGIN_LOCATORS['USERNAME_FIELD'], username)
        self.input_text(LOGIN_LOCATORS['PASSWORD_FIELD'], password)
        self.click(LOGIN_LOCATORS['LOGIN_BUTTON'])
        self.wait_for_element(LOGIN_LOCATORS['INVENTORY_ITEMS'])

