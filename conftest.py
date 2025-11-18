import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

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

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox")