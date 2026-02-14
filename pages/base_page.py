from playwright.sync_api import expect


class BasePage:
    URL = ""
    PAGE_TITLE = ".title"

    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url)

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def find(self, selector):
        return self.page.locator(selector)

    def fill_fields(self, selector, fields):
        self.page.fill(selector, fields)

    def click_element(self, selector):
        self.page.click(selector)

    def refresh_page(self):
        self.page.reload()

    def url_should_be_opened(self):
        expect(self.page).to_have_url(self.URL)

    @property
    def title_text(self):
        return self.page.locator(self.PAGE_TITLE)

