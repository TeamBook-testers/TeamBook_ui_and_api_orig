'''файл с фикстурами'''
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service





'''Для использования фикстуры необходимо персонализировать Service()'''
@pytest.fixture(autouse=True)
def browser():
    chrome_driver_path = os.getenv('CHROME_DRIVER_PATH', '/usr/local/bin/chromedriver')
    service = Service(chrome_driver_path)
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()