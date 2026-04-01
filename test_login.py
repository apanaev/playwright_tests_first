from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


def test_input_login_and_password(page):

    page.goto("http://144.31.139.115:5000", wait_until="load")
    login_link = page.locator("//a[@data-testid='nav-login']")
    login_link.click()
    page.wait_for_url("**/login")
    page.locator("//input[@id='username']").fill("Ruslan")
    page.locator("//input[@id='password']").fill("qwerty")
    page.locator("//input[@id='password']").press("Enter")

    loading_indicator = page.locator("//span[@data-testid='login-submixt-spinner']")
    expect(loading_indicator).to_be_visible()
    print()
    print("1. Отображается индикатор загрузки")
    expect(loading_indicator).to_be_hidden()
    print("2. Индикатор загрузки стал невидимым")
    locator_error = page.locator("//div[@data-testid='login-error-inline']")
    expect(locator_error).to_be_visible()
    print("3. Появляется сообщение об ошибке 'Invalid login or password.'")