import requests
import json
import pytest
from src.dev.utils.beer_utils import BeersMethodUtils

# Pre-Arrange
@pytest.fixture
def utils():
    return BeersMethodUtils()
# TODO: Exercise
# 1. Has a valid ‘abv’
# • It must be a double
# • It must not be null
# • It must not be an empty string
# • It must be over 4.0 
@pytest.mark.single_beer
def test_single_beer(utils):

    # Arrange
    brewed_after_param = "12-2015"
    # Act
    response=utils.get_beers_produced_after(brewed_after_param)
    for r in response:
        print(f"\n ID:{r.id}")

    # Assert
        
    # assert response.status_code ==  requests.codes.ok, f"Failed to get a successful response. Status code: {response.status_code}"
    # assert isinstance(response.json(), list), "Response json is not list collection"
    # assert response.json()[0]["id"] , "Response has no id attribute"

