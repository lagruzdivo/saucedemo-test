from pages.base_page import BasePage
from pages.locators import ORDER_SUCCESS_LOCATORS

class OrderSuccessPage(BasePage):
    def verify_order_success(self, expected_text = "Thank you for your order!"):
        actual_text = self.get_text(ORDER_SUCCESS_LOCATORS['COMPLETE_HEADER'])
        assert actual_text == expected_text