from asyncio import wait_for

import playwright.sync_api
from playwright.sync_api import Page, Locator


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.select_filter: Locator = page.locator("//*[@id='sort']")
        self.prices: Locator = page.locator("//*[@data-price]")

    def apply_filter(self, filter_type):
        self.select_filter.select_option(label=filter_type)

    def get_prices(self, n):
        self.page.wait_for_load_state("networkidle")
        result = self.prices.all_inner_texts()
        result = result[0:n]

        integer_prices = []
        for i in result:
            temp = i.split()
            integer_prices.append(int(temp[0]))

        return integer_prices[0:n]
