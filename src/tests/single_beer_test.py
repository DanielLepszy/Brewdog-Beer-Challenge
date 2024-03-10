import requests
import json
import pytest
from src.dev.utils.beer_utils import BeersMethodUtils

# Pre-Arrange
@pytest.fixture
def utils():
    return BeersMethodUtils()

@pytest.mark.single_beer
def test_single_beer(utils):

    # Arrange
    id = 1 
    # Act
    # response=utils.get_beer_by_id(id)
    response=utils.get_all_beers()
    for r in response:
        print(f"\n ID:{r}")

    # Assert
    # assert response.status_code ==  requests.codes.ok, f"Failed to get a successful response. Status code: {response.status_code}"
    # assert isinstance(response.json(), list), "Response json is not list collection"
    # assert response.json()[0]["id"] , "Response has no id attribute"

