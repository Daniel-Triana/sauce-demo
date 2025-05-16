import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):

    print("before the test runs")

    page.goto("https://www.saucedemo.com/")
    yield

    print(("after the test runs"))



def test_successful_login(page: Page):

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page.locator(".inventory_container")).to_be_visible()


