from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from ui.data_ui import LoginPageData


import allure
from allure_commons.types import AttachmentType

from ui.locators.login_page_locators import LoginPageLocators
from ui.pages.login_page import LoginPage



@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with correct user data')
def test_login_correct(browser):
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

@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with incorrect user data')
def test_login_with_incorrect_password(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_email()
    page.enter_incorrect_password()
    page.click_login_button()
    error_message = wait.until(EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageData.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Error is not displayed"
    assert expected_url == current_url, "URLs do not match"


@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with incorrect user data')
def test_login_with_incorrect_email(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_incorrect_email()
    page.enter_password()
    page.click_login_button()
    error_message = wait.until(EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageData.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Error is not displayed"
    assert expected_url == current_url, "URLs do not match"

@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with invalid user data')
def test_login_with_invalid_email(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_invalid_email()
    page.enter_password()
    page.click_login_button()
    error_message = wait.until(EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageData.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Error is not displayed"
    assert expected_url == current_url, "URLs do not match"

@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with invalid user data')
def test_login_blank_fields(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.click_login_button()
    error_message = wait.until(EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageData.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Error is not displayed"
    assert expected_url == current_url, "URLs do not match"

@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with invalid user data')
def test_login_with_blank_login_field(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_password()
    page.click_login_button()
    error_message = wait.until(EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageData.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Error is not displayed"
    assert expected_url == current_url, "URLs do not match"
@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with invalid user data')
def test_login_with_blank_password_field(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    wait = WebDriverWait(browser, 10)
    page.open()
    page.enter_email()
    page.click_login_button()
    error_message = wait.until(EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
    expected_url = LoginPageData.LOGIN_PAGE_URL
    current_url = browser.current_url
    assert error_message.is_displayed(), "Error is not displayed"
    assert expected_url == current_url, "URLs do not match"






