import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckMemeId(BaseEndpointApi):

    def check_meme_id_correct(self, token=None, created_data=None):
        url = f"{self.url}/meme/{created_data}"
        headers = {"Authorization": token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"HTTP {response.status_code}. Response: {response.text}")

    def check_meme_id_incorrect(self, token=None):
        url = f"{self.url}/meme/0"
        headers = {"Authorization": token}
        response = requests.get(url, headers=headers)
        return response.status_code
