import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class PostCreateMeme(BaseEndpointApi):

    def create_meme_valid(self, token=None):
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
        return self.response.json()

    def create_meme_without_text_fild(self, token=None):
        url = f"{self.url}/meme"
        self.response = requests.post(
            url,
            headers={"Authorization": token},
            json={
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCAUrJkyCKZIY3UMh4SD4YpcBMgzCZBhF1UQ&s",
                "tags": ["cool", "happy"],
                "info": {"author": "noname", "color": "gray"}
            }
        )
        return self.response.status_code == 400

    def create_meme_without_url_filed(self, token=None):
        url = f"{self.url}/meme"
        self.response = requests.post(
            url,
            headers={"Authorization": token},
            json={
                "text": "new meme",
                "tags": ["cool", "happy"],
                "info": {"author": "noname", "color": "gray"}
            }
        )
        return self.response.status_code == 400

    def create_meme_without_tags_filed(self, token=None):
        url = f"{self.url}/meme"
        self.response = requests.post(
            url,
            headers={"Authorization": token},
            json={
                "text": "new meme",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCAUrJkyCKZIY3UMh4SD4YpcBMgzCZBhF1UQ&s",
                "info": {"author": "noname", "color": "gray"}
            }
        )
        return self.response.status_code == 400

    def create_meme_without_info_filed(self, token=None):
        url = f"{self.url}/meme"
        self.response = requests.post(
            url,
            headers={"Authorization": token},
            json={
                "text": "new meme",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCAUrJkyCKZIY3UMh4SD4YpcBMgzCZBhF1UQ&s",
                "tags": ["cool", "happy"]
            }
        )
        return self.response.status_code == 400

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
