from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from ui.data_ui import LoginPageData


import allure
from allure_commons.types import AttachmentType

from ui.pages.login_page import LoginPage


@allure.feature('user_login')
@allure.severity('blocker')
@allure.story('Authorization with correct user data')

def test_login_correct(browser):
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