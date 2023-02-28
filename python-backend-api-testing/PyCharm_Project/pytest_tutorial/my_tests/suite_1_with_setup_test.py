import pytest

pytestmark = pytest.mark.fe

@pytest.fixture(scope='module')
def my_setup():
    print("")
    print(">>> MY SETUP <<<")

    return {'age': 23, 'name': 'Vladimir'}

@pytest.mark.ll
def test_login_page_valid_user(my_setup):
    print("")
    print("Login with valid user")
    print("Function: aaaaaaa")
    print("Name: {}".format(my_setup.get('name')))


@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: aaaaaaa")
