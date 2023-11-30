import pytest

from pages.Dashboard import DashboardPageClass


@pytest.mark.usefixtures("set_up_tear_down")
class TestDashboardPage:
    driver = None

    def test_if_header_elements_clickable(self):
        dashboard_page = DashboardPageClass(self.driver)
        dashboard_page.clickBellIcon()
        dashboard_page.clickNotificationCrossIcon()

    def test_if_tabs_are_clickable(self):
        dashboard_page = DashboardPageClass(self.driver)
        dashboard_page.clickManageClientShipTab()
        dashboard_page.clickDashboardMenuLink()
        dashboard_page.clickReportsTab()
