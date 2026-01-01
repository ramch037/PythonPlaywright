import pytest
from playwright.sync_api import Playwright



@pytest.fixture()
def setup_teardown(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://qa.primeroedge.co/login.aspx")
    yield page
    context.close()
