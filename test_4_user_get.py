import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Listing')
@allure.title('Get user list')
@allure.description('This test retrieves a list of users from the API and verifies the response structure and content')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_users_list_get():
    with allure.step('Define the API endpoint'):
        url = 'https://reqres.in/api/users?page=2'

    with allure.step('Send GET request to retrieve user list'):
        response = requests.get(url)
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains a page field'):
        assert 'page' in response_data, 'Response should contain a page field'
        assert response_data['page'] == 2, f"Expected page to be 2, but got {response_data['page']}"

    with allure.step('Verify response contains a data field'):
        assert 'data' in response_data, 'Response should contain a data field'
        assert isinstance(response_data['data'], list), 'Data should be a list'
        assert len(response_data['data']) > 0, 'Data list should not be empty'

    first_user = response_data['data'][0]
    expected_keys = {'id', 'email', 'first_name', 'last_name', 'avatar'}

    with allure.step('Verify the structure of the first user in the list'):
        assert expected_keys.issubset(first_user.keys()), f'Missing expected keys in the first user: {expected_keys - set(first_user.keys())}'


@allure.feature('User Management')
@allure.suite('Single User Retrieval')
@allure.title('Get a single user by ID')
@allure.description('This test retrieves a single user by ID from the API and verifies the response structure and content')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_single_user_get():
    with allure.step('Define the API endpoint'):
        url = 'https://reqres.in/api/users/2'

    with allure.step('Send GET request to retrieve a single user'):
        response = requests.get(url)
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    with allure.step('Verify response time is within acceptable limits'):
        assert response.elapsed.total_seconds() < 2, f'Response took too long: {response.elapsed.total_seconds()} seconds'

    response_data = response.json()

    with allure.step('Verify response contains a data field'):
        assert 'data' in response_data, 'Response should contain a data field'
        user_data = response_data['data']
        expected_keys = {'id', 'email', 'first_name', 'last_name', 'avatar'}

    with allure.step('Verify the structure of user data'):
        assert expected_keys.issubset(user_data.keys()), f'Missing expected keys in the user data: {expected_keys - set(user_data.keys())}'

    with allure.step('Verify the user ID in the response'):
        assert user_data['id'] == 2, f"Expected user ID to be 2, but got {user_data['id']}"


@allure.feature('User Management')
@allure.suite('Single User Retrieval')
@allure.title('Get a single user by ID not found')
@allure.description('This test attempts to retrieve a single user by a non-existent ID and verifies that the API responds with a 404 status code.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_single_user_not_found():
    with allure.step('Define the API endpoint for a non-existent user'):
        url = 'https://reqres.in/api/users/23'

    with allure.step('Send GET request to retrieve a non-existent user'):
        response = requests.get(url)
        assert response.status_code == 404, f'Expected status code 404, but got {response.status_code}'


