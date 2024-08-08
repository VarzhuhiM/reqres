import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('Delayed Response Retrieval')
@allure.title('Retrieve users with a delay')
@allure.description('This test retrieves a list of users with a simulated delay and verifies the response structure and content.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delayed_response_get():
    with allure.step('Define the API endpoint with a delay'):
        url = 'https://reqres.in/api/users?delay=3'

    with allure.step('Send GET request to retrieve users with delay'):
        response = requests.get(url)
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains a data field'):
        assert 'data' in response_data, 'Response should contain a data field'

    with allure.step('Verify that data is a list'):
        assert isinstance(response_data['data'], list), 'Data should be a list'

    with allure.step('Verify that data list is not empty'):
        assert len(response_data['data']) > 0, 'Data list should not be empty'

    with allure.step('Verify the structure of the first user in the data list'):
        first_user = response_data['data'][0]
        expected_keys = {'id', 'email', 'first_name', 'last_name', 'avatar'}
        assert expected_keys.issubset(first_user.keys()), f'Missing expected keys in the first user: {expected_keys - set(first_user.keys())}'
