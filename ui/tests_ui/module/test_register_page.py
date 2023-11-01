from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


import allure
from allure_commons.types import AttachmentType



from ui.data_ui import RegisterPageData
from ui.data_ui import PlannerPageData
from ui.pages.register_page import RegisterPage
from ui.locators.register_page_locators import RegisterPageLocators





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
    page.enter_business_email(RegisterPageData.REGISTER_BUSINESS_EMAIL_VALID)
    page.enter_org_name(RegisterPageData.REGISTER_ORGANIZATION_NAME_VALID)
    page.enter_password(RegisterPageData.REGISTER_PASSWORD_VALID)
    page.click_create_org_btn()
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.REGISTER_SKIP_BTN))
    page.skip_org_detail_form()

    with allure.step('the result of the successful registration'):
        allure.attach(browser.get_screenshot_as_png(), name='register_result', attachment_type=AttachmentType.PNG)

    wait.until(EC.url_to_be(PlannerPageData.PLANNER_PAGE_URL))
    fact_result_url = browser.current_url
    exp_result_url = PlannerPageData.PLANNER_PAGE_URL
    assert exp_result_url in fact_result_url




    
















