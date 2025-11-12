import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckMemeId(BaseEndpointApi):

    def check_meme_id(self, token=None, created_data=None):
        url = f"{self.url}/meme/{created_data}"
        headers = {"Authorization": token}
        self.response = requests.get(url, headers=headers)
        self.status_code = self.response.status_code
