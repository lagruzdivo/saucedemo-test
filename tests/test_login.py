from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locators for test
PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
ADD_TO_CART_SAUCE_LABS_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
ADD_TO_CART_SAUCE_LABS_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
ADD_TO_CART_SAUCE_LABS_FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
SHOPPING_CART_CONTAINER = (By.ID, "shopping_cart_container")
CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
INVENTORY_ITEMS_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
CHECKOUT_BUTTON = (By.ID, "checkout")
FIRST_NAME = (By.ID, "first-name")
LAST_NAME = (By.ID, "last-name")
POSTAL_CODE = (By.ID, "postal-code")
CONTINUE_BUTTON = (By.ID, "continue")
FINISH_BUTTON = (By.ID, "finish")

def add_product_to_cart(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    ).click()
def fill_checkout_form(driver, first_name="John", last_name = "John", postal_code = "123456"):
    driver.find_element(*FIRST_NAME).send_keys(first_name)
    driver.find_element(*LAST_NAME).send_keys(last_name)
    driver.find_element(*POSTAL_CODE).send_keys(postal_code)
    driver.find_element(*CONTINUE_BUTTON).click()

def verify_inventory_items(driver, *expected_items):
    inventory_item_names = driver.find_elements(*INVENTORY_ITEMS_NAMES)

    actual_count = len(inventory_item_names)
    expected_count = len(expected_items)
    assert actual_count == expected_count, f"Expected {expected_count} items, but got {actual_count}"

    for i in range(len(expected_items)):
        actual_item = inventory_item_names[i].text
        expected_item = expected_items[i]
        assert actual_item == expected_item, f"item{i+1}: expected '{actual_item}' but got '{actual_item}'"

def verify_cart_badge(driver, count):
    driver.find_element(*SHOPPING_CART_CONTAINER).click()

    cart_badge = driver.find_element(*CART_BADGE)
    assert cart_badge.text == count, f"Expected {count} but got {cart_badge.text}"

def test_open_page(login):
    assert "Swag Labs" in login.title

    #Products
    product_cards = login.find_elements(*PRODUCT_CARDS)
    assert len(product_cards) == 6, f"Expected 6 products, got {len(product_cards)}"

def test_checkout(login):

    # Add to cart

    add_product_to_cart(login, ADD_TO_CART_SAUCE_LABS_BACKPACK)
    add_product_to_cart(login, ADD_TO_CART_SAUCE_LABS_ONESIE)
    add_product_to_cart(login, ADD_TO_CART_SAUCE_LABS_FLEECE_JACKET)

    # Shopping cart container
    login.find_element(*SHOPPING_CART_CONTAINER).click()
    verify_inventory_items(login, "Sauce Labs Backpack", "Sauce Labs Onesie", "Sauce Labs Fleece Jacket")

    login.find_element(*CHECKOUT_BUTTON).click()

    # Checkout: Your information
    fill_checkout_form(login)

    login.find_element(*FINISH_BUTTON).click()

    checkout_complete = login.find_element(By.CSS_SELECTOR, "[data-test='complete-header']")
    assert checkout_complete.text == "Thank you for your order!"

