import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_HomePage(BaseTest):
    def test_homepageflow(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.homepage = HomePage(self.driver)
        #title = self.homepage.get_title(TestData.LOGIN_PAGE_TITLE)
        #assert title == TestData.LOGIN_PAGE_TITLE
        #self.homepage.is_dashboard_visible()
        #self.homepage.click_dashboard()
        self.homepage.click_assignleave()
        self.homepage.enter_data(TestData.EMPNAME)
