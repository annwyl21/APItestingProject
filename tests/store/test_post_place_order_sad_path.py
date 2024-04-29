import pytest
import logging as logger
from tests.utilities.util_api_requests import UtilApiRequests
from tests.models.purchase_order import PurchaseOrder
from datetime import datetime as dt

pytestmark = pytest.mark.place_order

purchase_order_id = 77
pet_id = 198772
quantity = 7
order_timestamp = "2024-04-26T12:10:36.034Z"
status = "approved"
complete = True

@pytest.mark.tcid17
def test_bad_request_id():
    bad_id = "unknown"
    endpoint = "store/order"
    api_request = UtilApiRequests(endpoint)

    request_body = {
        "id": bad_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": order_timestamp,
        "status": status,
        "complete": complete
        }
    
    response = api_request.post_request(request_body)
    assert response.status_code == 400, f"Unexpected status code: {response.status_code}"

@pytest.mark.tcid18
def test_bad_request_id():
    bad_id = 99999999
    endpoint = "store/order"
    api_request = UtilApiRequests(endpoint)

    request_body = {
        "id": bad_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": order_timestamp,
        "status": status,
        "complete": complete
        }
    
    response = api_request.post_request(request_body)
    assert response.status_code == 400, f"Unexpected status code: {response.status_code}"

@pytest.mark.tcid19
def test_bad_request_quantity():
    bad_quantity = 99999999
    endpoint = "store/order"
    api_request = UtilApiRequests(endpoint)

    request_body = {
        "id": purchase_order_id,
        "petId": pet_id,
        "quantity": bad_quantity,
        "shipDate": order_timestamp,
        "status": status,
        "complete": complete
        }
    
    response = api_request.post_request(request_body)
    assert response.status_code == 400, f"Unexpected status code: {response.status_code}"

@pytest.mark.tcid20
def test_order_complete_false():
    bad_complete = False
    endpoint = "store/order"
    api_request = UtilApiRequests(endpoint)

    request_body = {
        "id": purchase_order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": order_timestamp,
        "status": status,
        "complete": bad_complete
        }
    
    response = api_request.post_request(request_body)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"