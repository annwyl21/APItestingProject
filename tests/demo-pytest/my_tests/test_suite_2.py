import pytest

pytestmark= [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke 
class TestCheckout(object):
    def test_class_smoke(self):
        print("Test Class with a smoke test")
    
    def test_checkout_again(self):
        print("Test Class - 2nd smoke test")