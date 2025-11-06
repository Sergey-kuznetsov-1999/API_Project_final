import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckAuthorize(BaseEndpointApi):

    def authorize(self):
        url = f"{self.url}/authorize"
        response = requests.post(url, json={"name": "Sergey_K"})
        response.raise_for_status()
        return response.json()

    def check_authorize(self, token: str):
        url = f"{self.url}/authorize/{token}"
        response = requests.get(url)
        return response.status_code
