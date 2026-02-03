import pytest
import os

from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart_via_js(page):
    page.goto("/inventory.html")

    page.evaluate("localStorage.setItem('cart-contents', '[4]')")
    page.reload()

    inventory_page = InventoryPage()
    expect(page.locator(inventory_page.cart)).to_have_text("1")

    inventory_page.go_to_cart(page)

    cart_page = CartPage()
    expect(page.locator(cart_page.item_name_cart)).to_have_text("Sauce Labs Backpack")