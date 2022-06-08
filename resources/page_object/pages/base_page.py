import sys

sys.path.append(sys.path[0] + "/resources/page_object")
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from resources.page_object.locators import Locators


class BasePage(object):

    def __init__(self, driver):
        driver = self.driver

    def get_title(self):
        return self.driver.title

    def get_err_msg(self):
        # print(self.driver.find_element(By.XPATH, Locators.login_error).text)
        return self.driver.find_element(By.XPATH, Locators.error).text

    def errormsg_is_present(self):
        # print(self.driver.find_element(By.XPATH, Locators.error).is_displayed())

        return len(self.driver.find_elements(By.XPATH, Locators.error)) > 0
