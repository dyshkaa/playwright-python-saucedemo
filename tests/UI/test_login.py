import allure
import pytest
import os

from playwright.sync_api import expect

from utils.constants import WRONG_CREDENTIAL_ERROR_TEXT, MAIN_PAGE_TITLE
from utils.logger import setup_logger


logger = setup_logger()

@pytest.fixture
def browser_context_args(base_url):
    return {
        "base_url": base_url,
    }

@allure.feature("Authorization")
@allure.story("Login with valid credentials")
@pytest.mark.UI_login
def test_guest_can_login(login_page):
    login_page.open()
    login_page.url_should_be_opened()

    login_page.login(os.getenv("USER_LOGIN"), os.getenv("SECRET_PASSWORD"))
    expect(login_page.title_text).to_have_text(MAIN_PAGE_TITLE)

@allure.feature("Authorization")
@allure.story("Login with invalid credentials")
@pytest.mark.UI_login
@pytest.mark.parametrize("password", ["123", "password", "qwerty"])
def test_login_with_wrong_password(login_page, password):
    login_page.open()
    login_page.url_should_be_opened()

    login_page.login(os.getenv("USER_LOGIN"), password)
    expect(login_page.error_message_text).to_have_text(WRONG_CREDENTIAL_ERROR_TEXT)