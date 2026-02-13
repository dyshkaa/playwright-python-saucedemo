import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

#api context setup
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com"
    )
    yield request_context
    request_context.dispose()

#admin session
@pytest.fixture(scope="session")
def token(api_request_context):

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = api_request_context.post(url = "/auth", data=payload)
    assert response.ok
    json_response = response.json()
    assert "token" in json_response
    yield json_response["token"]