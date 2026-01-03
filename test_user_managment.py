import time

from page_header import HeaderBar
from page_home import HomePage
from page_login import LoginPage


def test_search_user(setup_teardown):
    page = setup_teardown
    login_page = LoginPage(page)
    login_page.login()

    header_bar = HeaderBar(page)
    header_bar.click_settings_button()

    home_page = HomePage(page)
    home_page.click_sites_and_users()
    time.sleep(5)
    home_page.click_users_of_sites_and_users()

    time.sleep(5)





