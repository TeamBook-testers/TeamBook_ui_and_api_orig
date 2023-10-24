'''файл с фикстурами'''
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service





'''Для использования фикстуры необходимо персонализировать Service()'''
@pytest.fixture(autouse=True)
def browser():
    service = Service(r"/usr/local/bin/chromedriver")
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()