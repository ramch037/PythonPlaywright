from playwright.sync_api import expect

from page_login import LoginPage


def test_login_valid_credentials(setup_teardown):
    page = setup_teardown
    login_page = LoginPage(page)
    login_page.login()
    page.wait_for_url("**/dashboard.aspx", timeout=15000)
    expect(page.locator("#ctl00_HorizontalBar_HorizontalBarLbl")).to_be_visible(timeout=15000)
