from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


import allure
from allure_commons.types import AttachmentType


from ui.pages.login_page import LoginPage
from ui.data_ui import RegisterPageData
from .pages.register_page import RegisterPage
from ..locators.register_page_locators import RegisterPageLocators




@allure.feature('register_short_version')
@allure.story('Registering the company and user with valid data. Fill the main form and skip the adding form')
@allure.severity('blocker')
def test_register_valid_short_ver(browser):
    link = RegisterPageData.REGISTER_PAGE_URL
    page = RegisterPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_first_name(RegisterPageData.REGISTER_FIRST_NAME_VALID)
    page.enter_last_name(RegisterPageData.REGISTER_LAST_NAME_VALID)
    
















