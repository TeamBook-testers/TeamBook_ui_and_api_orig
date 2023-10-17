from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

'''ожидаемые условия для каждой страницы'''


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def visibility_of_element_located(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def url_to_be(self, url, timeout=5):
        return wait(self.browser, timeout).until(EC.url_to_be(url))

    def url_contains(self, word_example, timeout=5):
        return wait(self.browser, timeout).until(EC.url_contains(word_example))

    def text_to_be_present_in_element(self, locator, expected_text, timeout=5):
        return wait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, expected_text))

    def text_to_be_present_in_element_value(self, locator, expected_text, timeout=5):
        return wait(self.browser, timeout).until(EC.text_to_be_present_in_element_value(locator, expected_text))

    def element_to_be_clickable(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def alert_is_present(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.alert_is_present())