from playwright.sync_api import expect
from faker import Faker

fake = Faker()
URL = "http://144.31.139.115:5000"

def test_input_login_and_password(page):
    page.goto(URL)
    login_link = page.get_by_test_id("nav-login")
    login_link.click()
    page.locator("//*[@id='username']").fill(fake.user_name())
    page.locator("//*[@id='password']").fill(fake.password())
    page.locator("//*[@id='password']").press("Enter")

    loading_indicator = page.get_by_test_id("login-submixt-spinner")
    expect(loading_indicator).to_be_visible()
    print()
    print("1. Отображается индикатор загрузки")
    expect(loading_indicator).to_be_hidden()
    print("2. Индикатор загрузки стал невидимым")
    locator_error = page.get_by_test_id("login-error-inline")
    expect(locator_error).to_be_visible()
    expect(locator_error).to_have_text("Invalid login or password.")
    print("3. Появляется сообщение об ошибке 'Invalid login or password.'")