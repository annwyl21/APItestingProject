import pytest

# Fixture
@pytest.fixture(scope='module') # add scope for before all, can be accessed like a regular parameter, can send variables, lists etc
def my_setup():
    print("")
    print(">>>>>>>>>> SETUP")

@pytest.mark.smoke 
def test_login_page_valid_user(my_setup): # before each fixture must be passed as a parameter
    print("")
    print("Logging with valid user")
    print('+'*50)

@pytest.mark.regression
def test_login_page_wrong_password():
    print("")
    print("wrong password")
    print('-'*50)