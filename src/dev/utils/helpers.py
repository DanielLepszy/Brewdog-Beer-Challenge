from requests.models import Response
from datetime import datetime

from src.dev.data_model.beer_model import BeerModelInfo
from src.dev.utils.mappers import BeerModelMapper

class HelperMethods:

    def merge_all_page_reponse_into_one_json(self,reposne_pages: list[Response]) -> list[dict]:
        json_beers_list: list[dict] = []
    
        for response in reposne_pages:
            json_beers_list.extend(response.json())

        return json_beers_list
    
    def map_beer_model_from_page_resp(self,reposne_pages: list[Response]) -> list[BeerModelInfo]:
        json_data = self.merge_all_page_reponse_into_one_json(reposne_pages)
        all_gathered_beers:list[BeerModelInfo] = BeerModelMapper.map_json_objects_to_beer_models(self,json_data)

        return all_gathered_beers

    def to_date_format(self,date_to_format:str, date_format:str) -> datetime:
        return datetime.strptime(date_to_format, date_format)

    