
from selenium.webdriver.common.by import By

class UsersPageLocators:

    # поменять селектор он ПЛОХОЙ
    CREATE_USER_BUTTON = (By.XPATH, '(//button)[3]')
    FIRST_NAME = (By.ID, 'userFirstName')
    LAST_NAME = (By.ID, 'userLastName')
    TEAMS = (By.CSS_SELECTOR, '.tb-react-select-multi__control')
    ONE_TEAM = (By.XPATH, "//div[text()='team1']")
    ADD_USER_BUTTON = (By.ID, 'createUser')
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'was created')]")