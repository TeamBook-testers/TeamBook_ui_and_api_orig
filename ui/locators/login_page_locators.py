from selenium.webdriver.common.by import By



class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, ":r0:")
    LOGIN_PASSWORD = (By.ID, ":r1:")
    LOGIN_BUTTON = (By.ID, "login_btn")
    USER_MENU = (By.ID, "openUserMenu")