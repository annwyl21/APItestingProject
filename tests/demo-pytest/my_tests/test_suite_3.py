import pytest

# Fixture
@pytest.fixture(scope='module') # add scope for before all, can be accessed like a regular parameter, can send variables, lists etc
def my_setup():
    print("")
    print("SetUp runs before all tests in the module")

@pytest.mark.smoke 
def test_before_all_smoke(my_setup): # before each fixture must be passed as a parameter
    print("")
    print("1. Uses before all fixture")
    print('+'*50)

@pytest.mark.regression
def test_before_all_regression():
    print("")
    print("2. Uses before all fixture")
    print('-'*50)
    