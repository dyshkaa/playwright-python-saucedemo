class InventoryPage:
    def __init__(self):
        self.products = ".title"
        self.cart = ".shopping_cart_link"
        self.add_backpack = '[data-test="add-to-cart-sauce-labs-backpack"]'
        self.add_item = '[data-test="add-to-cart-'

        self.item_image = "img.inventory_item_img"

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

class LeftSideMenu:
    def __init__(self):
        self.burger_btn = "#react-burger-menu-btn"
        self.logout_btn = '[data-test="logout-sidebar-link"]'
        self.all_items_btn = '[data-test="inventory-sidebar-link"]'
        self.about_btn = '[data-test="about-sidebar-link"]'
        self.reset_btn = '[data-test="reset-sidebar-link"]'
        self.burger_close_btn = "#react-burger-cross-btn"

    def navigate(self, page):
        page.goto("/inventory.html")

    def open_menu(self, page):
        page.locator(self.burger_btn).click()

    def logout(self, page):
        page.locator(self.logout_btn).click()

