import allure
import pytest
from playwright.sync_api import Playwright, APIRequestContext

from utils.logger import setup_logger

logger = setup_logger()

@allure.feature("Booking Func")
@allure.story("API booker functionality")
@pytest.mark.API
def test_get_booking(api_request_context: APIRequestContext):
    logger.info("Api get booking test is started")
    response = api_request_context.get(url = "/booking")
    assert response.status == 200
    logger.info("Response is OK")

    json_response = response.json()
    assert len(json_response) != 0
    logger.info("Api Response contains answer")
    logger.info("Api get booking test is finished")

@allure.feature("Booking Func")
@allure.story("API booker functionality")
@pytest.mark.API
def test_create_booking(api_request_context: APIRequestContext):
    logger.info("Api create booking test is started")

    payload = {
        "firstname": "Ivan",
        "lastname": "Petrov",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-10"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_request_context.post(url = "/booking", data=payload)
    assert response.ok
    logger.info("Response is OK")

    json_response = response.json()
    assert json_response["booking"]["firstname"] == "Ivan"
    logger.info("Booking created successfully")

    logger.info("Api create booking test is finished")

@allure.feature("Booking Func")
@allure.story("API booker functionality")
@pytest.mark.API
def test_delete_booking(api_request_context: APIRequestContext, token):
    logger.info("Api delete booking test is started")

    payload = {
        "firstname": "test",
        "lastname": "testovich",
        "totalprice": 900,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2025-03-10"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_request_context.post(url="/booking", data=payload)
    assert response.ok
    logger.info("New booker created")

    json_response = response.json()
    new_booker_id = json_response["bookingid"]

    headers = {
        "Cookie": f"token={token}"
    }

    response = api_request_context.delete(url = f"/booking/{new_booker_id}", headers=headers)
    assert response.ok
    assert api_request_context.get(url = f"/booking/{new_booker_id}").status == 404

    logger.info("Booking deleted successfully")

    api_request_context.get(url = f"/booking/{new_booker_id}")


