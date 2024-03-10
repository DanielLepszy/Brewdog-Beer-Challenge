import requests

class BaseRequests:

    headers = {'Content-Type': 'application/json'}

    def __init__(self):
        self.baseUrl = "https://api.punkapi.com/v2"

    def get_beers(self,params:dict = {}):
         full_url = self.baseUrl+'/beers'
         print(f'\nDebug - GET /Beers: {full_url} with params:{params}')
         return requests.get(full_url,params)
         
    def get_single_beer_by_id(self,id:int):
            full_url = self.baseUrl+'/beers/'+ str(id)
            print(f'Debug - GET Single Beer: {full_url}')
            return requests.get(full_url)
    
    def get_random_beer(self):
        full_url = self.baseUrl+"/beers/random"
        print(f'Debug - GET Random Beer: {full_url}')
        return requests.get(full_url)
         