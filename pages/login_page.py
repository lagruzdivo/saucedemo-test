from pages.base_page import BasePage
from pages.locators import LOGIN_LOCATORS

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.username = None
        self.password = None
        self.login_button = None


    def login(self, username, password):
        self.driver.get(self.BASE_URL)

        self.username = self.find_element(LOGIN_LOCATORS['USERNAME_FIELD'])
        self.password = self.find_element(LOGIN_LOCATORS['PASSWORD_FIELD'])
        self.login_button = self.find_element(LOGIN_LOCATORS['LOGIN_BUTTON'])

        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
        self.wait_for_element(LOGIN_LOCATORS['INVENTORY_ITEMS'])


