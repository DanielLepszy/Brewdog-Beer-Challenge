from dataclasses import dataclass

@dataclass
class BeerModelInfo:
    id: int
    name: str
    tagline: str
    first_brewed: str
    description: str
    image_url: str
    abv: float
    ibu: int # float?
    target_fg: int # float?
    target_og: int
    ebc: int
    srm: int
    ph: int
    attenuation_level: int
    volume: dict
    boil_volume: dict
    method: dict
    ingredients: dict
    food_pairing: list
    brewers_tips: str
    contributed_by: str

# TODO: Modify constructor based on https://opensource.com/article/21/9/unit-test-python
@classmethod
def from_dict(cls, data: dict) -> BeerModelInfo:
        return cls(
            temp=data["main"]["temp"],
            sunrise=format_date(data["sys"]["sunrise"]),
        )
    # def __init__(self,id,name,tagline,first_brewed,description,image_url,abv,ibu,target_fg,target_og,ebc,srm,ph,attenuation_level,
    #              volume,boil_volume,method,ingredients,food_pairing,brewers_tips,contributed_by) -> None:
    #     self.id=id 
    #     self.name=name
    #     self.tagline=tagline
    #     self.first_brewed=first_brewed
    #     self.description=description
    #     self.image_url=image_url
    #     self.abv=abv
    #     self.ibu=ibu
    #     self.target_fg=target_fg
    #     self.target_og=target_og
    #     self.ebc=ebc
    #     self.srm=srm
    #     self.ph=ph
    #     self.attenuation_level=attenuation_level
    #     self.volume=volume
    #     self.boil_volume=boil_volume
    #     self.method=method
    #     self.ingredients=ingredients
    #     self.food_pairing=food_pairing
    #     self.brewers_tips=brewers_tips
    #     self.contributed_by=contributed_by
