import pytest
from playwright.sync_api import expect
from utils.logger import setup_logger

import sys
import pytest

logger = setup_logger()

def test_login_page_visual(page, base_url, assert_snapshot):
    logger.info("Visual test started: Login Page")
    
    page.goto(base_url)

    expect(page.locator(".login_logo")).to_be_visible()
    assert_snapshot(page.screenshot(), "login_page_snapshot.png")

    logger.info("Visual test passed")