class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.inventory_container = page.locator(".inventory_container")

