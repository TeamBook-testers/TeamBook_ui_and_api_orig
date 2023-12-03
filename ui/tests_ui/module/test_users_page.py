import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.data_ui import UsersPageData
from ui.locators.users_page_locators import UsersPageLocators
from ui.pages.users_page import UsersPage




# def test_create_user_with_required_fields_only(browser, login):
#
#     link = UsersPageData.USERS_PAGE_URL
#     page = UsersPage(browser, link)
#     wait = WebDriverWait(browser, 10)
#     page.open()
#     page.create_user_button()
#     page.fill_name_field()
#     page.fill_lastname_field()
#     page.select_team()
#     page.save_user_button_click()
#     notification = wait.until(EC.visibility_of_element_located(UsersPageLocators.SUCCESS_MESSAGE))
#     assert notification

def test_create_user_with_full_valid_general_info(browser, login):

    link = UsersPageData.USERS_PAGE_URL
    page = UsersPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.create_user_button()
    time.sleep(1)
    page.fill_name_field()
    page.fill_lastname_field()
    page.fill_email_field()
    page.select_role()
    page.select_analitics()
    page.select_team()
    page.select_tag()
    page.select_time_zone()
    page.select_start_date()
    page.select_end_date()
    page.fill_phone_number_field()
    page.save_user_button_click()
    notification = wait.until(EC.visibility_of_element_located(UsersPageLocators.SUCCESS_MESSAGE))
    assert notification


