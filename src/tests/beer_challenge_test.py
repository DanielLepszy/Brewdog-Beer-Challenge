from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
import pytest
import requests
from requests.models import Response
from src.dev.utils.beer_utils import BeersRequestUtils
from src.dev.data_model.beer_model import BeerModelInfo 


@pytest.mark.api 
class TestApi:

    # Arrange before-all
    @pytest.fixture(scope="module",autouse=True)
    def soft_assert(self):
        return SoftAsserts()

    @pytest.fixture(scope="module",autouse=True)
    def utils(self):
        return BeersRequestUtils()

    @pytest.fixture(scope="module", autouse=True)
    def date_format(self):
        return "%m/%Y"
    @pytest.fixture(scope="module", autouse=True)
    def date_after(self):
        return "12/2015"

    @pytest.fixture(scope="module", autouse=True)
    def beers_per_page_response_after_dec_2015(self,utils,date_after):
        params = { "page":1, "per_page":80,"brewed_after":date_after }
        return utils.get_all_beers(params)
    
    @pytest.fixture(scope="module", autouse=True)
    def beers_models_after_dec_2015(self,utils,beers_per_page_response_after_dec_2015):
        return utils.map_beer_model_from_page_resp(beers_per_page_response_after_dec_2015)
        
    @pytest.mark.dependency(name="produced_beers_after_dec")
    @pytest.mark.first
    def test_beers_produced_after_december_2015(self,utils,soft_assert,date_after,date_format,beers_per_page_response_after_dec_2015,beers_models_after_dec_2015):

        # Verify all GET requests return 200 status
        for response_per_page in beers_per_page_response_after_dec_2015:
            assert response_per_page.status_code == requests.codes.ok, f'Status code {response_per_page.status_code} for {response_per_page.request.path_url} '
        
        # Marge all json results from each page and map json into BeerModelInfo models 
        beer_models = utils.map_beer_model_from_page_resp(beers_per_page_response_after_dec_2015)

        for beer in beer_models:
            soft_assert.assert_is_not_none(beer.id, f"\n ID is None")
            soft_assert.assert_is_not_none(beer.first_brewed, f"\nFor beerId {beer.id} - The first_brewed is None")
            soft_assert.assert_true(utils.to_date_format(date_after,date_format) < utils.to_date_format(beer.first_brewed,date_format),
                                    f"\nFor beerId {beer.id} - The first_brewed is lower than {date_after}")    
        
        soft_assert.assert_all()

    @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    def test_if_abv_is_not_null(self,soft_assert,beers_models_after_dec_2015):

        # Assert
        for beer in beers_models_after_dec_2015:
            soft_assert.assert_is_not_none(beer.abv, f"\nFor beerId {beer.id} - the abv attribute is Null.")
        
        soft_assert.assert_all()

    # Comment:
    # This tests verify wheter abv is float numbers not double because there is no dobule data type in python
    # The tests for empty string is not necessary because I use mapping response to BeerModelInfo where I typed abv as float type. 
    # If any empty string occurs then the mapping exception will be thrown
    @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    def test_if_abv_is_double(self,soft_assert,beers_models_after_dec_2015):
        
        for beer in beers_models_after_dec_2015:
            soft_assert.assert_true(type(beer.abv)==float, f"\nFor beerId {beer.id} - the abv attribute is not float. Expected: float, Result:{type(beer.abv)}")
        
        soft_assert.assert_all()


    @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    def test_if_abv_is_not_empty_string(self,soft_assert,beers_models_after_dec_2015):
        
        # Assert
        for beer in beers_models_after_dec_2015:
            soft_assert.assert_true(beer.abv and not str(beer.abv).isspace(), f"\nFor beerId { beer.id } - the abv attribute contains empty string.")
        
        soft_assert.assert_all()


    @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    def test_if_abv_is_grater_than(self,soft_assert,beers_models_after_dec_2015):
        
        #Arrange
        supplied_number = 4.0
        # Assert
        for beer in beers_models_after_dec_2015:
            soft_assert.assert_true(beer.abv > supplied_number, f"\nFor beerId {beer.id} produced after December 2015 - the abv attribute is not grater than {supplied_number}. Result: {beer.abv}")
        
        soft_assert.assert_all()

    @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    def test_if_name_is_not_null(self,soft_assert,beers_models_after_dec_2015):

        # Assert
        for beer in beers_models_after_dec_2015:
            soft_assert.assert_is_not_none(beer.name, f"\nFor beerId {beer.id} - the name attribute is None")
        
        soft_assert.assert_all()

    @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    def test_if_name_is_not_empty_string(self,soft_assert,beers_models_after_dec_2015):

        # Assert
        for beer in beers_models_after_dec_2015:
            soft_assert.assert_is_not_none(beer.name and not beer.name.isspace(), f"\nFor beerId {beer.id} - the name attribute is empty string")
        
        soft_assert.assert_all()


    # - - - - - - ADDITIONAL TESTS - - - - - - - - 
        
    @pytest.mark.additional
    def test_if_abv_gt_param_return_proper_response(self,soft_assert,utils,date_after):
        
        #Arrange
        params = { "page":1, "per_page":80,"brewed_after": date_after, "abv_gt":4.0 }
        responses:list[Response] = utils.get_all_beers(params)
        
        for response in responses:
            assert response.status_code == 200, f'Status code {response.status_code} for {response.request.path_url} '
        #Act 
        beers:list[BeerModelInfo] = utils.map_beer_model_from_page_resp(responses)
        # Assert
        for beer in beers:
            soft_assert.assert_true( beer.abv > params["abv_gt"], f"\nFor beerId {beer.id} the abv attribute is lower than abv_gt:{params['abv_gt']}. Result: {beer.abv}")
        
        soft_assert.assert_all()


    @pytest.mark.additional
    def test_if_abv_lt_param_return_proper_response(self,soft_assert,utils,date_after):
        
        #Arrange
        params = { "page":1, "per_page":80,"brewed_after": date_after, "abv_lt":4.0 }
        responses:list[Response] = utils.get_all_beers(params)
        
        for response in responses:
            assert response.status_code == 200, f'Status code {response.status_code} for {response.request.path_url} '
        #Act 
        beers:list[BeerModelInfo] = utils.map_beer_model_from_page_resp(responses)
        # Assert
        for beer in beers:
            soft_assert.assert_true( beer.abv < params["abv_lt"], f"\nFor beerId {beer.id} the abv attribute is grater than abv_lt:{params['abv_lt']}. Result: {beer.abv}")
        
        soft_assert.assert_all()

    @pytest.mark.additional
    def test_get_single_beer_by_id(self,soft_assert,utils):
        
        #Arrange
        response:Response = utils.get_single_beer_by_id(1)
        assert response.status_code == 200, f'Status code {response.status_code} for {response.request.path_url} '

        #Act 
        beer :BeerModelInfo = utils.map_to_beer_model(response.json()[0])
        soft_assert.assert_equal(beer.id, 1, f"Wrong id in single beer in {response.request.path_url}")
        # Assert
        soft_assert.assert_all()
