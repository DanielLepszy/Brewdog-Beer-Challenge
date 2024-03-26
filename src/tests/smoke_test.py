import requests
import json
import pytest
from src.dev.base.base_requests import BaseRequests

# Pre-Arrange
@pytest.fixture
def base():
    return BaseRequests()

# Comment:
# Simple smoke test to verify status code, response type for many beers and response content
@pytest.mark.smoke
def test_get_all_beer(base):

    # Act
    response=base.get_beers()

    # Assert
    assert response.status_code ==  requests.codes.ok, f"Failed to get a successful response. Status code: {response.status_code}"
    assert isinstance(response.json(), list), "Response json is not list collection"
    assert response.json()[0]["id"] , "Response has no id attribute"

# Comment: 
# Test works for exisitng ID only. 
@pytest.mark.smoke
def test_get_single_beer(base):

    # Arrange 
    id = 1
    # Act
    response=base.get_single_beer_by_id(id)

    # Assert
    assert response.status_code ==  requests.codes.ok, f'Failed to get a successful response. Status code: {response.status_code}'
    assert isinstance(response.json(), list), "Response json is not list collection"
    assert response.json()[0]["id"]==id , "Wrong single beer id"
    assert len(response.json())==1 , f"Endpoint returns more than one beer. Result: {len(response.json())} beers object"

# Comment: 
# Negative scenario for non-existed ID for single beer. 
# We have fixed amount of beers (ids), thus the test should cover such case to verify whether API is consistent and return proper status code (404).  
@pytest.mark.smoke
def test_get_single_beer_for_no_existed_id(base):

    # Arrange 
    id = 9999999999999999

    # Act
    response=base.get_single_beer_by_id(id)

    # Assert
    assert response.status_code ==  requests.codes.not_found, f'No beer found that matches the ID {id}. Current status code: {response.status_code}'

# Comment: 
# Scenario for non-id as endpoint. 
@pytest.mark.smoke
def test_get_single_beer_for_non_int_endpoint(base):

    # Arrange 
    id = '1x'

    # Act
    response=base.get_single_beer_by_id(id)

    # Assert
    assert response.status_code ==  requests.codes.bad_request, f'beerId must be a number and greater than 0. Current beerId:{id}, status code: {response.status_code}'

# Comment: 
# Scenario for id=0. 
@pytest.mark.smoke
def test_get_single_beer_for_id_zero(base):

    # Arrange 
    id = 0

    # Act
    response=base.get_single_beer_by_id(id)

    # Assert
    assert response.status_code ==  requests.codes.bad_request, f'beerId must be a number and greater than 0. Current beerId:{id}, status code: {response.status_code}'

# Comment: 
# Scenario for simple SQL Injection. 
@pytest.mark.smoke
def test_get_single_beer_for_id_zero(base):

    # Arrange 
    id = '4 OR 1=1'

    # Act
    response=base.get_single_beer_by_id(id)

    # Assert
    assert response.status_code ==  requests.codes.bad_request, f'beerId must be a number and greater than 0. Current beerId:{id}, status code: {response.status_code}'

@pytest.mark.smoke
def test_get_random_beer(base):

    # Act
    response=base.get_random_beer()

    # Assert
    assert response.status_code ==  requests.codes.ok, f'Failed to get a successful response. Status code: {response.status_code}'
    assert isinstance(response.json(), list), "Response json is not list collection"
    assert response.json()[0]["id"] , "Random beer id not exist"
    assert len(response.json())==1 , f"RExpected 1 beer object. Result: {len(response.json())} beers object"
