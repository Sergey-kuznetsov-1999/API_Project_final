import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class PutUpdateMeme(BaseEndpointApi):

    def put_update_meme(self, token=None, created_data=None, update_data=None):
        url = f"{self.url}/meme/{created_data}"
        self.response = requests.put(
            url,
            headers={"Authorization": token},
            json=update_data
        )
        return self.response
