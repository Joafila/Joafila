from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.dashboard_page import Dashboard


class Login(BasePage):
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    checkbox_field = (By.ID, "check1")
    sign_in_button = (By.XPATH, "//button[@class='btn btn-block'']")
    warning_message = (By.ID, "toast-bar-error")

    def __init__(self, driver):
        super.__init__(driver)

    def set_username(self, username):
        self.set(self.username_field,username)

    def set_password(self, password):
        self.set(self.password_field, password)

    def click_checkbox(self):
        self.click(self.checkbox_field)

    def click_signin(self):
        self.click(self.sign_in_button)
        return Dashboard(self.driver)

    def log_into_application(self, username, password):
        self.set_password(username)
        self.set_password(password)
        self.click_checkbox()
        self.click_signin()

    def get_warning_message(self):
        self.get_text(self.warning_message)