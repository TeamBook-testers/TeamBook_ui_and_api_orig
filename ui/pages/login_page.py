from .base_page import BasePage
from ..data_ui import LoginPageData
from ..locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageData.LOGIN_EMAIL)

    def enter_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(LoginPageData.LOGIN_PASSWORD)

    def button_submit(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()