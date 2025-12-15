from selenium.webdriver.common.by import By

# Login Page locators:
LOGIN_LOCATORS = {
    'USERNAME_FIELD': (By.ID, "user-name"),
    'PASSWORD_FIELD': (By.ID, "password"),
    'LOGIN_BUTTON': (By.ID, "login-button"),
    'INVENTORY_ITEMS': (By.CSS_SELECTOR, "[data-test='inventory-container']")
}

# Product Page locators:
PRODUCT_LOCATORS = {
    'PRODUCT_CARDS': (By.CLASS_NAME, "inventory_item"),
    'ITEM_BACKPACK': (By.ID, "add-to-cart-sauce-labs-backpack"),
    'ITEM_ONESIE': (By.ID, "add-to-cart-sauce-labs-onesie"),
    'ITEM_FLEECE_JACKET': (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
}

# Cart Page locators:
CART_LOCATORS = {
    'SHOPPING_CART_CONTAINER': (By.ID, "shopping_cart_container"),
    'CART_BADGE': (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"),
    'INVENTORY_ITEMS_NAMES': (By.CSS_SELECTOR, "[data-test='inventory-item-name']"),
    'CHECKOUT_BUTTON': (By.ID, "checkout")
}

# User form locators
USER_FORM_LOCATORS = {
    'FIRST_NAME': (By.ID, "first-name"),
    'LAST_NAME': (By.ID, "last-name"),
    'POSTAL_CODE': (By.ID, "postal-code"),
    'CONTINUE_BUTTON': (By.ID, "continue")
}

# Checkout overview locator
CHECKOUT_OVERVIEW_LOCATORS = {
    'FINISH_BUTTON': (By.ID, "finish")
}

# Order success locators
ORDER_SUCCESS_LOCATORS = {
    'COMPLETE_HEADER': (By.CSS_SELECTOR, "[data-test='complete-header']")
}