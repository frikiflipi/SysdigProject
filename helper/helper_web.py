# ---------------------------------------------------------------------------
# Created By  : Guillermo Navarro
# Created Date: 13/06/2022
# version ='1.0'
# Comment: Class to be able to select different browsers and settings
# ---------------------------------------------------------------------------

from selenium import webdriver
from helper.helper_base import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())