import json

import allure
import requests

from src.api.response import AssertableResponse
from src.api.services import UserApiService


@allure.step
def test_user_can_register_with_valid_creds(faker):
    user = {"username": faker.name(), "password": "1234567", "email": "bzhest@gmail.com"}

    response = UserApiService().create_user(user)

    assert response.status_code(200)
    assert len(response.field('id')) > 0


@allure.step
def test_can_get_user_by_id(faker):
    user = {"username": faker.name(), "password": "1234567", "email": "bzhest@gmail.com"}

    response = UserApiService().create_user(user)
    user_id = response.field('id')

    resp = UserApiService().get_user_by_id(user_id)
    resp.status_code(200)
