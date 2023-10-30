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
        
    