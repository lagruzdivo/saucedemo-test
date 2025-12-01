from selenium.webdriver.common.by import By

# Login Page locators:
USERNAME_FIELD = (By.ID, "user-name")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
INVENTORY_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-container']")

# Product Page locators:
PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
ADD_TO_CART_SAUCE_LABS_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
ADD_TO_CART_SAUCE_LABS_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
ADD_TO_CART_SAUCE_LABS_FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")

# Cart Page locators:
SHOPPING_CART_CONTAINER = (By.ID, "shopping_cart_container")
CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
INVENTORY_ITEMS_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

# Checkout locators
CHECKOUT_BUTTON = (By.ID, "checkout")
FIRST_NAME = (By.ID, "first-name")
LAST_NAME = (By.ID, "last-name")
POSTAL_CODE = (By.ID, "postal-code")
CONTINUE_BUTTON = (By.ID, "continue")
FINISH_BUTTON = (By.ID, "finish")
COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")