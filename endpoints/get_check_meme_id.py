import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckMemeId(BaseEndpointApi):

    def check_meme_id(self, token=None, created_data=None):
        url = f"{self.url}/meme/{created_data}"
        headers = {"Authorization": token}
        response = requests.get(url, headers=headers)
        return response.status_code
