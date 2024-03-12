from src.dev.base.base_requests import BaseRequests 
from src.dev.data_model.beer_model import BeerModelInfo 
from src.dev.utils.helpers import HelperMethods 
from src.dev.utils.mappers import BeerModelMapper 
import requests
from requests.models import Response
from requests.models import Response

class BeersRequestUtils(BaseRequests,HelperMethods,BeerModelMapper):
    def __init__(self):
        super().__init__()

    def get_all_beers_per_page(self,params:dict = {}) -> Response:
         return self.get_beers(params)
        
    def get_all_beers(self,params:dict = {}) -> list[Response]:
        all_beers_response:list[Response] = []
        beers_per_page_resp:Response = self.get_all_beers_per_page(params)
   
        if beers_per_page_resp.status_code != requests.codes.ok:
            return [beers_per_page_resp]
        elif beers_per_page_resp.status_code == requests.codes.ok and len(beers_per_page_resp.json()) > 0:
            all_beers_response.append(beers_per_page_resp)
            params["page"] += 1

            while beers_per_page_resp.json():
                beers_per_page_resp = self.get_all_beers_per_page(params)
                if beers_per_page_resp.json() is not None and len(beers_per_page_resp.json()) > 0:
                    all_beers_response.append(beers_per_page_resp)
                    params["page"] += 1
                else:
                    break

        return all_beers_response
        
    
    def get_beers_produced_after(self,params:dict) -> list[Response]:
        return self.get_all_beers(params)
