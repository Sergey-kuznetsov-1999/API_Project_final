import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckAuthorize(BaseEndpointApi):

    def check_authorize(self, token: str):
        url = f"{self.url}/authorize/{token}"
        response = requests.get(url)
        return response.status_code