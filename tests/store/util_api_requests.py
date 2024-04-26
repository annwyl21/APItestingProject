import requests
import logging as logger
import config

class UtilApiRequests:
    def __init__(self, endpoint):
        # self.base_url = "http://localhost:8080/api/v3/"
        self.base_url = config.BASE_URL
        self.endpoint = endpoint
        self.headers = {"Content-Type": "application/json"}

    def get_request(self, expected_status_code=200):
        path = self.base_url + self.endpoint
        response = requests.get(url=path, headers=self.headers)
        if response.status_code != expected_status_code:
            logger.info(f"Unexpected GET API Response: {response.status_code} not {expected_status_code}")
        return response
    
    def post_request(self, request_body, expected_status_code=200):
        path = self.base_url + self.endpoint
        response = requests.post(url=path, json=request_body, headers=self.headers)
        if response.status_code != expected_status_code:
            logger.info(f"Unexpected GET API Response: {response.status_code} not {expected_status_code}")
        return response
    
    def delete_request(self, purchase_order_id, expected_status_code=200):
        path = self.base_url + self.endpoint + "/" + str(purchase_order_id)
        response = requests.delete(url=path, headers=self.headers)
        return response