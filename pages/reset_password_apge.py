from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from utilities.locators import ResetPasswordField


class ResetPassword (BasePage):

    def __int__(self, driver):
        self.locate = ResetPasswordField
        super.__init__(driver)

    def reset_password_field(self, password, confirm_password):
        self.set(self.locate.new_password_field, password)
        self.set(self.locate.confirm_password_field, confirm_password)
        self.click(self.locate.reset_password_button)
        return Dashboard()

    def get_confirmation_error_message(self):
        return self.get_text(self.locate.reset_warning_message)
