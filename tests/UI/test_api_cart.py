import allure
import pytest

from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("Basic Feature")
@allure.story("API add product to cart scenario")
@pytest.mark.API
def test_add_item_to_cart_via_js(page):
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    inventory_page.open()

    inventory_page.add_product_via_js()
    inventory_page.refresh_page()

    expect(inventory_page.link_counter).to_have_text("1")

    inventory_page.go_to_cart()

    expect(cart_page.product_name).to_have_text("Sauce Labs Backpack")