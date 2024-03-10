import requests
from src.dev.base.punkapi_requests import BaseRequests 
from src.dev.data_model.beer_model import BeerModelInfo 

class BeersMethodUtils(BaseRequests):
    def __init__(self):
        super().__init__()

    def get_beer_by_id(self,id:int) -> BeerModelInfo:
        if(id>0):
            json_data = self.get_single_beer_by_id(id).json()[0]
            return BeerModelInfo.from_dict(json_data)
            


