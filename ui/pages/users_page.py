from ui.locators.users_page_locators import UsersPageLocators
from ui.pages.base_page import BasePage


class UsersPage(BasePage):
    def create_user_button(self):
        create_button = self.browser.find_element(*UsersPageLocators.CREATE_USER_BUTTON)
        create_button.click()

    def fill_name_field(self):
        name_field = self.browser.find_element(*UsersPageLocators.FIRST_NAME)
        name_field.send_keys(UsersPageData.FIRST_NAME)

    def fill_lastname_field(self):
        lastname_field = self.browser.find_element(*UsersPageLocators.LAST_NAME)
        lastname_field.send_keys(UsersPageData.LAST_NAME)