import time
from selenium import webdriver
import pytest
from pages.AddInternalUser import AddInternalUser
from pages.Login import LoginPageClass


@pytest.mark.usefixtures("set_up_tear_down")
class TestAddUser:
    driver = None

    def test_add_internal_user(self):
        login_page = LoginPageClass(self.driver)
        dashboard_page = login_page.login_to_site("ctiadmindev", "Admin@12345")
        dashboard_page.dashboardQuickAccess()
        manage_user_page = dashboard_page.clickManageUserTab()
        manage_user_page.manageUserPageTitle()
        manage_user_page.clickAddInternalUserBtn()
        add_int_user = AddInternalUser(self.driver)
        add_int_user.addUserFillingMandatoryFields("James", "98921001241", "j@mailinator.com", "James_")
        user_success_message = "Details updated successfully."
        assert add_int_user.displaySuccessMessage().__contains__(user_success_message)



