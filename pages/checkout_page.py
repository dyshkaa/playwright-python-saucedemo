class CheckoutPage:
    def __init__(self, page):
        self.firstName = '[data-test="firstName"]'
        self.lastName = '[data-test="lastName"]'
        self.zip = '[data-test="postalCode"]'
        self.ctn_btn = '[data-test="continue"]'
        self.title_overview = '.title'
        self.item_name_overview = '[data-test="inventory-item-name"]'
        self.finish_btn = '[data-test="finish"]'
        self.title_final = '.complete-header'
        self.page = page

    def navigate(self):
        self.page.goto("/checkout-step-one.html")
        
    def press_cont_btn(self):
        self.page.locator(self.ctn_btn).click()

    def fill_information(self, firstname, lastname, postal):
        self.page.locator(self.firstName).fill(firstname)
        self.page.locator(self.lastName).fill(lastname)
        self.page.locator(self.zip).fill(postal)

    def press_finish_btn(self,):
        self.page.locator(self.finish_btn).click()