import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Update')
@allure.title('Update user information')
@allure.description('This test updates the user information and verifies the response')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update_user():
    with allure.step('Define the API endpoint and payload'):
        url = 'https://reqres.in/api/users/2'
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }

    with allure.step('Send PUT request to update user'):
        response = requests.put(url, json=data)
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the name in the response'):
        assert response_data['name'] == data['name'], f"Expected name to be {data['name']}, but got {response_data['name']}"

    with allure.step('Verify the job in the response'):
        assert response_data['job'] == data['job'], f"Expected job to be {data['job']}, but got {response_data['job']}"

    with allure.step('Verify the response contains an updatedAt field'):
        assert 'updatedAt' in response_data, 'Response should contain an updatedAt field'

