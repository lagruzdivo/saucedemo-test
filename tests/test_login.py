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

def add_product_to_cart(driver, locator, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    ).click()

def test_open_page(logged_in):
    driver = logged_in
    assert "Swag Labs" in driver.title

    #Products
    product_cards = driver.find_elements(*PRODUCT_CARDS)
    assert len(product_cards) == 6, f"Expected 6 products, got {len(product_cards)}"

def test_add_cart(logged_in):
    driver = logged_in

    # Add to cart

    add_product_to_cart(driver, ADD_TO_CART_SAUCE_LABS_BACKPACK)
    add_product_to_cart(driver, ADD_TO_CART_SAUCE_LABS_ONESIE)
    add_product_to_cart(driver, ADD_TO_CART_SAUCE_LABS_FLEECE_JACKET)

    # Shopping cart container
    driver.find_element(*SHOPPING_CART_CONTAINER).click()

    cart_badge = driver.find_element(*CART_BADGE)
    assert cart_badge.text == "3"

    inventory_item_names = driver.find_elements(*INVENTORY_ITEMS_NAMES)
    assert inventory_item_names[0].text == "Sauce Labs Backpack"
    assert inventory_item_names[1].text == "Sauce Labs Onesie"
    assert inventory_item_names[2].text == "Sauce Labs Fleece Jacket"
