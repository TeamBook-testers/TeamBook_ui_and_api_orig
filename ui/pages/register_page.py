from .base_page import BasePage
from ..locators.register_page_locators import RegisterPageLocators
from ..data_ui import RegisterPageData




class RegisterPage(BasePage):
    
    def enter_first_name(self, name):
        first_name = self.browser.find_element(*RegisterPageLocators.REGISTER_FIRST_NAME)
        first_name.send_keys(name)
        
    def enter_last_name(self, surname):
        last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_LAST_NAME)
        last_name.send_keys(surname)
        
    def enter_business_email(self, business_email):
        last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        last_name.send_keys(business_email)

    def enter_org_name(self, org_name):
        last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_ORGANIZATION_NAME)
        last_name.send_keys(org_name)

    def enter_password(self, password):
        last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        last_name.send_keys(password)

    def click_create_org_btn(self):
        create_org_btn = self.browser.find_element(*RegisterPageLocators.CREATE_COMPANY_FORM_BTN)
        create_org_btn.click()

    def skip_org_detail_form(self):
        skip_btn = self.browser.find_element(*RegisterPageLocators.REGISTER_SKIP_BTN)
        skip_btn.click()