import pytest

from pages.Login import LoginPageClass
from pages.Dashboard import DashboardPageClass
from pages.ManageUsers import ManageUserClass


@pytest.mark.usefixtures("set_up_tear_down")
class TestManageUsers:
    driver = None

    def test_go_to_manage_users(self):
        login_page = LoginPageClass(self.driver)
        dashboard_page = login_page.login_to_site("ctiadmindev", "Admin@123")
        manage_user_page = dashboard_page.clickManageUserTab()
        expected_text = "Manage Users"
        assert manage_user_page.manageUserPageTitle().__eq__(expected_text)

    def test_search_valid_manage_user( self ):
        login_page = LoginPageClass(self.driver)
        dashboard_page = login_page.login_to_site("ctiadmindev", "Admin@123")
        dashboard_page.dashboardQuickAccess()
        manage_user_page = dashboard_page.clickManageUserTab()
        manage_user_page.clickSearchBar('Tim')
        assert manage_user_page.displayValidResult()

    def test_search_invalid_manage_user(self):
        login_page = LoginPageClass(self.driver)
        dashboard_page = login_page.login_to_site("ctiadmindev", "Admin@123")
        manage_user_page = dashboard_page.clickManageUserTab()
        manage_user_page.clickSearchBar('Jim')
        expected_message = "No Rows To Show"
        assert expected_message






