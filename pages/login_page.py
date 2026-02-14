from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "/"

    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    LOGIN_LOGO = ".login_logo"

    ERROR_MESSAGE = 'h3[data-test="error"]'

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open_url(self.URL)
    
    def login(self, username: str, password: str):
        self.fill_fields(self.USERNAME_FIELD, username)
        self.fill_fields(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)

    @property
    def error_message_text(self):
        return self.page.locator(self.ERROR_MESSAGE)

    @property
    def login_logo(self):
        return self.page.locator(self.LOGIN_LOGO)



