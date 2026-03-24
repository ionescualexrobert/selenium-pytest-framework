import pytest
import json
from pages.login_page import LoginPage


def load_test_data():
    with open("data/login_data.json") as f:
        return json.load(f)


test_data = load_test_data()


@pytest.mark.regression
@pytest.mark.parametrize(
    "data",
    test_data,
    ids=[item["id"] for item in test_data]
)
def test_login_negative(driver, data):

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(data["username"], data["password"])

    message = login_page.get_message_text()

    assert data["expected"] in message