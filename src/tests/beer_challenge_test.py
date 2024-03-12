from nrt_pytest_soft_asserts.soft_asserts import SoftAsserts
import pytest
import requests
from requests.models import Response
from src.dev.utils.beer_utils import BeersRequestUtils
from src.dev.data_model.beer_model import BeerModelInfo 

@pytest.mark.api 
class TestApi:

    # Arrange before-all
    @pytest.fixture(scope="module", autouse=True)
    def soft_assert(self):
        return  SoftAsserts()
    @pytest.fixture(scope="module", autouse=True)
    def utils(self):
        return BeersRequestUtils()
    @pytest.fixture(scope="module", autouse=True)
    def date_format(self):
        return "%m/%Y"
    @pytest.fixture(scope="module", autouse=True)
    def date_after(self):
        return "12/2015"
    @pytest.fixture(scope="module", autouse=True)
    def per_page(self):
        return 80
    @pytest.fixture(scope="module", autouse=True)
    def page_number(self):
        return 1
    @pytest.fixture(scope="module", autouse=True)
    def get_beers_after_dec(self,utils,date_after,page_number,per_page):
        return utils.get_beers_produced_after({ "page":page_number, "per_page":per_page,"brewed_after":date_after })
    # @pytest.fixture(scope="module", autouse=True)
    # def all_beers_modules(self) -> list[BeerModelInfo]:
    #     return []
    
    @pytest.mark.dependency(name="produced_beers_after_dec")
    @pytest.mark.first
    def test_beers_produced_after_december_2015(self,utils,soft_assert,date_after,date_format,page_number,per_page):

        # Arrange
        brewed_after = utils.to_date_format(date_after,date_format)
        params = { "page":page_number, "per_page":per_page,"brewed_after":date_after }

        # Make all GET requests for single page (max elements pare page is 80) 
        page_response_list:list[Response] = utils.get_beers_produced_after(params)

        # Verify all GET requests return 200 status
        for response_per_page in page_response_list:
            assert response_per_page.status_code == requests.codes.ok, f'Status code {response_per_page.status_code} for {response_per_page.request.path_url} '
        
        # Marge all json results from each page and map json into BeerModelInfo models 
        self.all_beers_modules = utils.get_all_beer_models_from_pages(page_response_list)

        for beer in all_beers_modules:
            print("aa")
            soft_assert.assert_is_not_none(beer.id, f"\n ID is None")
            soft_assert.assert_is_not_none(beer.first_brewed, f"\nFor beerId {beer.id} - The first_brewed is None")
            soft_assert.assert_true(brewed_after < utils.to_date_format(beer.first_brewed,date_format),
                                    f"\nFor beerId {beer.id} - The first_brewed is lower than {brewed_after}")    
        
        soft_assert.assert_all()

    @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    def test_if_abv_is_not_null(self,soft_assert,all_beers_modules):

        # Assert
        for beer in self.all_beers_modules:
            print("asdas")
            soft_assert.assert_is_not_none(beer.abv, f"\nFor beerId {beer.id} - the abv attribute is Null.")
        
        soft_assert.assert_all()

    # Comment:
    # This tests verify wheter abv is float numbers not double because there is no dobule data type in python
    # The tests for empty string is not necessary because I use mapping response to BeerModelInfo where I typed abv as float type. 
    # If any empty string occurs then the mapping exception will be thrown
    # @pytest.mark.api
    # @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    # def test_if_abv_is_double(soft_assert):

        # Assert
        # for beer in beers_produced_after_dec:
        #     soft_assert.assert_true(type(beer.abv)== float, f"\nFor beerId {beer.id} - the abv attribute is not float. Expected: float, Result:{type(beer.abv)}")
        
        # soft_assert.assert_all()


    # @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    # def test_if_abv_is_not_empty_string(soft_assert,beers_produced_after_december):

    #     # Assert
    #     for beer in beers_produced_after_december:
    #         soft_assert.assert_true(beer.abv and not beer.abv.isspace(), f"\nFor beerId {beer.id} - the abv attribute contains empty string.")
        
    #     soft_assert.assert_all()


    # @pytest.mark.api
    # @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    # def test_if_abv_is_grater_than(soft_assert):
        
        # #Arrange
        # supplied_number = 4.0

        # # Assert
        # for beer in beers_produced_after_dec:
        #     soft_assert.assert_true( beer.abv> supplied_number, f"\nFor beerId {beer.id} produced after December 2015 - the abv attribute is not grater than {supplied_number}. Result: {beer.abv}")
        
        # soft_assert.assert_all()

    # @pytest.mark.api
    # @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    # def test_if_name_is_not_null(soft_assert):

    #     # Assert
    #     for beer in beers_produced_after_dec:
    #         soft_assert.assert_is_not_none(beer.name, f"\nFor beerId {beer.id} - the name attribute is None")
        
    #     soft_assert.assert_all()

    # @pytest.mark.api
    # @pytest.mark.dependency(depends=["produced_beers_after_dec"])
    # def test_if_name_is_not_empty_string(soft_assert):

    #     # Assert
    #     for beer in beers_produced_after_dec:
    #         soft_assert.assert_is_not_none(beer.name and not beer.name.isspace(), f"\nFor beerId {beer.id} - the name attribute is empty string")
        
    #     soft_assert.assert_all()


    # - - - - - - ADDITIONAL TESTS - - - - - - - - 
        
    # @pytest.mark.additional
    # def test_if_abv_gt_param_return_proper_response(soft_assert,utils):
        
    #     #Arrange
    #     supplied_number = 4.0
    #     brewed_after = "12/2015"

    #     #Act 
    #     beers:list[BeerModelInfo] = utils.get_beers_with_abv_gt_than(brewed_after,supplied_number)

    #     # Assert
    #     for beer in beers:
    #         soft_assert.assert_true( beer.abv > supplied_number, f"\nFor beerId {beer.id} the abv attribute is not grater than {supplied_number}. Result: {beer.abv}")
        
    #     soft_assert.assert_all()


    # @pytest.mark.additional
    # def test_if_abv_lt_param_return_proper_response(soft_assert,utils):
        
    #     #Arrange
    #     supplied_number = 4.0
    #     brewed_after = "12/2015"

    #     #Act 
    #     beers:list[BeerModelInfo] = utils.get_beers_with_abv_lt_than(brewed_after,supplied_number)

    #     # Assert
    #     for beer in beers:
    #         soft_assert.assert_true( beer.abv < supplied_number, f"\nFor beerId {beer.id} the abv attribute is not grater than {supplied_number}. Result: {beer.abv}")
        
    #     soft_assert.assert_all()
