from selenium.webdriver.common.by import By



class RegisterPageLocators:
    REGISTER_FIRST_NAME = (By.ID, 'register-first-name')
    REGISTER_LAST_NAME = (By.ID, 'register-last-name')
    REGISTER_EMAIL = (By.ID, 'register-email')
    REGISTER_ORGANIZATION_NAME = (By.ID, 'register-company-name')
    REGISTER_PASSWORD = (By.ID, 'password-field')
    CREATE_COMPANY_FORM_BTN = (By.ID, 'create_org_btn')
    