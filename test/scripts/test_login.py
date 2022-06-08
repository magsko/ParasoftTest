import sys
sys.path.append(sys.path[0] + "/resources/test_base")
from selenium import webdriver
from resources.page_object.pages.login_page import Login
from resources.test_base.web_driver_setup import WebDriverSetup
import unittest
import pytest
from faker import Faker


class TestLogin(unittest.TestCase):
    login_url = 'https://parabank.parasoft.com/parabank/index.htm'
    driver = webdriver.Chrome()
    fake = Faker()
    valid_user = 'admin'
    valid_pass = 'admin'
    wrong_credentials_err = 'The username and password could not be verified.'
    missing_credential_err = 'Please enter a username and password.'
    page_title = 'ParaBank | Accounts Overview'
      
    def teardown_method(self, method):
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.login_url)
        self.login = Login(self.driver)

    def test_valid_credentials(self):
        self.login.log_in(self.valid_user, self.valid_pass)
        assert self.login.get_title() == self.page_title

    def test_login_no_username(self):
        self.login.log_in('',  self.valid_pass)
        assert self.login.errormsg_is_present() and self.login.get_err_msg() == self.missing_credential_err

    def test_login_no_pwd(self):
        self.login.log_in(self.valid_user, '')
        assert self.login.errormsg_is_present() and self.login.get_err_msg() == self.missing_credential_err

    def test_wrong_username(self):
        self.login.log_in(self.fake.email(), self.fake.password())
        assert self.login.errormsg_is_present() and self.login.get_err_msg() == self.wrong_credentials_err

    def test_wrong_password(self):
        self.login.log_in(self.valid_user, self.fake.password())
        assert self.login.errormsg_is_present() and self.login.get_err_msg() == self.wrong_credentials_err



