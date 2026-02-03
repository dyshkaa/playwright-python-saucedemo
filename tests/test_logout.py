import pytest
import os

from playwright.sync_api import expect
from pages.inventory_page import LeftSideMenu

def test_login_and_logout(page, login_page, base_url):
    login_page.navigate(page)

    login_page.login(page, os.getenv("USER_LOGIN"), os.getenv("SECRET_PASSWORD"))
    
    left_side_menu = LeftSideMenu()
    left_side_menu.open_menu(page)

    left_side_menu.logout(page)
    expect(page.locator('.login_logo')).to_be_visible()
    expect(page).to_have_url(base_url)
