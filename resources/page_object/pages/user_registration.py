import sys
sys.path.append(sys.path[0] + "/resources/page_object")
from selenium.webdriver.common.by import By
from resources.page_object.locators import Locators


#New User class
class NewUser(object):

    def load_page(self, driver, url):
        self.driver = driver
        driver.get(url)

    def __init__(self, driver):
        self.driver = driver
        self.first_name = driver.find_element(By.XPATH, Locators.first_name)
        self.last_name = driver.find_element(By.XPATH, Locators.last_name)
        self.address = driver.find_element(By.XPATH, Locators.address)
        self.city = driver.find_element(By.XPATH,Locators.city)
        self.state = driver.find_element(By.XPATH, Locators.state)
        self.zip = driver.find_element(By.XPATH, Locators.zip)
        self.phone = driver.find_element(By.XPATH, Locators.phone)
        self.ssn = driver.find_element(By.XPATH, Locators.ssn)
        self.username = driver.find_element(By.XPATH, Locators.username)
        self.password = driver.find_element(By.XPATH, Locators.password)
        self.confirm_password = driver.find_element(By.XPATH, Locators.confirm_password)
        self.register_btn = driver.find_element(By.XPATH, Locators.register_btn)

    def fill_in_field(self, field, string):
        field.send_keys(string)







