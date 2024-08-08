import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Update')
@allure.title('Patch user details')
@allure.description('This test updates a user’s details using the PATCH method and verifies the updated information.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_update_user_patch():
    with allure.step('Define the API endpoint and payload for updating user details'):
        url = 'https://reqres.in/api/users/2'
        data = {
            "name": "Varzhuhi",
            "job": "QA"
        }

    with allure.step('Send PATCH request to update user details'):
        response = requests.patch(url, json=data)
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify that the response contains the updated name'):
        assert response_data['name'] == data['name'], f"Expected name to be {data['name']}, but got {response_data['name']}"

    with allure.step('Verify that the response contains the updated job'):
        assert response_data['job'] == data['job'], f"Expected job to be {data['job']}, but got {response_data['job']}"

    with allure.step('Verify that the response contains an updatedAt field'):
        assert 'updatedAt' in response_data, 'Response should contain an updatedAt field'


