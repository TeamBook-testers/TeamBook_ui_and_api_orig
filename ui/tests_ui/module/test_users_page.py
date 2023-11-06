import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.data_ui import UsersPageData
from ui.locators.users_page_locators import UsersPageLocators
from ui.pages.users_page import UsersPage




def test_create_user(browser, login):

    link = UsersPageData.USERS_PAGE_URL
    page = UsersPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.create_user_button()
    page.fill_name_field()
    page.fill_lastname_field()
    page.select_team()
    page.add_user()
    notification = wait.until(EC.visibility_of_element_located(UsersPageLocators.SUCCESS_MESSAGE))
    assert notification




