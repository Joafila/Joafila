import pytest

from pages.Login import LoginPageClass
from pages.Dashboard import DashboardPageClass
from pages.ManageUsers import ManageUserClass


@pytest.mark.usefixtures("set_up_tear_down")
class TestManageUsers:
    driver = None

    def test_go_to_manage_users(self):
        login_page = LoginPageClass(self.driver)
        login_page.enterUsername('ctiadmindev')
        login_page.enterPassword('Admin@12345')
        login_page.tapTermsAndConditions()
        login_page.clickSignIn()
        dashboard_page = DashboardPageClass(self.driver)
        dashboard_page.clickManageUserTab()

    def test_search_valid_manage_user( self ):
        login_page = LoginPageClass(self.driver)
        login_page.enterUsername('ctiadmindev')
        login_page.enterPassword('Admin@12345')
        login_page.tapTermsAndConditions()
        login_page.clickSignIn()
        dashboard_page = DashboardPageClass(self.driver)
        dashboard_page.clickManageUserTab()
        manage_user_page = ManageUserClass(self.driver)
        manage_user_page.clickSearchBar('Tim')
        assert manage_user_page.displayValidResult()

    # def test_search_invalid_manage_user(self):
    #     login_page = LoginPageClass(self.driver)
    #     login_page.enterUsername('ctiadmindev')
    #     login_page.enterPassword('Admin@12345')
    #     login_page.tapTermsAndConditions()
    #     login_page.clickSignIn()
    #     dashboard_page = DashboardPageClass(self.driver)
    #     dashboard_page.clickManageUserTab()
    #     manage_user_page = ManageUserClass(self.driver)
    #     manage_user_page.clickSearchBar('Jim')
    #     expected_message = "No Rows To Show"
    #     assert manage_user_page.no_records_message().__eq__(expected_message)






