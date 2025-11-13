from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_open_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
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

    finally:
        driver.quit()
