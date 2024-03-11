from src.dev.base.punkapi_requests import BaseRequests 
from src.dev.data_model.beer_model import BeerModelInfo 
from datetime import datetime

class BeersMethodUtils(BaseRequests):
    def __init__(self):
        super().__init__()

    def get_beer_by_id(self,id:int) -> BeerModelInfo:
        if(id>0):
            json_data = self.get_single_beer_by_id(id).json()[0]
            return BeerModelInfo.from_dict(json_data)
    
    def get_random_beer(self,id:int) -> BeerModelInfo:
        json_data = self.get_single_beer_by_id(id).json()[0]
        return BeerModelInfo.from_dict(json_data)
    
    def  get_all_beers_per_page(self,page_number:int,per_page:int,incoming_params:dict = {}) -> list[BeerModelInfo]:
         beers_per_page:list[BeerModelInfo] = []
         params = {"page":page_number, "per_page":per_page}
         params.update(incoming_params)
         json_data=self.get_beers(params).json()
         for beer in json_data:
            beers_per_page.append(BeerModelInfo.from_dict(beer))

         return beers_per_page

    def get_all_beers(self,params:dict = {}) -> list[BeerModelInfo]:
        all_beers:list[BeerModelInfo] = []
        page_number = 1
        per_page = 80
        beers_per_page = [0]

        while beers_per_page:
             beers_per_page = self.get_all_beers_per_page(page_number,per_page,params)
             if beers_per_page:
                all_beers.extend(beers_per_page)
                page_number += 1
             
        return all_beers
    
    def get_beers_produced_after(self,brewed_after:str) -> list[BeerModelInfo]:
        params = {"brewed_after": brewed_after}
        return self.get_all_beers(params)

    def to_date_format(self,date_to_format:str, date_format:str) -> datetime:
        return datetime.strptime(date_to_format, date_format)

    

