import sys

sys.path.append(sys.path[0] + "/resources/page_object")
from selenium.webdriver.common.by import By
from resources.page_object.locators import Locators
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())



class Home(object):

    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.XPATH, Locators.username_field)
        self.password_field = driver.find_element(By.XPATH, Locators.password_field)

        # self.logo = driver.find_element(By.XPATH, Locator.logo)
        # self.search_text = driver.find_element(By.XPATH, Locator.search_text)
        # self.submit = driver.find_element(By.XPATH, Locator.submit)

    def getUsernameField(self):
        return self.username_field

    def getPasswrodField(self):
        return self.password_field

    def getSearchText(self):
        return self.search_text

    def getSubmit(self):
        return self.submit

    def getWebPageLogo(self):
        return self.logo
