import pytest
import os
import base64

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
def login_page (page):
    login_page = LoginPage()
    login_page.navigate(page)
    return login_page

@pytest.fixture
def do_login(page, login_page):
    login_page.login(page, os.getenv("USER_LOGIN"), os.getenv("SECRET_PASSWORD"))
    yield