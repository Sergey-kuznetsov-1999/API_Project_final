import requests


class BaseEndpointApi:
    url = "http://memesapi.course.qa-practice.com/"

    def __init__(self):
        self.response = None

    def authorize(self):
        url = f"{self.url}/authorize"
        response = requests.post(url, json={"name": "Sergey_K"})
        response.raise_for_status()
        return response.json()
