class CartPage:
    def __init__(self, page):
        self.item_name_cart = '[data-test="inventory-item-name"]'
        self.checkout_btn = '[data-test="checkout"]'
        self.page = page

    def navigate(self):
        self.page.goto("/cart.html")
    
    def press_checkout_btn (self):
        self.page.locator(self.checkout_btn).click()
