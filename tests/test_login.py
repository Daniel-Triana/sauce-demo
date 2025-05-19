import pytest
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage

@pytest.fixture(scope="function", autouse=True )
def before_each_after_each(page: Page):
    print("before the test runs")
    page.goto("https://www.saucedemo.com/")
    yield
    print(("after the test runs"))



def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    expect(inventory_page.inventory_container).to_be_visible()


