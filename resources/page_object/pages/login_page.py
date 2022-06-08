import sys
sys.path.append(sys.path[0] + "/resources/page_object")
from resources.page_object.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from resources.page_object.locators import Locators



class Login(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.XPATH,Locators.login_username)
        self.pass_field = driver.find_element(By.XPATH, Locators.login_password)
        self.btn = driver.find_element(By.XPATH, Locators.login_btn)
        
    def enter_username(self, user):
        self.username_field.send_keys(user)

    def enter_pass(self, pwd):
        self.pass_field.send_keys(pwd)

    def click_login_button(self):
        self.btn.click()

    def log_in(self, user, pwd):
        self.enter_username(user)
        self.enter_pass(pwd)
        self.click_login_button()
    
 
        




        


