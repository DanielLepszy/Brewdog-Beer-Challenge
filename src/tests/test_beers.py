import requests
import json
import pytest
from src.dev.base_requests import BaseRequests

# Pre-Arrange
@pytest.fixture
def base():
    return BaseRequests()

def test_verify_get_all_beers_response(base):

    # Arrange 
    endpoint = '/beers'

    # Act
    response=base.get_all_beers(endpoint)

    # Assert
    assert response.status_code ==  requests.codes.ok
    # assert response.json == 200
    print(f'All Beers: {response}')

