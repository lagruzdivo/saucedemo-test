from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import USER_FORM_LOCATORS

class UserFormPage(BasePage):
    def fill_checkout_form(self, first_name, last_name, postal_code): # заполнение формы заказа

        self.input_text(USER_FORM_LOCATORS['FIRST_NAME'], first_name)
        self.input_text(USER_FORM_LOCATORS['LAST_NAME'], last_name)
        self.input_text(USER_FORM_LOCATORS['POSTAL_CODE'], postal_code)
        self.click(USER_FORM_LOCATORS['CONTINUE_BUTTON'])