'''файл с фикстурами'''
import os
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

from ui.data_ui import ChromeDriverPaths, LoginPageData
from ui.locators.login_page_locators import LoginPageLocators
from ui.pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

import chromedriver_autoinstaller

load_dotenv()




'''Для использования фикстуры необходимо персонализировать Service()'''
@pytest.fixture()
def browser():
    #use here your own path to ChromeDriver! (located in ui.data_ui > ChromeDriverPaths)
    chrome_driver_path = ChromeDriverPaths.CHROME_DRIVER_PATH_J
    # chrome_driver_path = ChromeDriverPaths.CHROME_DRIVER_PATH_V
    service = Service(chrome_driver_path)
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def browser():
    chromedriver_autoinstaller.install()
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_email()
    page.enter_password()
    page.click_login_button()
    with allure.step('after successful login, the planning page is open.'):
        allure.attach(browser.get_screenshot_as_png(), name='main_page', attachment_type=AttachmentType.PNG)
    user_menu = wait.until(EC.visibility_of_element_located(LoginPageLocators.USER_MENU))
    assert user_menu, 'user_menu is not found within 10 seconds'
