import pytest
import os

from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("item_name_param", ["Sauce Labs Fleece Jacket", "Sauce Labs Backpack", "Sauce Labs Onesie"])
def test_buy_any_item (page, item_name_param, fake):
    page.goto("/inventory.html")
    
    inventory_page = InventoryPage()
    cart_page = CartPage()
    inventory_page.add_item_to_cart(page, item_name_param)
    expect(page.locator(inventory_page.cart)).to_have_text("1")
    
    inventory_page.go_to_cart(page)
    expect(page.locator(cart_page.item_name_cart)).to_have_text(item_name_param)
    cart_page.press_checkout_btn(page)

    checkout_page = CheckoutPage()
    random_first_name = fake.first_name()
    random_last_name = fake.last_name()
    random_zip = fake.zipcode()

    checkout_page.fill_information(random_first_name, random_last_name, random_zip, page)
    checkout_page.press_cont_btn(page)
    expect(page.locator(checkout_page.title_overview)).to_have_text("Checkout: Overview")
    expect(page.locator(checkout_page.item_name_overview)).to_have_text(item_name_param)
    
    checkout_page.press_finish_btn(page)
    expect(page.locator(checkout_page.title_final)).to_have_text("Thank you for your order!")
    

