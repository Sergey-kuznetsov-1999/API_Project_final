import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class PutUpdateMeme(BaseEndpointApi):

    def put_update_meme_valid(self, token=None):
        url = f"{self.url}/meme/1395"
        self.response = requests.put(
            url,
            headers={"Authorization": token},
            json={
                "id": 1395,
                "text": "Update meme",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
                "tags": ["wow", "monkey"],
                "info": {"author": "it's me", "color": "black"}
            }
        )
        return self.response.json()

    def put_update_meme_not_found(self, token=None):
        url = f"{self.url}/meme/0"
        self.response = requests.put(
            url,
            headers={"Authorization": token},
            json={
                "id": 0,
                "text": "Update meme",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
                "tags": ["wow", "monkey"],
                "info": {"author": "it's me", "color": "black"}
            }
        )
        return self.response.status_code == 404

    def put_update_meme_invalid(self, token=None):
        url = f"{self.url}/meme/1395"
        self.response = requests.put(
            url,
            headers={"Authorization": token},
            json={
                "text": "Update meme",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXyZvNLQC-bdb4KEUt7we_r87XmeH8XhZtJg&s",
                "tags": ["wow", "monkey"],
                "info": {"author": "it's me", "color": "black"}
            }
        )
        return self.response.status_code == 400
