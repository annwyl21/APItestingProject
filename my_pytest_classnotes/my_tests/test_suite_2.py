import pytest

pytestmark= [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke 
class TestCheckout(object):
    def test_checkout_as_guest(self):
        print("checkout as guest")
    
    def test_checkout_again(self):
        print("2nd test")