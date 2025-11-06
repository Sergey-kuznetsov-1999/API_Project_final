class BaseEndpointApi:
    url = "http://memesapi.course.qa-practice.com/"

    def __init__(self):
        self.response = None
        self.status_code = None

    def check_status_code_endpoint(self, status_code, expected_code):
        assert status_code == expected_code, f"Expected {expected_code}, got {status_code}"
