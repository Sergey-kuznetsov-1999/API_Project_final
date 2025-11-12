import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class DeleteMeme(BaseEndpointApi):

    def delete_meme(self, token=None, data=None):
        url = f"{self.url}/meme/{data}"
        headers = {"Authorization": token}
        self.response = requests.delete(url, headers=headers)
        self.status_code = self.response.status_code
        return self.response
