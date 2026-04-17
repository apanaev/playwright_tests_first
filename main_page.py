import playwright.sync_api
from playwright.sync_api import Page, Locator


class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_input: Locator = page.get_by_test_id("search-input")

    def find(self, name):
        self.search_input.fill(name)
        self.search_input.press("Enter")
