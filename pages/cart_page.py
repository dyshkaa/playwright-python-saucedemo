from pages.base_page import BasePage

class CartPage(BasePage):
    URL = "/cart.html"
    PRODUCT_NAME_IN_CART = '[data-test="inventory-item-name"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open_url(self.URL)

    def press_checkout_btn (self):
        self.click_element(self.CHECKOUT_BUTTON)

    @property
    def product_name(self):
        return self.page.locator(self.PRODUCT_NAME_IN_CART)
