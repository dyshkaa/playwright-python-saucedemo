import pytest
import os
import base64

from faker import Faker
from playwright.sync_api import BrowserType

from pages.login_page import LoginPage

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_bytes = page.screenshot()
            image = base64.b64encode(screenshot_bytes).decode("utf-8")
            extra.append(pytest_html.extras.html(f'<div style="margin: 10px;"><img src="data:image/png;base64,{image}" style="width:600px; border:1px solid red;" align="right"/></div>'))
    
    report.extra = extra

@pytest.fixture
def fake():
    faker = Faker()
    return faker

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