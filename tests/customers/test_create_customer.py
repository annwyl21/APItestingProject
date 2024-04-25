
import pytest
import logging as logger
# from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
# from ssqaapitest.src.helpers.customers_helper import CustomerHelper
# from ssqaapitest.src.dao.customers_dao import CustomersDAO
# from ssqaapitest.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.customers
@pytest.mark.tcid001
def test_create_customer():

    logger.info("TEST: Create new customer with email and password only.")

    # create the payload
    email = "test1@tester.com"
    customer_details = {
        "email": email, 
        "firstname": "Mrs", 
        "lastname": "Tester"
        }
    password = "password"
    
    payload = {
        "customer": customer_details,
        "password": password
    }

    # make the call
    access_token = "cdxf96vcah8pbivc3zzrshd8t15ikua5"
    uri = "https://magento.softwaretestingboard.com/rest/default/V1/customers"

    # building up a simple post request
    # ??? cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', f"Create customer api returned value for first_name" \
                                              f"but it should be empty. "
