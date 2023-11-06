from dotenv import load_dotenv
import os
import uuid
from faker import Faker



load_dotenv()
fake = Faker()

class ChromeDriverPaths:
    CHROME_DRIVER_PATH_J = '/Users/uliabubnova/PycharmProjects/TeamBook_ui_and_api/TeamBook_ui_and_api_orig_jul/chromedriver'
    CHROME_DRIVER_PATH_V = '/usr/local/bin/chromedriver'


class LoginPageData:
    LOGIN_PAGE_URL = 'https://web.teambooktest.com/login'
    LOGIN_CORRECT_EMAIL = os.environ['LOGIN_EMAIL']
    LOGIN_CORRECT_PASSWORD = os.environ['LOGIN_PASSWORD']
    LOGIN_INCORRECT_PASSWORD = fake.password(length=8)
    LOGIN_INCORRECT_EMAIL = fake.email()
    LOGIN_INVALID_EMAIL = fake.word()



class RegisterPageData:
    REGISTER_PAGE_URL = 'https://web.teambooktest.com/register'
    REGISTER_FIRST_NAME_VALID = fake.first_name()
    REGISTER_LAST_NAME_VALID = fake.last_name()
    REGISTER_BUSINESS_EMAIL_VALID = fake.email()
    REGISTER_ORGANIZATION_NAME_VALID = fake.text(max_nb_chars=10)
    REGISTER_PASSWORD_VALID = 'Password1!'




class UsersPageData:
    USERS_PAGE_URL = 'https://web.teambooktest.com/users'
    FIRST_NAME = fake.first_name()
    LAST_NAME = fake.last_name()




class PlannerPageData:
    PLANNER_PAGE_URL = 'https://web.teambooktest.com/planners'