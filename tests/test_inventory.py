import pytest
import os

from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.logger import setup_logger
from utils.data_loader import load_products
from  utils.connection_aborter import aborter

logger = setup_logger()
products = load_products()
product_name = [item["name"] for item in products]

@pytest.mark.parametrize("item_name_param", product_name)
def test_buy_any_item (page, item_name_param, fake):
    logger.info(f"Test Executed: {item_name_param} buying")

    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    inventory_page.navigate()
    logger.info("Inventory page is opened")

    inventory_page.add_item_to_cart(item_name_param)
    expect(page.locator(inventory_page.cart)).to_have_text("1")
    logger.info(f"{item_name_param} is added to cart")

    inventory_page.go_to_cart()
    expect(page.locator(cart_page.item_name_cart)).to_have_text(item_name_param)
    logger.info("Cart page is opened")

    cart_page.press_checkout_btn()
    logger.info("Proceed to order page is opened")

    random_first_name = fake.first_name()
    random_last_name = fake.last_name()
    random_zip = fake.zipcode()
    logger.info("Data for fields is generated")
    logger.info(f"First Name: {random_first_name}, Last Name: {random_last_name}, Zip: {random_zip}")

    checkout_page.fill_information(random_first_name, random_last_name, random_zip)
    logger.info("Form for order is filled")

    checkout_page.press_cont_btn()
    expect(page.locator(checkout_page.title_overview)).to_have_text("Checkout: Overview")
    expect(page.locator(checkout_page.item_name_overview)).to_have_text(item_name_param)
    logger.info("Proceeding with checkout. Checkout: Overview page is opened")
    
    checkout_page.press_finish_btn()
    expect(page.locator(checkout_page.title_final)).to_have_text("Thank you for your order!")
    logger.info("Order is submitted successfully")
    logger.info(f"Test {item_name_param} buying is passed")


def test_broken_images(page):
    logger.info("Test execution: displaying placeholder for broken images (MOCKED)")

    inventory_page = InventoryPage(page)
    page.route("**/*.{png,jpg,jpeg}", aborter)

    inventory_page.navigate()

    logger.info("Images are mocked")

    logger.info("Inventory page is opened")

    image_width = page.locator(inventory_page.item_image).first.evaluate("el => el.naturalWidth")
    assert image_width == 0
    logger.info("Test for broken images is passed")
