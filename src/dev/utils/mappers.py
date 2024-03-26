from requests.models import Response 
from src.dev.data_model.beer_model import BeerModelInfo 

class BeerModelMapper:

    def map_to_beer_model(self,json: dict) -> BeerModelInfo:
        return BeerModelInfo.from_dict(json)
    
    def map_json_objects_to_beer_models(self,json: list[dict]) -> list[BeerModelInfo]:
        beers:list[BeerModelInfo] = []
        for beer in json:
            beers.append(self.map_to_beer_model(beer))

        return beers
 