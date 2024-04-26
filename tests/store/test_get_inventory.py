import pytest
import logging as logger
import requests
from model_inventory import Inventory

class TestInventoryAPI:

    @classmethod
    def setup_class(cls):
        endpoint = "http://localhost:8080/api/v3/store/inventory"
        headers = {"Accept": "application/json"}
        response = requests.get(url=endpoint, headers=headers)
        status_code = response.status_code
        json_data = response.json()
        # Class Variable
        cls.api_response = Inventory(status_code, json_data["approved"], json_data["placed"], json_data["delivered"])

    @pytest.mark.inventory
    @pytest.mark.status_code
    def test_get_status_code(self):
        logger.info("TEST: GET status code 200")
        # Access class variable using class name
        assert TestInventoryAPI.api_response.status_code == 200, f"Unexpected status code: {TestInventoryAPI.api_response.status_code}"

    @pytest.mark.inventory
    @pytest.mark.tcid01
    def test_values_positive(self):
        assert TestInventoryAPI.api_response.approved > 0
        assert TestInventoryAPI.api_response.placed > 0
        assert TestInventoryAPI.api_response.delivered > 0

    @pytest.mark.inventory
    @pytest.mark.tcid02
    def test_placed_bigger_than_delivered(self):
        assert TestInventoryAPI.api_response.placed > TestInventoryAPI.api_response.delivered

    @pytest.mark.inventory
    @pytest.mark.tcid03
    def test_approved_less_than_or_equal_to_1000(self):
        assert TestInventoryAPI.api_response.approved <= 1000
