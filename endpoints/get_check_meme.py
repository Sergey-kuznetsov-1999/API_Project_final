import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class CheckMeme(BaseEndpointApi):

    def check_meme(self, token=None):
        url = f"{self.url}/meme"
        headers = {"Authorization": token}
        self.response = requests.get(url, headers=headers)
        self.status_code = self.response.status_code
        return self.response.status_code

    def check_response_not_empty(self):
        response_data = self.response.json()
        assert response_data is not None
