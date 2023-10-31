
from selenium.webdriver.common.by import By

class UsersPageLocators:

    # поменять селектор он ПЛОХОЙ
    CREATE_USER_BUTTON = (By.XPATH, '(//button)[3]')

    FIRST_NAME = (By.ID, 'userFirstName')
    LAST_NAME = (By.ID, 'userLastName')