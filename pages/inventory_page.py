from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self, locator, timeout=10):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def add_products_to_cart(self, *product_locators, timeout=10):
        for locator in product_locators:
            self.add_product_to_cart(locator, timeout)