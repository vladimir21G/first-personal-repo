import pytest

@pytest.mark.smoke
class TestCheckout(object):

        def test_checkout_as_guest(self):
                print("checkout as guest")
                print("Class: aaaaaa")

        def test_checkout_with_existing_user(self):
                print("Checkout with existing user")
                print("Class: aaaaaaa")
