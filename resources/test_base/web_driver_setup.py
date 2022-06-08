# Setup and teardown


import unittest
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3


class WebDriverSetup(unittest.TestCase):
    # pass
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        print("Set up initiated")

    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.delete_all_cookies()
            self.driver.close()
            self.driver.quit()