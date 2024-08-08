import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Creation')
@allure.title('Create a new user')
@allure.description('This test creates a new user and verifies the response')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_user():
    url = 'https://reqres.in/api/users'
    data = {
        "name": "Varzhuhi",
        "job": "QA"
    }
    with allure.step('Send POST request to create user'):
        response = requests.post(url, json=data)
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains user ID'):
        assert 'id' in response_data, 'Response should contain an id'

    with allure.step('Verify response contains correct name and job'):
        assert response_data['name'] == data['name'], f"Expected name to be {data['name']}, but got {response_data['name']}"

    with allure.step('Verify response contains correct job'):
        assert response_data['job'] == data['job'], f"Expected job to be {data['job']}, but got {response_data['job']}"


