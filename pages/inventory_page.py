class InventoryPage:
    def __init__(self):
        self.products = ".title"
        self.cart = ".shopping_cart_link"
        self.add_backpack = '[data-test="add-to-cart-sauce-labs-backpack"]'
        self.add_item = '[data-test="add-to-cart-'

        
    def navigate(self, page):
        page.goto("/inventory.html")

    def add_backpack_to_cart (self, page):
        page.locator(self.add_backpack).click()

    def add_item_to_cart(self, page, item_name):
        upd_item_name = item_name.lower().replace(" ", "-")
        self.add_item = f'[data-test="add-to-cart-{upd_item_name}"]'
        page.locator(self.add_item).click()


    def go_to_cart(self, page):
        page.locator(self.cart).click()


