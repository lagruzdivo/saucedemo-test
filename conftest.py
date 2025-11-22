import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locators for login
USERNAME_FIELD = (By.ID, "user-name")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
INVENTORY_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-container']")


@pytest.fixture(scope="function")
def driver(request):
    # Для переключения между браузерами
    browser = getattr(request.config.option, "browser", "chrome")  # по умолчанию chrome
    if browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        # Настройки для отключения всплывающих окон в Firefox
        driver.execute_script("""
                Object.defineProperty(navigator, 'credentials', {
                    get: () => undefined
                });
            """)
    else:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in(driver):
    driver.get("https://www.saucedemo.com")

    # Login
    driver.find_element(*USERNAME_FIELD).send_keys("performance_glitch_user")
    driver.find_element(*PASSWORD_FIELD).send_keys("secret_sauce")
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(INVENTORY_ITEMS)
    )

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox")