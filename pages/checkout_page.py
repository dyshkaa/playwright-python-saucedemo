class CheckoutPage:
    def __init__(self):
        self.firstName = '[data-test="firstName"]'
        self.lastName = '[data-test="lastName"]'
        self.zip = '[data-test="postalCode"]'
        self.ctn_btn = '[data-test="continue"]'
        self.title_overview = '.title'
        self.item_name_overview = '[data-test="inventory-item-name"]'
        self.finish_btn = '[data-test="finish"]'
        self.title_final = '.complete-header'

    def navigate(self, page):
        page.goto("/checkout-step-one.html")
        
    def press_cont_btn(self, page):
        page.locator(self.ctn_btn).click()

    def fill_information(self, firstN, lastN, postal, page):
        page.locator(self.firstName).fill(firstN)
        page.locator(self.lastName).fill(lastN)
        page.locator(self.zip).fill(postal)

    def press_finish_btn(self, page):
        page.locator(self.finish_btn).click()