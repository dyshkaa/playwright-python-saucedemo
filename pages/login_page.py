class LoginPage:
    def __init__(self):
        self.username_field = "#user-name"
        self.password_field = "#password"
        self.login_button = "#login-button"

    def navigate(self, page):
        page.goto("/")
    
    def login(self, page, username, password):
        page.fill(self.username_field, username)
        page.fill(self.password_field, password)
        page.click(self.login_button)



