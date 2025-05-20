import pytest, os
import hashlib
from utils.json_utils import read_json_file
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(BASE_DIR, "test_data", "login_users.json")
user_data = read_json_file(json_path)

def hash_bytes(byte_data):
    return hashlib.sha256(byte_data).hexdigest()


@pytest.fixture(scope="function", autouse=True )
def before_each_after_each(page: Page):
    print("before the test runs")
    page.goto("https://www.saucedemo.com/")
    yield
    print(("after the test runs"))

def test_product_images_are_unique_by_content(page: Page):
    problem_user = user_data["problem_user"]
    login_page = LoginPage(page)
    login_page.login(problem_user["username"], problem_user["password"])
    inventory_page = InventoryPage(page)
    expect(inventory_page.inventory_img_list).to_have_count(6)
    image_elements = inventory_page.inventory_img_list
    count = image_elements.count()
    image_hashes = []
    for i in range(count):
        src = image_elements.nth(i).get_attribute("src")
        image_bytes = page.evaluate(
            """async (src) => {
                const res = await fetch(src);
                const buffer = await res.arrayBuffer();
                return Array.from(new Uint8Array(buffer));
            }""",
            src
        )
        byte_data = bytes(image_bytes)
        image_hashes.append(hash_bytes(byte_data))

    unique_hashes = set(image_hashes)
    assert len(image_hashes) == len(unique_hashes), \
        f"Duplicate images were found by content: {len(image_hashes) - len(unique_hashes)}"
