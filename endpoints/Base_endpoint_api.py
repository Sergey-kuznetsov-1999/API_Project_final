class BaseEndpointApi:
    url = "http://memesapi.course.qa-practice.com/"

    def __init__(self):
        self.response = None
        self.status_code = None

    def check_status_code_endpoint(self, expected_code):
        assert self.response.status_code == expected_code, (f"Expected {expected_code}, "
                                                            f"got {self.response.status_code}")

    def check_id_is_correct(self, expected_id):
        response_data = self.response.json()
        actual_id = response_data['id']
        assert int(actual_id) == int(expected_id), f"Expected ID {expected_id}, but got {actual_id}"
