'''файл с фикстурами'''
import os
import time
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

load_dotenv()



'''Для использования фикстуры необходимо персонализировать Service()'''
@pytest.fixture(autouse=True)
def browser():
    # chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
    chrome_driver_path = os.environ['CHROME_DRIVER_PATH_V']
    service = Service(chrome_driver_path)
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()

    # login_email.send_keys(os.environ['LOGIN'])
