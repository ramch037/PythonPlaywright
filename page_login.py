class LoginPage:

    def __init__(self, page):
        self.page = page


    def login(self):
        self.page.locator("#UserNameTextBox").fill("cssupport")
        self.page.locator("#PasswordTextBox").fill("password")
        self.page.locator("#LoginButton").click()
        return self.page
