import pytest
from config_reader import ConfigReader
from playwright.sync_api import Page
from main_page import MainPage
from search_page import SearchPage

@pytest.mark.parametrize('test', ConfigReader().test_data())

def test_check_site(page: Page,test):
    config = ConfigReader()
    # all_tests = config.test_data() Важно оставить для меня
    page.goto(config.main_url())
    main_page = MainPage(page)
    main_page.find(test["name"])

    find_page = SearchPage(page)
    find_page.apply_filter(test["filter"])
    prices = find_page.get_prices(test["n"])
    # print(config.data["test_data"]) вижу все тестовые данные тоже важно оставить для меня


    if test["filter"]=="Price: low to high":
        assert prices == sorted(prices), f"Цены отсортированы не правильно Получил: {prices}"
    else:
        assert prices == sorted(prices,reverse=True), f"Цены отсортированы не правильно Получил: {prices}"


    print()
    print("Цены отсортированы в соответствии с выбранным фильтром")



