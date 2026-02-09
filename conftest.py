import asyncio
import pytest
import os
import base64
import allure
from faker import Faker
from playwright.sync_api import BrowserType
from pages.login_page import LoginPage

from dotenv import load_dotenv
load_dotenv()

##allure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

##faker
@pytest.fixture
def fake():
    faker = Faker()
    return faker

##login
@pytest.fixture
def login_page (page):
    return LoginPage()

##session fixture
@pytest.fixture(scope="session")
def user_session(browser_type: BrowserType, browser_type_launch_args, base_url):
    browser = browser_type.launch(**browser_type_launch_args)
    context = browser.new_context(base_url=base_url)
    page = context.new_page()

    login_p = LoginPage()
    login_p.navigate(page)

    username = os.getenv("USER_LOGIN")
    password = os.getenv("SECRET_PASSWORD")
    
    login_p.login(page, username, password)
    
    page.wait_for_url("**/inventory.html")

    context.storage_state(path="state.json")
    browser.close()
    
    return "state.json"

##give tokens
@pytest.fixture(scope="function")
def browser_context_args(user_session, base_url):
    return {
        "storage_state": "state.json",
        "base_url": base_url
    }
