from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.inventory_page import InventoryPage
from pages.locators import PRODUCT_LOCATORS
from pages.order_success_page import OrderSuccessPage
from pages.user_form_page import UserFormPage

def test_checkout(driver, login): # полная последовательность совершения покупки

    # Add to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_products_to_cart(
        PRODUCT_LOCATORS['ITEM_BACKPACK'],
        PRODUCT_LOCATORS['ITEM_ONESIE'],
        PRODUCT_LOCATORS['ITEM_FLEECE_JACKET']
    )

    inventory_page.go_to_cart()

    # Shopping cart container
    cart_page = CartPage(driver)
    cart_page.verify_inventory_items(
        "Sauce Labs Backpack",
        "Sauce Labs Onesie",
        "Sauce Labs Fleece Jacket"
    )
    cart_page.click_checkout_button()

    # Checkout: Your information
    user_form_page = UserFormPage(driver)
    user_form_page.fill_checkout_form("John", "Doe", "123456")

    # Обзор заказа
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.finish_order()

    # Подтверждение заказа
    order_success_page = OrderSuccessPage(driver)
    order_success_page.verify_success_message()
