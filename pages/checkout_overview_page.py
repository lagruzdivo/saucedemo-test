from pages.base_page import BasePage
from pages.locators import CHECKOUT_OVERVIEW_LOCATORS

class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.finish_button = self.driver.find_element(CHECKOUT_OVERVIEW_LOCATORS['FINISH_BUTTON'])

    def finish_order(self):
        self.finish_button.click()
