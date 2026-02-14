from pages.base_page import BasePage

class InventoryPage(BasePage):
    URL = "/inventory.html"

    CART = ".shopping_cart_link"
    ADD_BACKPACK_TO_CART_BUTTON = '[data-test="add-to-cart-sauce-labs-backpack"]'
    ADD_TO_CART_BUTTON = '[data-test="add-to-cart-'

    EVALUATE_PARAM = "localStorage.setItem('cart-contents', '[4]')"

    PRODUCT_IMAGE = "img.inventory_item_img"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open_url(self.URL)

    def add_backpack_to_cart (self):
        self.click_element(self.ADD_BACKPACK_TO_CART_BUTTON)

    def add_item_to_cart(self, item_name):
        upd_item_name = item_name.lower().replace(" ", "-")
        self.ADD_TO_CART_BUTTON = f'[data-test="add-to-cart-{upd_item_name}"]'
        self.click_element(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click_element(self.CART)

    def add_product_via_js (self):
        self.page.evaluate(self.EVALUATE_PARAM)

    @property
    def link_counter(self):
        return self.page.locator(self.CART)

    @property
    def product_image(self):
        return self.page.locator(self.PRODUCT_IMAGE)

class LeftSideMenu(BasePage):
    URL = "/inventory.html"

    BURGER_BUTTON = "#react-burger-menu-btn"
    LOGOUT_BUTTON = '[data-test="logout-sidebar-link"]'
    ALL_ITEMS_BUTTON = '[data-test="inventory-sidebar-link"]'
    ABOUT_BUTTON = '[data-test="about-sidebar-link"]'
    RESET_BUTTON = '[data-test="reset-sidebar-link"]'
    CLOSE_BURGER_BUTTON = "#react-burger-cross-btn"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open_url(self.URL)

    def open_menu(self):
        self.click_element(self.BURGER_BUTTON)

    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)


