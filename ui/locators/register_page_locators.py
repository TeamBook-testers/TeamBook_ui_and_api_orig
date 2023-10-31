from selenium.webdriver.common.by import By



class RegisterPageLocators:
    REGISTER_FIRST_NAME = (By.ID, 'register-first-name')
    REGISTER_LAST_NAME = (By.ID, 'register-last-name')
    REGISTER_EMAIL = (By.ID, 'register-email')
    REGISTER_ORGANIZATION_NAME = (By.ID, 'register-company-name')
    REGISTER_PASSWORD = (By.ID, 'password-field')
    CREATE_COMPANY_FORM_BTN = (By.ID, 'create_org_btn')

    REGISTER_SKIP_BTN = (By.XPATH, "//p[contains(text(), 'Skip')]")
    REGISTER_NEXT_BTN = (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/button')