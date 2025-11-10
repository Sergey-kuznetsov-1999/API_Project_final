import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckAuthorize(BaseEndpointApi):

    def authorize(self):
        url = f"{self.url}/authorize"
        self.response = requests.post(url, json={"name": "Sergey_K"})
        self.status_code = self.response.status_code
        return self.response.json()

    def check_authorize(self, token: str):
        url = f"{self.url}/authorize/{token}"
        self.response = requests.get(url)
        self.status_code = self.response.status_code
        return self.response.status_code
