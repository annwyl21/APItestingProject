import requests
import logging as logger

class UtilApiRequests:
    def __init__(self, endpoint):
        self.base_url = "http://localhost:8080/api/v3/"
        self.endpoint = endpoint
        self.headers = {"Content-Type": "application/json"}

    def get_request(self, expected_status_code=200):
        path = self.base_url + self.endpoint
        response = requests.get(url=path, headers=self.headers)
        if response.status_code != expected_status_code:
            logger.info(f"GET API Response: {response.status_code}")
        return response
     