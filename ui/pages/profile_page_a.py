from ui.pages.base_page import BasePage


class GeneralInfo(BasePage):
    def click_edit(self):
        edit = self.browser.find_element(*GeneralInfo.EDIT)
        edit.click()


        """   чек-лист по General Info
        1. Click "Edit"
        2. Upload photo
        git config --global user.email "lialottarank@gmail.com"
  git config --global user.name "LiaLottar"
        3. Las




        """

