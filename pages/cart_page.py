class CartPage:
    def __init__(self):
        self.item_name_cart = '[data-test="inventory-item-name"]'
        self.checkout_btn = '[data-test="checkout"]'
    
    def navigate(self, page):
        page.goto("/cart.html")
    
    def press_checkout_btn (self, page):
        page.locator(self.checkout_btn).click()
