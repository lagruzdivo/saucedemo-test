from pages.base_page import BasePage
from pages.locators import ORDER_SUCCESS_LOCATORS

class OrderSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.complete_header = self.find_element(ORDER_SUCCESS_LOCATORS['COMPLETE_HEADER'])

    def verify_success_message(self, expected_text="Thank you for your order!"):
        actual_text = self.complete_header.text
        assert actual_text == expected_text