from dotenv import load_dotenv
import os

load_dotenv()

class LoginPageData:
    LOGIN_PAGE_URL = os.getenv('LOGIN_PAGE_URL')
    LOGIN_EMAIL = os.getenv('LOGIN_EMAIL')
    LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
    INVALID_PASSWORD = os.getenv('INVALID_PASSWORD')