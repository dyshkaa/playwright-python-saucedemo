from pages.base_page import BasePage

class CheckoutPage(BasePage):
    URL = "/checkout-step-one.html"

    FIRSTNAME = '[data-test="firstName"]'
    LASTNAME = '[data-test="lastName"]'
    ZIP = '[data-test="postalCode"]'
    CONTINUE_BUTTON = '[data-test="continue"]'
    PRODUCT_NAME_IN_OVERVIEW = '[data-test="inventory-item-name"]'
    FINISH_BUTTON = '[data-test="finish"]'
    TITLE_FINAL = '.complete-header'

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open_url(self.URL)
        
    def press_cont_btn(self):
        self.click_element(self.CONTINUE_BUTTON)

    def fill_information(self, firstname, lastname, postal):
        self.fill_fields(self.FIRSTNAME, firstname)
        self.fill_fields(self.LASTNAME, lastname)
        self.fill_fields(self.ZIP, postal)

    def press_finish_btn(self,):
        self.click_element(self.FINISH_BUTTON)

    @property
    def product_name_in_overview(self):
        return self.page.locator(self.PRODUCT_NAME_IN_OVERVIEW)

    @property
    def title_in_overview(self):
        return self.page.locator(self.TITLE_FINAL)