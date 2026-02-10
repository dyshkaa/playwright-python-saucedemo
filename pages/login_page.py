class LoginPage:
    def __init__(self, page):
        self.username_field = "#user-name"
        self.password_field = "#password"
        self.login_button = "#login-button"
        self.page = page

    def navigate(self):
        self.page.goto("/")
    
    def login(self, username: str, password: str):
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.login_button)



