import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Deletion')
@allure.title('Delete a user')
@allure.description('This test deletes a user and verifies the response status code.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_user_delete():
    user_id = 2
    url = f'https://reqres.in/api/users/{user_id}'

    with allure.step('Send DELETE request to delete the user'):
        response = requests.delete(url)
        assert response.status_code == 204, f'Expected status code 204, but got {response.status_code}'


