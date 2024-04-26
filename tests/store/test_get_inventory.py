import pytest
import logging as logger
from util_api_requests import UtilApiRequests
from inventory import Inventory

pytestmark = pytest.mark.inventory

@pytest.fixture(scope='module')
def setup():
    endpoint = "store/inventory"
    api_request = UtilApiRequests(endpoint)
    response = api_request.get_request()
    status_code = response.status_code
    json_data = response.json()
    api_response = Inventory(status_code, json_data["approved"], json_data["placed"], json_data["delivered"])
    return api_response

@pytest.mark.status_code
def test_get_status_code(setup):
    logger.info("TEST: GET status code 200")
    assert setup.status_code == 200, f"Unexpected status code: {setup.status_code}"

@pytest.mark.tcid01
def test_values_positive(setup):
    assert setup.approved > 0
    assert setup.placed > 0
    assert setup.delivered > 0

@pytest.mark.tcid02
def test_placed_bigger_than_delivered(setup):
    assert setup.placed > setup.delivered

@pytest.mark.tcid03
def test_approved_less_than_or_equal_to_1000(setup):
    assert setup.approved <= 1000
