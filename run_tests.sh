rm -rf allure_results

pytest test/api/test_user_registration_api.py -sv --alluredir=allure_results
