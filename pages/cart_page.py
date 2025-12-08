from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.locators import (
        # Cart locators
    SHOPPING_CART_CONTAINER, CART_BADGE, INVENTORY_ITEMS_NAMES
)
class CartPage(BasePage):
    def verify_cart_badge(self, count, timeout=10): # клик иконки корзины, ждёт появление цифры и проверяет её
        self.find_element(SHOPPING_CART_CONTAINER).click()

        self.wait.until(
            EC.presence_of_element_located(CART_BADGE)
        )

        cart_badge = self.find_element(CART_BADGE)
        assert cart_badge.text == count, f"Expected {count} but got {cart_badge.text}"

    def verify_inventory_items(self, *expected_items, timeout=10): # проверяет товары в корзине(название и кол-во)
        self.wait.until(
            EC.presence_of_element_located(INVENTORY_ITEMS_NAMES)
        )

        inventory_item_names = self.find_elements(INVENTORY_ITEMS_NAMES)

        actual_count = len(inventory_item_names)
        expected_count = len(expected_items)
        assert actual_count == expected_count, f"Expected {expected_count} items, but got {actual_count}"

        for i in range(len(expected_items)):
            actual_item = inventory_item_names[i].text
            expected_item = expected_items[i]
            assert actual_item == expected_item, f"item{i+1}: expected '{expected_item}' but got '{actual_item}'"

    def go_to_cart(self):
        self.find_element(SHOPPING_CART_CONTAINER).click()
