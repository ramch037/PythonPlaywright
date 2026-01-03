class HomePage:
    def __init__(self, page):
        self. page = page

    def click_sites_and_users(self):
        self.page.locator('//span[text()="Sites and Users"]').click()

    def click_users_of_sites_and_users(self):
        self.page.locator('//span[text()="Users"]').click()

