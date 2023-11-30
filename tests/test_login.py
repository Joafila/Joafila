import pytest

from pages.Login import LoginPageClass
from pages.Dashboard import DashboardPageClass


@pytest.mark.usefixtures("set_up_tear_down")
class TestLogin:
    driver = None

    def test_valid_credentials(self):
        login_page = LoginPageClass(self.driver)
        login_page.enterUsername('ctiadmindev')
        login_page.enterPassword('Admin@12345')
        login_page.tapTermsAndConditions()
        login_page.clickSignIn()
        dashboard_page = DashboardPageClass(self.driver)
        dashboard_page.dashboardQuickAccess()

    def test_invalid_credentials(self):
        login_page = LoginPageClass(self.driver)
        login_page.enterUsername('ctiadmindev')
        login_page.enterPassword('Admin@123')
        login_page.tapTermsAndConditions()
        login_page.clickSignIn()
        incorrect_credential_text = 'Incorrect username or password'
        assert login_page.errorMessage().__eq__(incorrect_credential_text)
