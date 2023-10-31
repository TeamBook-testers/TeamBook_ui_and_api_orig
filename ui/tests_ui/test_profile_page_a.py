import time
import pytest

from ui.pages.profile_page_a import GeneralInfo


def test_general_info(browser, login):
    link = "https://web.teambooktest.com/profile"
    page = GeneralInfo(browser, link)
    page.open()
    page.click_edit()


