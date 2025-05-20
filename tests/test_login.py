import pytest, os
from utils.json_utils import read_json_file
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(BASE_DIR, "test_data", "login_users.json")
user_data = read_json_file(json_path)

@pytest.fixture(scope="function", autouse=True )
def before_each_after_each(page: Page):
    print("before the test runs")
    page.goto("https://www.saucedemo.com/")
    yield
    print(("after the test runs"))

def test_successful_login(page: Page):
    valid_user = user_data["valid_user"]
    login_page = LoginPage(page)
    login_page.login(valid_user["username"], valid_user["password"])
    inventory_page = InventoryPage(page)
    expect(inventory_page.inventory_container).to_be_visible()

def test_unsuccessful_login(page: Page):
    locked_user = user_data["locked_user"]
    login_page = LoginPage(page)
    login_page.login(locked_user["username"], locked_user["password"])
    expect(login_page.warning_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")


