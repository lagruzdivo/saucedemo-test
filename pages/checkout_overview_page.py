from pages.base_page import BasePage
from pages.locators import CHECKOUT_OVERVIEW_LOCATORS

class CheckoutOverviewPage(BasePage):
    def finish_order(self):
        self.click(CHECKOUT_OVERVIEW_LOCATORS['FINISH_BUTTON'])