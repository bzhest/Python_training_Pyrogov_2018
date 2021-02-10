import requests
import json

from src.api.response import AssertableResponse


class ApiService(object):

    def __init__(self):
        self.header = {'content-type': 'application/json'}
        self.base_url = "http://localhost:80"


class UserApiService(ApiService):

    def __init__(self):
        super().__init__()

    def create_user(self, user):

        return AssertableResponse(requests.post(
            url=self.base_url + "/register",
            data=json.dumps(user),
            headers=self.header
        ))

    def get_user_by_id(self, user_id):
        return AssertableResponse(requests.get(f"{self.base_url}/customers/{user_id}"))