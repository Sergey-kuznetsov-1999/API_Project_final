import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckMeme(BaseEndpointApi):

    def check_meme(self, token=None):
        url = f"{self.url}/meme"
        headers = {"Authorization": token}
        response = requests.get(url, headers=headers)
        return response.status_code
