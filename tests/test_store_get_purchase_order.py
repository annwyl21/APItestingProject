import pytest
import logging as logger
from util_api_requests import UtilApiRequests
from model_purchase_order import PurchaseOrder
from datetime import datetime as dt

pytestmark = pytest.mark.get_purchase_order

@pytest.fixture(scope='module')
def setup():
    pet_id = "1"
    endpoint = "store/order/" + pet_id
    api_request = UtilApiRequests(endpoint)
    response = api_request.get_request()
    status_code = response.status_code
    json_data = response.json()
    print(json_data)
    api_response = PurchaseOrder(status_code, json_data["id"], json_data["petId"], json_data["quantity"], json_data["shipDate"], json_data["status"], json_data["complete"])
    return api_response

@pytest.mark.status_code
def test_get_status_code(setup):
    logger.info("TEST: GET status code 200")
    assert setup.status_code == 200, f"Unexpected status code: {setup.status_code}"

@pytest.mark.tcid04
def test_values_positive(setup):
    assert setup.po_id > 0
    assert setup.pet_id > 0
    assert setup.quantity > 0

@pytest.mark.tcid05
def test_quantity_greater_than_zero(setup):
    assert setup.quantity > 0

@pytest.mark.tcid06
def test_date(setup):
    timestamp = dt.strptime(setup.shipdate, "%Y-%m-%dT%H:%M:%S.%f%z")
    date = timestamp.date()
    today = date.today()
    assert date == today