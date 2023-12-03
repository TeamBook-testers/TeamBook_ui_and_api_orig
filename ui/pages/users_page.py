import time
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
    def fill_email_field(self):
        lastname_field = self.browser.find_element(*UsersPageLocators.EMAIL)
        lastname_field.send_keys(UsersPageData.EMAIL)

    def select_team(self):
        teams_dropdown = self.browser.find_element(*UsersPageLocators.TEAMS_DROPDOWN)
        teams_dropdown.click()
        teams_dropdown_list = self.browser.find_elements(*UsersPageLocators.TEAMS_DROPDOWN_LIST)
        teams_dropdown_list[0].click()

        # teams_dropdown_list = self.browser.find_elements(*UsersPageLocators.TEAM_LIST1)
        # print(teams_dropdown_list)
        # for i in teams_dropdown_list:
        #     print(i.get_attribute('outerHTML'))
        #
        # for role_element in teams_dropdown_list:
        #     parent_element = role_element.find_element(By.XPATH, '..')
        #     print(parent_element.get_attribute('outerHTML'))


    def select_role(self):

        roles_dropdown = self.browser.find_element(*UsersPageLocators.ROLES_DROPDOWN)
        roles_dropdown.click()
        roles_dropdown_list = self.browser.find_elements(*UsersPageLocators.ROLES_DROPDOWN_LIST)
        roles_dropdown_list[0].click()

        # time.sleep(2)
        # roles_dropdown_list = self.browser.find_elements(*UsersPageLocators.ROLES3)
        # print(roles_dropdown_list)
        # for i in roles_dropdown_list:
        #     print(i.get_attribute('outerHTML'))
        # for role_element in roles_dropdown_list:
        #     parent_element = role_element.find_element(By.XPATH, '..')
        #     print(parent_element.get_attribute('outerHTML'))

    def select_analitics(self):
        analitics_dropdown = self.browser.find_element(*UsersPageLocators.ANALITICS_DROPDOWN)
        analitics_dropdown.click()
        analitics_dropdown_list = self.browser.find_elements(*UsersPageLocators.ANALITICS_DROPDOWN_LIST)
        analitics_dropdown_list[0].click()


        # for i in analitics_dropdown_list:
        #     print(i.get_attribute('outerHTML'))
        # for anal_element in analitics_dropdown_list:
        #     parent_element = anal_element.find_element(By.XPATH, '..')
        #     print(parent_element.get_attribute('outerHTML'))


    def select_tag(self):
        tag_dropdown = self.browser.find_element(*UsersPageLocators.TAGS_DROPDOWN)
        tag_dropdown.click()
        tag_dropdown_list = self.browser.find_elements(*UsersPageLocators.TAGS_DROPDOWN_LIST)
        if tag_dropdown_list:
            tag_dropdown_list[0].click()

    def select_time_zone(self):
        timezone_dropdown = self.browser.find_element(*UsersPageLocators.TIMEZONE_DROPDOWN)
        timezone_dropdown.click()
        timezone_dropdown_list = self.browser.find_elements(*UsersPageLocators.TIMEZONE_DROPDOWN_LIST)
        timezone_dropdown_list[0].click()

    def select_start_date(self):
        checkbox_start_date = self.browser.find_element(*UsersPageLocators.CHECKBOX_START_DATE)
        checkbox_start_date.click()
        enter_start_date = self.browser.find_element(*UsersPageLocators.ENTER_START_DATE )
        enter_start_date.click()
        selected_day = self.browser.find_element(*UsersPageLocators.TODAY_DATE)
        selected_day.click()

    def select_end_date(self):
        checkbox_end_date = self.browser.find_element(*UsersPageLocators.CHECKBOX_END_DATE )
        checkbox_end_date.click()
        enter_end_date = self.browser.find_element(*UsersPageLocators.ENTER_END_DATE)
        enter_end_date.click()
        time.sleep(1)
        selected_day = self.browser.find_element(*UsersPageLocators.TODAY_DATE)
        selected_day.click()

    def fill_phone_number_field(self):
        lastname_field = self.browser.find_element(*UsersPageLocators.PHONE_NUMBER)
        lastname_field.send_keys(UsersPageData.PHONE_NUMBER)

    def save_user_button_click(self):
        save_user_button = self.browser.find_element(*UsersPageLocators.ADD_USER_BUTTON)
        save_user_button.click()

    # def succ(self):
    #     succ = self.browser.find_element(*UsersPageLocators.SUCCESS_MESSAGE)
    #     print(succ)
    #     print(succ.text)
    #     print(succ.get_attribute('outerHTML'))
    #     parent_element = succ.find_element(By.XPATH, '..')
    #     parent_parent_element = parent_element.find_element(By.XPATH, '..')
    #     print(parent_parent_element.get_attribute('outerHTML'))












