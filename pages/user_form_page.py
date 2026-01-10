from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import USER_FORM_LOCATORS

class UserFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.first_name = self.find_element(USER_FORM_LOCATORS['FIRST_NAME'])
        self.last_name = self.find_element(USER_FORM_LOCATORS['LAST_NAME'])
        self.postal_code = self.find_element(USER_FORM_LOCATORS['POSTAL_CODE'])
        self.continue_button = self.find_element(USER_FORM_LOCATORS['CONTINUE_BUTTON'])

    def fill_checkout_form(self, first_name, last_name, postal_code): # заполнение формы заказа
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.postal_code.send_keys(postal_code)
        self.continue_button.click()