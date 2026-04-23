import pytest
from reader.config_reader import ConfigReader
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.search_page import SearchPage
from data.test_data import SEARCH_AND_NUMBER, FILTERS, SortOptions


@pytest.mark.parametrize("name,n", SEARCH_AND_NUMBER)
@pytest.mark.parametrize("filter_type", FILTERS)
def test_check_site(page: Page, filter_type, n, name):
    config = ConfigReader("data/config.json")
    page.goto(config.main_url)
    main_page = MainPage(page)
    main_page.find(name)

    find_page = SearchPage(page)
    find_page.apply_filter(filter_type)
    prices = find_page.get_prices(n)

    if filter_type == SortOptions.LOW_TO_HIGH:
        assert prices == sorted(prices), f"Цены отсортированы не правильно Получил: {prices}"
    else:
        assert prices == sorted(prices, reverse=True), f"Цены отсортированы не правильно Получил: {prices}"

    print()
    print("Цены отсортированы в соответствии с выбранным фильтром")
