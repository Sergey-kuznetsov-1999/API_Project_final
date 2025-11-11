import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class PutUpdateMeme(BaseEndpointApi):

    def default_put_meme_data(self, created_id):
        return {
            "id": created_id,
            "text": "Update meme",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
            "tags": ["wow", "monkey"],
            "info": {"author": "it's me", "color": "black"}
        }

    def default_put_meme_data_incorrect_id(self):
        return {
            "id": 0,
            "text": "Update meme",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
            "tags": ["wow", "monkey"],
            "info": {"author": "it's me", "color": "black"}
        }

    def default_put_meme_data_without_id(self):
        return {
            "text": "Update meme",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
            "tags": ["wow", "monkey"],
            "info": {"author": "it's me", "color": "black"}
        }

    def put_update_meme(self, token=None, created_data=None, update_data=None):
        url = f"{self.url}/meme/{created_data}"
        self.response = requests.put(
            url,
            headers={"Authorization": token},
            json=update_data
        )
        self.status_code = self.response.status_code
        return self.response
