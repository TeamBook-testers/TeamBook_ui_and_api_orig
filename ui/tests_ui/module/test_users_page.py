import time

from ui.data_ui import UsersPageData
from ui.pages.users_page import UsersPage


def test_create_user(browser, login):

    link = UsersPageData.USERS_PAGE_URL
    page = UsersPage(browser, link)
    page.open()
    time.sleep(2)

    #поменять селектор потом
    page.create_user_button()