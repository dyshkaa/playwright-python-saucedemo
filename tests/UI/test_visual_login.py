import allure
import pytest
import os
from playwright.sync_api import expect

from utils.constants import WRONG_CREDENTIAL_ERROR_TEXT
from utils.logger import setup_logger

from pages.login_page import LoginPage

import sys
import pytest

logger = setup_logger()

@pytest.fixture
def browser_context_args(base_url):
    return {
        "base_url": base_url,
    }

@allure.feature("Pixel Perfect tests")
@allure.story("Check login page design")
@pytest.mark.Pixel_perf
def test_login_page_visual(login_page, page, assert_snapshot):
    logger.info("Visual test started: Login Page")

    login_page.open()

    expect(login_page.login_logo).to_be_visible()
    assert_snapshot(page.screenshot(), "login_page_snapshot.png")

    logger.info("Visual test passed")

@allure.feature("Pixel Perfect tests")
@allure.story("Check login page on error design")
@pytest.mark.Pixel_perf
def test_login_page_on_error(login_page, page, assert_snapshot):
    logger.info("Visual test started: Error banner on Login Page")

    login_page.open()
    expect(login_page.login_logo).to_be_visible()

    login_page.login(os.getenv("USER_LOGIN"), "123")

    expect(login_page.error_message_text).to_be_visible()
    expect(login_page.error_message_text).to_have_text(WRONG_CREDENTIAL_ERROR_TEXT)

    assert_snapshot(page.screenshot(), "login_page_with_error_snapshot.png")