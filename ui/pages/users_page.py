

from selenium.webdriver.common.by import By

from ui.data_ui import UsersPageData
from ui.locators.users_page_locators import UsersPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


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

    def select_team(self):
        teams_dropdown = self.browser.find_element(*UsersPageLocators.TEAMS)
        teams_dropdown.click()
        option = self.browser.find_element(*UsersPageLocators.ONE_TEAM)
        option.click()

    def add_user(self):
        add_user_button = self.browser.find_element(*UsersPageLocators.ADD_USER_BUTTON)
        add_user_button.click()





