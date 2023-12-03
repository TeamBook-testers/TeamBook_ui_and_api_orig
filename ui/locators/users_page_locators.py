
from selenium.webdriver.common.by import By

class UsersPageLocators:

    # поменять селектор он ПЛОХОЙ
    CREATE_USER_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]')
    FIRST_NAME = (By.ID, 'userFirstName')
    LAST_NAME = (By.ID, 'userLastName')
    TEAMS_DROPDOWN = (By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/p[2]/div/div")
    #селекторы для пользовательских списков и для системных отличаются!!!
    TEAMS_DROPDOWN_LIST = (By.CSS_SELECTOR, '.tb-react-select-multi__option')
    # TEAM_LIST1 = (By.XPATH, "//div[text()='team1'] | //div[text()='Test org Team']")
    EMAIL = (By.ID, 'userEmail')
    ROLES_DROPDOWN = (By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/p[2]/div/div")
    # ROLES2 = (By.CSS_SELECTOR, '.tb-react-select__single-value')
    # ROLES3 = (By.XPATH, "//div[text()='Regular'] | //div[text()='Contractor'] | //div[text()='Self-Planner'] | //div[text()='Planner'] | //div[text()='Admin']" )
    ROLES_DROPDOWN_LIST = (By.CSS_SELECTOR, '.tb-react-select__option')
    ROLES5 = (By.XPATH, "(//div[@class='tb-react-select__option'])[0]")

    TAGS_DROPDOWN = (By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div[1]/div/div/div")
    TAGS_DROPDOWN_LIST = (By.CSS_SELECTOR, '.tb-react-select-multi__option')


    ANALITICS_DROPDOWN = (By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/p[2]/div/div")
    # ANALITICS_TEXT = (By.XPATH, "//div[text()='Billable'] | //div[text()='Non-billable']")
    ANALITICS_DROPDOWN_LIST = (By.CSS_SELECTOR, '.tb-react-select__option')

    TIMEZONE_DROPDOWN = (By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/p[2]/div/div")
    TIMEZONE_DROPDOWN_LIST = (By.CSS_SELECTOR, '.tb-react-select__option')

    CHECKBOX_START_DATE = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[5]/div[1]/div[1]/img')
    CHECKBOX_END_DATE = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[5]/div[1]/div[2]/img[1]')
    ENTER_START_DATE = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[5]/div[1]/div[1]/div/div/input')
    TODAY_DATE = (By.CLASS_NAME, 'MuiPickersDay-daySelected')
    ENTER_END_DATE = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div[2]/div[5]/div[1]/div[2]/div/div/input')



    PHONE_NUMBER = (By.ID, 'userPhoneNumber')
    ADD_USER_BUTTON = (By.ID, 'createUser')
    # лучше заменить п на звездочку
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'was created')]")
    SUCCESS_MESSAGE2 = (By.CSS_SELECTOR, ".mobile_hidden")
