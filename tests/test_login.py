from pages import login_page
from pages.login_page import Login
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestLogin(BaseTest):

    def valid_credentials(self):
        login_page = Login(self.driver)
        login_page.set_username(TestData.Username)
        login_page.set_username(TestData.Password)
        login_page.click_checkbox()
        login_page.click_signin()
        actual_title = login_page.get_title()
        assert actual_title == "Dashboard| IHM & Ship Recycling Services"

