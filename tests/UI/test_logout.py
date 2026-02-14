import allure
import pytest
import os

from playwright.sync_api import expect
from pages.inventory_page import LeftSideMenu

@pytest.fixture
def browser_context_args(base_url):
    return {
        "base_url": base_url,
    }

@allure.feature("Authorization")
@allure.story("Logout")
@pytest.mark.UI_login
def test_login_and_logout(page, login_page):
    left_side_menu = LeftSideMenu(page)

    login_page.open()

    login_page.login(os.getenv("USER_LOGIN"), os.getenv("SECRET_PASSWORD"))
    left_side_menu.open_menu()

    left_side_menu.logout()
    expect(login_page.login_logo).to_be_visible()

    login_page.url_should_be_opened()
