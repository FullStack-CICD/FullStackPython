import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):
    """By Locators"""
    EMAIL = (By.ID,"txtUsername")
    PASSWORD = (By.ID,"txtPassword")
    LOGIN_BUTTON =(By.ID,"btnLogin")
    TITLE=(By.ID,"logInPanelHeading")
    SIGNUP_LINK = (By.LINK_TEXT,"Forgot your password?")
    """Constructor of the Page class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        time.sleep(10)
    """Page Actions for Login Page"""
    """This is used to get page title"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    """This is used to check sign up link"""
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """This is used to login to app"""
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        time.sleep(30)
