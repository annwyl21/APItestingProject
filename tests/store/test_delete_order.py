import pytest
import logging as logger
from tests.utilities.util_api_requests import UtilApiRequests
from tests.models.purchase_order import PurchaseOrder
from datetime import datetime as dt

pytestmark = pytest.mark.delete_order

purchase_order_id = 99
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
    
    api_request.post_request(request_body)
    response = api_request.delete_request(purchase_order_id)
    status_code = response.status_code
    return status_code

@pytest.mark.status_code
@pytest.mark.tcid13
def test_get_status_code(setup):
    logger.info("TEST: GET status code 200")
    assert setup == 200, f"Unexpected status code: {setup}"

@pytest.mark.tcid14
def test_attempt_get_invalid_id():
    logger.info("TEST: GET status code 405 - not found")
    endpoint = "store/order" + str(purchase_order_id)
    api_request = UtilApiRequests(endpoint)
    response = api_request.get_request()
    assert response.status_code == 404, f"Unexpected status code: {response.status_code}"