import pytest

from pages.Login import LoginPageClass
from pages.Dashboard import DashboardPageClass


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
