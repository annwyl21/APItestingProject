import requests
import logging as logger

class UtilApiRequests:
    def __init__(self):
        self.endpoint = "http://localhost:8080/api/v3/store/inventory"
        self.headers = {"Content-Type": "application/json"}

    def get_request(self, expected_status_code=200):
        response = requests.get(url=self.endpoint, headers=self.headers)
        if response.status_code != expected_status_code:
            logger.info(f"GET API Response: response.status_code")
        return response
        