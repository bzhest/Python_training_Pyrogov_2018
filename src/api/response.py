import allure


class AssertableResponse(object):

    def __init__(self, response):
        self._response = response

    @allure.step
    def status_code(self, code):
        return self._response.status_code == code

    @allure.step
    def field(self, name):
        return self._response.json()[name]