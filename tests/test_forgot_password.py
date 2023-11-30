import pytest

from pages.ForgotPassword import ForgotPasswordPageClass
from pages.Login import LoginPageClass


@pytest.mark.usefixtures("set_up_tear_down")
class TestForgotPassword:
    driver = None

    def enter_registered_email(self):
        login_page = LoginPageClass(self.driver)
        login_page.clickForgotPassword()
        forgot_password = ForgotPasswordPageClass(self.driver)
        forgot_password.enterRegisteredEmail('testlateredot@gmail.com')
        forgot_password.clickRequestNewPassword()
        forgot_password.clickConfirmationYes()
        expected_error_msg = 'Please contact the eDOT Team to change the Admin password.'
        assert forgot_password.errorToContactAdmin().__eq__(expected_error_msg)
