'''файл с фикстурами'''
import os
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ui.data_ui import ChromeDriverPaths, LoginPageData
from ui.pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()



'''Для использования фикстуры необходимо персонализировать Service()'''
@pytest.fixture(autouse=True)
def browser():

    #use here your own path to ChromeDriver! (located in ui.data_ui > ChromeDriverPaths)
    chrome_driver_path = ChromeDriverPaths.CHROME_DRIVER_PATH_J
    service = Service(chrome_driver_path)
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()

    # login_email.send_keys(os.environ['LOGIN'])
@pytest.fixture()
def login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.enter_email()
    page.enter_password()
    page.button_submit()
    with allure.step('after successful login, the planning page is open.'):
        allure.attach(browser.get_screenshot_as_png(), name='main_page', attachment_type=AttachmentType.PNG)
    try:
        user_menu = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, "openUserMenu"))
        )
    except TimeoutException:
        user_menu = None

    assert user_menu, 'user_menu is not found within 10 seconds'
