import sys

sys.path.append(sys.path[0] + "/resources/test_base")
from time import sleep

from resources.test_base.web_driver_setup import WebDriverSetup
from resources.page_object.pages.home_page import Home
import resources.page_object.urls
import unittest
import selenium
import pytest
from selenium import webdriver


class ParasoftHomePage(WebDriverSetup):
    homepage_url = "https://parabank.parasoft.com/"

    def test_always_passes(self):
        assert True

    def test_always_fails(self):
        assert False

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        if (cls.driver != None):
            print("Cleanup of test environment")
            cls.driver.close()
            cls.driver.quit()

    def test_home_page(self):
        print("TESTING HOME PAGE")
        driver = self.driver
        self.driver.get(self.homepage_url)
        home_page = Home(driver)
        password = home_page.password_field
        password.click()
        password.send_keys("test")

 

    #
    # #verify we are on the right page TODO update
    #     web_page_title = "Google"
    #     try:
    #         if driver.title == web_page_title:
    #             print("WebPage loaded successfully")
    #             self.assertEqual(driver.title, web_page_title)
    #     except Exception as error:
    #         print(error + "WebPage Failed to load")
    #


if __name__ == '__main__':
    unittest.main()
