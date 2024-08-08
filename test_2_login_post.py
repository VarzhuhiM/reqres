import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Authentication')
@allure.title('Login with valid credentials')
@allure.description('This test logs in a user with valid credentials and verifies the response')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_login_user():
    with allure.step('Define the API endpoint and payload'):
        url = 'https://reqres.in/api/login'
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

    with allure.step('Send POST request to login'):
        response = requests.post(url, json=data)
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains a token'):
        assert 'token' in response_data, 'Response should contain a token'

    with allure.step('Verify the token is a string and is not empty'):
        assert isinstance(response_data['token'], str), 'Token should be a string'
        assert response_data['token'], 'Token should not be empty'


@allure.feature('User Management')
@allure.suite('User Authentication')
@allure.title('Login with missing password')
@allure.description('This test attempts to login a user without providing a password and verifies the error response')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_negative_login_user():
    with allure.step('Define the API endpoint and incomplete payload'):
        url = 'https://reqres.in/api/login'
        data = {
            "email": "peter@klaven"
        }

    with allure.step('Send POST request to login without a password'):
        response = requests.post(url, json=data)
        assert response.status_code == 400, f'Expected status code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains an error message'):
        assert 'error' in response_data, 'Response should contain an error message'

    with allure.step('Verify the error message is "Missing password"'):
        assert response_data['error'] == 'Missing password', f"Unexpected error message: {response_data['error']}"


