import pytest

from pages.Dashboard import DashboardPageClass
from pages.Login import LoginPageClass


@pytest.mark.usefixtures("set_up_tear_down")
class TestDashboardPage:
    driver = None

    def test_if_header_elements_clickable(self):
        login_page = LoginPageClass(self.driver)
        login_page.enterUsername('ctiadmindev')
        login_page.enterPassword('Admin@12345')
        login_page.tapTermsAndConditions()
        login_page.clickSignIn()
        dashboard_page = DashboardPageClass(self.driver)
        dashboard_page.clickBellIcon()
        dashboard_page.clickNotificationCrossIcon()

    def test_if_tabs_are_clickable(self):
        login_page = LoginPageClass(self.driver)
        login_page.enterUsername('ctiadmindev')
        login_page.enterPassword('Admin@12345')
        login_page.tapTermsAndConditions()
        login_page.clickSignIn()
        dashboard_page = DashboardPageClass(self.driver)
        dashboard_page.clickManageClientShipTab()
        dashboard_page.clickDashboardMenuLink()
        dashboard_page.clickReportsTab()
