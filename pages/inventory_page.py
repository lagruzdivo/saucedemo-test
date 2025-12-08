from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def add_product_to_cart(self, locator, timeout=10): # добавление товара в корзину
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()