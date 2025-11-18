from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

def test_open_page(driver):
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title

    # Login
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    #Products
    product_cards = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(product_cards) == 6, f"Expected 6 products, got {len(product_cards)}"

def test_add_cart(driver):
    driver.get("https://www.saucedemo.com")

    # Login
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("performance_glitch_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Add to cart

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))
    ).click()

    # Shopping cart container
    shopping_cart_button = driver.find_element(By.ID, "shopping_cart_container").click()

    cart_badge = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    assert cart_badge.text == "3"

    inventory_item_names = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    assert inventory_item_names[0].text == "Sauce Labs Backpack"
    assert inventory_item_names[1].text == "Sauce Labs Onesie"
    assert inventory_item_names[2].text == "Sauce Labs Fleece Jacket"
