import pytest
from selenium.webdriver.support import wait

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
        dashboard_page = login_page.clickSignIn()
        dashboard_page.dashboardQuickAccess()
        dashboard_page.clickBellIcon()
        dashboard_page.clickNotificationCrossIcon()

    def test_if_tabs_are_clickable(self):
        login_page = LoginPageClass(self.driver)
        login_page.enterUsername('ctiadmindev')
        login_page.enterPassword('Admin@12345')
        login_page.tapTermsAndConditions()
        dashboard_page = login_page.clickSignIn()
        dashboard_page.dashboardQuickAccess()
        dashboard_page.clickManageClientShipTab()

