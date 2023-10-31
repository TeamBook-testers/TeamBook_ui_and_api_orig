from ui.pages.base_page import BasePage


class GeneralInfo(BasePage):
    def click_edit(self):
        edit = self.browser.find_element(*GeneralInfo.EDIT)
        edit.click()

    # def upload_photo(self):
    # def first_name(self):
    # def last_name(self):
    # def phone_number(self):
    # def your_time_zone(self):
    # def save_button(self):


        """Check list General Info
        1. Click "Edit"
        2. Upload photo
        git config --global user.email "lialottarank@gmail.com"
        git config --global user.name "LiaLottar"
        3. Field: First Name (def, locator)
        4. Field: Last Name (def, locator)
        5. Field: Phone number (def, locator)
        6. Field: Your Time Zone (drop-down list!, def, locators)
        7. Button "Save"
        For 3-5 test data
        
        For "Shedule" - only check box
        """

