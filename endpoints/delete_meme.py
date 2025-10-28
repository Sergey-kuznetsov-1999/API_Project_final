import requests
from endpoints.Base_endpoint_api import BaseEndpointApi


class DeleteMeme(BaseEndpointApi):

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
            meme_id = meme_data.get("id")
            return meme_id
        else:
            return None

    def delete_meme_valid(self, token=None, meme_id=None):

        if meme_id is None:
            meme_id = self.create_meme_id(token)
            if meme_id is None:
                return "error"

        url = f"{self.url}/meme/{meme_id}"
        headers = {"Authorization": token}
        response = requests.delete(url, headers=headers)
        print(response)
        print(meme_id)
        print(response.status_code)
        print(response.text)

    def delete_meme_invalid(self, token=None, meme_id=None):

        url = f"{self.url}/meme/{meme_id}"
        headers = {"Authorization": token}
        response = requests.delete(url, headers=headers)
        print(response)
        print(meme_id)
        print(response.status_code)
        print(response.text)
