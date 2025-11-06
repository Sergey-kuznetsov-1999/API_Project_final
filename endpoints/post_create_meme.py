import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class PostCreateMeme(BaseEndpointApi):

    def create_meme_valid(self, token=None, data=None):

        if data is None:
            data = {
                "text": "new meme",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCAUrJkyCKZIY3UMh4SD4YpcBMgzCZBhF1UQ&s",
                "tags": ["cool", "happy"],
                "info": {"author": "noname", "color": "gray"}
            }
        url = f"{self.url}/meme"
        self.response = requests.post(
            url,
            headers={"Authorization": token},
            json=data
        )

        self.status_code = self.response.status_code

        try:
            return self.response.json()
        except:
            return self.status_code

    def create_meme_id(self, token=None):
        url = f"{self.url}/meme"
        self.response = requests.post(
            url,
            headers={"Authorization": token},
            json={
                "text": "new meme",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCAUrJkyCKZIY3UMh4SD4YpcBMgzCZBhF1UQ&s",
                "tags": ["cool", "happy"],
                "info": {"author": "noname", "color": "gray"}
            }
        )
        if self.response.status_code == 200:
            meme_data = self.response.json()
            return meme_data.get("id")
        else:
            return None
