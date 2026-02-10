import pytest
import os
from playwright.sync_api import expect
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

def test_login_page_visual(page, base_url, assert_snapshot):
    logger.info("Visual test started: Login Page")
    
    page.goto(base_url)

    expect(page.locator(".login_logo")).to_be_visible()
    assert_snapshot(page.screenshot(), "login_page_snapshot.png")

    logger.info("Visual test passed")

def test_login_page_on_error(page, base_url, assert_snapshot):
    logger.info("Visual test started: Error banner on Login Page")
    login_page = LoginPage(page)

    page.goto(base_url)
    expect(page.locator(".login_logo")).to_be_visible()

    login_page.login(os.getenv("USER_LOGIN"), "123")

    expect(page.locator('h3[data-test="error"]')).to_be_visible()

    assert_snapshot(page.screenshot(), "login_page_with_error_snapshot.png")