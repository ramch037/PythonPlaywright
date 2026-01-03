from playwright.sync_api import Playwright

class HeaderBar:
    def __init__(self, page):
        self.page = page


    def click_settings_button(self):
        self.page.locator('//img[@src="images/system_white.svg"]').click()