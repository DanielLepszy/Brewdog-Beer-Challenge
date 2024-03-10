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
    aa: str

    def set_value(data:dict,key:str):
          if(key in data):
                return dict[key]
          else:
                return None
    @classmethod
    def from_dict(cls, data: dict) -> "BeerModelInfo":
            return cls(
                id=cls.set_value(data,"id"),
                name=cls.set_value(data,"name"),
                tagline=cls.set_value(data,"tagline"),
                first_brewed=cls.set_value(data,"first_brewed"),
                description=cls.set_value(data,"description"),
                image_url=cls.set_value(data,"image_url"),
                abv=cls.set_value(data,"abv"),
                ibu=cls.set_value(data,"ibu"),
                target_fg=cls.set_value(data,"target_fg"),
                target_og=cls.set_value(data,"target_og"),
                ebc=cls.set_value(data,"ebc"),
                srm=cls.set_value(data,"srm"),
                ph=cls.set_value(data,"ph"),
                attenuation_level=cls.set_value(data,"attenuation_level"),
                volume=cls.set_value(data,"volume"),
                boil_volume=cls.set_value(data,"boil_volume"),
                method=cls.set_value(data,"method"),
                ingredients=cls.set_value(data,"ingredients"),
                food_pairing=cls.set_value(data,"food_pairing"),
                brewers_tips=cls.set_value(data,"brewers_tips"),
                contributed_by=cls.set_value(data,"contributed_by"),
            )
 