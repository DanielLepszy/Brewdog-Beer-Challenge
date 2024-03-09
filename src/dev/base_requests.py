import requests

class BaseRequests:

    headers = {'Content-Type': 'application/json'}

    def __init__(self):
        self.baseUrl = "https://api.punkapi.com/v2"

    def get_all_beers(self,endpoint:str):
         print(f'Debug - GET: {self.baseUrl}{endpoint}')
         return requests.get(self.baseUrl+endpoint)
         