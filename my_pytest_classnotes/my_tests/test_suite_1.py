import pytest
# import to use markers and fixtures, otherwise pytest will just look for test_ naming conventions

pytestmark = pytest.mark.fe

# decorators can be stacked to mark for multiple test suites
@pytest.mark.smoke 
def test_login_page_valid_user():
    print("Logging with valid user")
    print('+'*50)

@pytest.mark.regression
def test_login_page_wrong_password():
    print("wrong password")
    print('-'*50)

