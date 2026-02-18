from pages.locators import PRODUCT_LOCATORS

def test_open_page(driver, login): # Проверяет текст заголовка, и что 6 товаров
    assert "Swag Labs" in driver.title

    #Products
    product_cards = driver.find_elements(*PRODUCT_LOCATORS['PRODUCT_CARDS'])
    assert len(product_cards) == 6, f"Expected 6 products, got {len(product_cards)}"
