import pytest
import json
import logging as logger
from util_api_requests import UtilApiRequests
from model_purchase_order import PurchaseOrder
from datetime import datetime as dt

pytestmark = pytest.mark.place_order

purchase_order_id = 10
pet_id = 198772
quantity = 7
order_timestamp = "2024-04-26T12:10:36.034Z"
status = "approved"
complete = True

@pytest.fixture(scope='module')
def setup():
    endpoint = "store/order"
    api_request = UtilApiRequests(endpoint)

    request_body = {
        "id": purchase_order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": order_timestamp,
        "status": status,
        "complete": complete
        }
    
    response = api_request.post_request(request_body)
    status_code = response.status_code
    json_data = response.json()
    api_response = PurchaseOrder(status_code, json_data["id"], json_data["petId"], json_data["quantity"], json_data["shipDate"], json_data["status"], json_data["complete"])
    return api_response

@pytest.mark.status_code
def test_get_status_code(setup):
    logger.info("TEST: GET status code 200")
    assert setup.status_code == 200, f"Unexpected status code: {setup.status_code}"

@pytest.mark.tcid07
def test_order_id_same(setup):
    assert setup.po_id == purchase_order_id

@pytest.mark.tcid08
def test_pet_id_same(setup):
    assert setup.pet_id == pet_id

@pytest.mark.tcid09
def test_quantity_same(setup):
    assert setup.quantity == quantity

@pytest.mark.tcid10
def test_date_same(setup):
    timestamp_sent = dt.strptime(order_timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")
    date_sent = timestamp_sent.date()
    timestamp_retrieved = dt.strptime(setup.shipdate, "%Y-%m-%dT%H:%M:%S.%f%z")
    date_retrieved = timestamp_retrieved.date()
    assert date_retrieved == date_sent

@pytest.mark.tcid11
def test_status_same(setup):
    assert setup.status == status

@pytest.mark.tcid12
def test_complete_same(setup):
    assert setup.complete == complete