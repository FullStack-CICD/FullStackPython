import time
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage

class HomePage(BasePage):
    """By Locators"""
    DASHBOARD=(By.XPATH,"//a[@id='menu_dashboard_index']/b")
    ASSIGN_LEAVE=(By.CSS_SELECTOR,"td:nth-child(1) img")
    EMP_NAME=(By.ID,"assignleave_txtEmployee_empName")
    """Constructor of the Page class"""
    def __init__(self,driver):
        super().__init__(driver)
        #self.driver.get(TestData.BASE_URL)
        time.sleep(10)
    def get_home_page_title(self,title):
        return self.get_title(title)

    def is_dashboard_visible(self):
        return self.is_visible(self.DASHBOARD)

    def click_dashboard(self):
        return self.do_click(self.DASHBOARD)

    def click_assignleave(self):
        return self.do_click(self.ASSIGN_LEAVE)

    def enter_data(self,empname):
        self.do_send_keys(self.EMP_NAME,empname)
        time.sleep(30)