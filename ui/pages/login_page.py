from .base_page import BasePage
from ..data_ui import LoginPageData
from ..locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageData.LOGIN_CORRECT_EMAIL)

    def enter_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(LoginPageData.LOGIN_CORRECT_PASSWORD)
    def enter_incorrect_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(LoginPageData.LOGIN_INCORRECT_PASSWORD)

    def enter_incorrect_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageData.LOGIN_INCORRECT_EMAIL)
    def enter_invalid_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageData.LOGIN_INVALID_EMAIL)
    def click_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

