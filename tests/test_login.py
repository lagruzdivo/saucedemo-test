from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.locators import (
    # Product locators
    PRODUCT_CARDS, ADD_TO_CART_SAUCE_LABS_BACKPACK, ADD_TO_CART_SAUCE_LABS_ONESIE, ADD_TO_CART_SAUCE_LABS_FLEECE_JACKET,
    # Checkout locators
    CHECKOUT_BUTTON, FIRST_NAME, LAST_NAME, POSTAL_CODE, CONTINUE_BUTTON, FINISH_BUTTON, COMPLETE_HEADER
)

def fill_checkout_form(driver, first_name, last_name, postal_code, timeout=10): # заполнение формы заказа

    wait = WebDriverWait(driver, timeout)

    wait.until(EC.element_to_be_clickable(FIRST_NAME)).send_keys(first_name)
    wait.until(EC.element_to_be_clickable(LAST_NAME)).send_keys(last_name)
    wait.until(EC.element_to_be_clickable(POSTAL_CODE)).send_keys(postal_code)
    wait.until(EC.element_to_be_clickable(CONTINUE_BUTTON)).click()

def test_open_page(driver, login): # Проверяет текст заголовка, и что 6 товаров
    assert "Swag Labs" in driver.title

    #Products
    product_cards = driver.find_elements(*PRODUCT_CARDS)
    assert len(product_cards) == 6, f"Expected 6 products, got {len(product_cards)}"

def test_checkout(driver, login): # полная последовательность совершения покупки

    # Add to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart(ADD_TO_CART_SAUCE_LABS_BACKPACK)
    inventory_page.add_product_to_cart(ADD_TO_CART_SAUCE_LABS_ONESIE)
    inventory_page.add_product_to_cart(ADD_TO_CART_SAUCE_LABS_FLEECE_JACKET)

    # Shopping cart container
    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.verify_inventory_items( "Sauce Labs Backpack", "Sauce Labs Onesie", "Sauce Labs Fleece Jacket")

    driver.find_element(*CHECKOUT_BUTTON).click()

    # Checkout: Your information
    fill_checkout_form(driver, "John", "Doe", "123456")

    driver.find_element(*FINISH_BUTTON).click()

    checkout_complete_title = driver.find_element(*COMPLETE_HEADER)
    assert checkout_complete_title.text == "Thank you for your order!"
