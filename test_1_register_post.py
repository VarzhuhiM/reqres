import pytest
import requests
import allure

my_id = None
my_token = None


@allure.feature('User Management')
@allure.suite('User Registration')
@allure.title('Register a user with valid credentials')
@allure.description('This test registers a user with valid credentials and verifies the response')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_register_user():
    global my_id
    global my_token

    with allure.step('Send POST request to register user'):
        url = 'https://reqres.in/api/register'
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post(url, json=data)

    with allure.step('Verify the status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains a token'):
        assert 'token' in response_data, 'Response should contain a token'
        assert isinstance(response_data['token'], str), 'Token should be a string'

    with allure.step('Verify response contains an ID'):
        assert 'id' in response_data, 'Response should contain an ID'
        assert response_data['id'], 'ID should not be empty'

    my_id = response_data['id']
    my_token = response_data['token']


@allure.feature('User Management')
@allure.suite('User Registration')
@allure.title('Register a user without a password')
@allure.description('This test attempts to register a user without a password and verifies the error response')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_register_user():
    with allure.step('Send POST request to register user without a password'):
        url = 'https://reqres.in/api/register'
        data = {
            "email": "sydney@fife"
        }
        response = requests.post(url, json=data)

    with allure.step('Verify the status code is 400'):
        assert response.status_code == 400, f'Expected status code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains an error message'):
        assert 'error' in response_data, 'Response should contain an error message'
        assert response_data['error'] == 'Missing password', f"Unexpected error message: {response_data['error']}"


