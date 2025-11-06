import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class DeleteMeme(BaseEndpointApi):

    def delete_meme(self, token=None, data=None):

        url = f"{self.url}/meme/{data}"
        headers = {"Authorization": token}
        response = requests.delete(url, headers=headers)
        return response.status_code
