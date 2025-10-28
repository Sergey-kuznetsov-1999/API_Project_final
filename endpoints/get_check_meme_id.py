import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckMemeId(BaseEndpointApi):

    def check_meme_id_correct(self, token=None):
        url = f"{self.url}/meme/123"
        headers = {"Authorization": token}
        response = requests.get(url, headers=headers)
        return response.status_code == 200

    def check_meme_id_incorrect(self, token=None):
        url = f"{self.url}/meme/0"
        headers = {"Authorization": token}
        response = requests.get(url, headers=headers)
        return response.status_code == 404
