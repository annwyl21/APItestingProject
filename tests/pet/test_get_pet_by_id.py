import pytest
import logging as logger
from tests.utilities.util_api_requests import UtilApiRequests

pytestmark = pytest.mark.pet_by_id

pet_id = 10

@pytest.fixture(scope='module')
def setup():
    endpoint = "pet/" + str(pet_id)
    api_request = UtilApiRequests(endpoint)
    response = api_request.get_request()
    return response

@pytest.mark.status_code
#@pytest.mark.usefixtures(setup)
def test_get_status_code(setup):
    logger.info("TEST: GET status code 200")
    assert setup.status_code == 200, f"Unexpected status code: {setup.status_code}"

@pytest.mark.tcid21
def test_returned_pet_has_same_id(setup):
    json_data = setup.json()
    assert json_data["id"] == pet_id
