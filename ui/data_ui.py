from dotenv import load_dotenv
import os
import uuid
from faker import Faker

load_dotenv()
fake = Faker()

class LoginPageData:
    LOGIN_PAGE_URL = os.getenv('LOGIN_PAGE_URL')
    LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
    LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
    INVALID_PASSWORD = os.getenv('INVALID_PASSWORD')



class RegisterPageData:
    REGISTER_PAGE_URL = 'https://web.teambooktest.com/register'
    REGISTER_FIRST_NAME_VALID = fake.first_name()
    REGISTER_LAST_NAME_VALID = fake.last_name()
    REGISTER_BUSINESS_EMAIL_VALID = f'{uuid}@mail.ru'
    REGISTER_ORGANIZATION_NAME_VALID = fake.text(max_nb_chars=10)
    REGISTER_PASSWORD_VALID = 'Password1!'
