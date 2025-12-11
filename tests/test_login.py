from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.locators import PRODUCT_LOCATORS, CHECKOUT_LOCATORS, CART_LOCATORS


def fill_checkout_form(driver, first_name, last_name, postal_code, timeout=10): # заполнение формы заказа

    wait = WebDriverWait(driver, timeout)

    wait.until(EC.element_to_be_clickable(CHECKOUT_LOCATORS['FIRST_NAME'])).send_keys(first_name)
    wait.until(EC.element_to_be_clickable(CHECKOUT_LOCATORS['LAST_NAME'])).send_keys(last_name)
    wait.until(EC.element_to_be_clickable(CHECKOUT_LOCATORS['POSTAL_CODE'])).send_keys(postal_code)
    wait.until(EC.element_to_be_clickable(CHECKOUT_LOCATORS['CONTINUE_BUTTON'])).click()

def test_open_page(driver, login): # Проверяет текст заголовка, и что 6 товаров
    assert "Swag Labs" in driver.title

    #Products
    product_cards = driver.find_elements(*PRODUCT_LOCATORS['PRODUCT_CARDS'])
    assert len(product_cards) == 6, f"Expected 6 products, got {len(product_cards)}"

def test_checkout(driver, login): # полная последовательность совершения покупки

    # Add to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart(PRODUCT_LOCATORS['ITEM_BACKPACK'])
    inventory_page.add_product_to_cart(PRODUCT_LOCATORS['ITEM_ONESIE'])
    inventory_page.add_product_to_cart(PRODUCT_LOCATORS['ITEM_FLEECE_JACKET'])

    # Shopping cart container
    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    cart_page.verify_inventory_items(
        "Sauce Labs Backpack",
        "Sauce Labs Onesie",
        "Sauce Labs Fleece Jacket"
    )

    driver.find_element(*CHECKOUT_LOCATORS['CHECKOUT_BUTTON']).click()

    # Checkout: Your information
    fill_checkout_form(driver, "John", "Doe", "123456")

    driver.find_element(*CHECKOUT_LOCATORS['FINISH_BUTTON']).click()

    checkout_complete_title = driver.find_element(*CHECKOUT_LOCATORS['COMPLETE_HEADER'])
    assert checkout_complete_title.text == "Thank you for your order!"
