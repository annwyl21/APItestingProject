import pytest
# import to use markers and fixtures, otherwise pytest will just look for test_ naming conventions

pytestmark = pytest.mark.fe

# decorators can be stacked to mark for multiple test suites
@pytest.mark.smoke 
def test_smoke():
    print("Smoke Test")
    print('+'*50)

@pytest.mark.regression
def test_decorators():
    print("Regression Test")
    print('-'*50)

