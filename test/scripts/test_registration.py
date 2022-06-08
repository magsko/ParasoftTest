import sys

sys.path.append(sys.path[0] + "/resources/test_base")
from selenium import webdriver
from time import sleep
from resources.test_base.web_driver_setup import WebDriverSetup
from resources.page_object.pages.user_registration import NewUser
import unittest
import pytest
import selenium
from faker import Faker


# class NewUserRegistration(WebDriverSetup):
class NewUserRegistration(unittest.TestCase):
    registration_url = "https://parabank.parasoft.com/parabank/register.htm"
    user = {'first_name': 'John',
            'last_name': 'Doe',
            'address': '123 Street',
            'city': 'Boston',
            'state': 'MA',
            'zip': '123',
            'phone': '12345',
            'ssn': '123-456-7789',
            'username': 'john',
            'password': '123'
            }
    fake = Faker()
    driver = webdriver.Chrome()
 
    
    @classmethod
    def setUp(cls):
        # cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(cls.registration_url)
        cls.driver.implicitly_wait(5)

    def test_page_is_loaded(self):
        registration_form = NewUser(self.driver)
        assert registration_form.get_title() == 'ParaBank | Register for Free Online Account Access'


    def test_password_mismatch(self):
        registration_form = NewUser(self.driver)
        registration_form.enter_password(self.fake.password())
        registration_form.conf_password(self.fake.password())
        registration_form.register_btn.click()
        assert registration_form.get_pass_err_msg().is_displayed()


    def test_form_input(self):
        self.fill_in_form()
        self.driver.implicitly_wait(5)
        assert self.driver.title == 'ParaBank | Customer Created'

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def fill_in_form(self):
        registration_form = NewUser(self.driver)
        registration_form.first_name.send_keys(self.fake.first_name())
        registration_form.last_name.send_keys(self.user['last_name'])
        registration_form.address.send_keys(self.user['address'])
        registration_form.city.send_keys(self.user['city'])
        registration_form.zip.send_keys(self.user['zip'])
        registration_form.state.send_keys(self.user['state'])
        registration_form.phone.send_keys(self.user['phone'])
        registration_form.ssn.send_keys(self.user['ssn'])
        registration_form.username.send_keys(self.fake.name())
        registration_form.password.send_keys(self.user['password'])
        registration_form.confirm_password.send_keys(self.user['password'])
        registration_form.register_btn.click()


if __name__ == '__main__':
    unittest.main()
