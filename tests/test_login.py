import pytest
import os

from playwright.sync_api import expect

def test_guest_can_login(page, login_page):
    login_page.login(page, os.getenv("USER_LOGIN"), os.getenv("SECRET_PASSWORD"))
    expect(page.locator('.title')).to_contain_text('Products')

@pytest.mark.parametrize("password", ["123", "password", "qwerty"])
def test_login_with_wrong_password(page, login_page, password):
    login_page.login(page, "standard_user", password)
    expect(page.locator('h3[data-test="error"]')).to_contain_text('Epic sadface: Username and password do not match any user in this service')