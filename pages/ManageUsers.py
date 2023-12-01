from selenium.webdriver.common.by import By

from pages.AddInternalUser import AddInternalUser


class ManageUserClass:
    def __init__(self, driver):
        self.driver = driver
    users_page_title = "manage-users-title"
    manage_client_search_bar_id = "//input[@id='searchQueryInput']"
    clear_all_btn_id = "(//button[@type='button'][normalize-space()='Clear All'])[2]"
    no_records_message = ".ag-overlay-no-rows-center"
    manage_user_role_permission_id = "//div[@class='row mt-row']//button[@type='button'][normalize-space()='Manage Users Roles & Permissions']"
    valid_user_search_result_id = "(//div[@role='gridcell'][normalize-space()='Tim'])[1]"
    add_internal_user = "div[class='desktop-class'] div[class='col-12'] button:nth-child(1)"

    def manageUserPageTitle(self):
        return self.driver.find_element(By.CLASS_NAME, self.users_page_title).text

    def clickSearchBar(self, user_name):
        # self.driver.find_element(By.XPATH, self.manage_client_search_bar_id).click()
        self.driver.find_element(By.XPATH, self.manage_client_search_bar_id).send_keys(user_name)

    def clickClearButton(self):
        self.driver.find_element(By.XPATH, self.clear_all_btn_id).click()

    def noRecordsMessage(self):
        return self.driver.find_element(By.XPATH, self.no_records_message).text

    def clickManageUserRolesPermissionBtn(self):
        self.driver.find_element(By.XPATH, self.manage_user_role_permission_id).click()

    def clickAddInternalUserBtn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_internal_user).click()
        # return AddInternalUser(self.driver)

    def displayValidResult(self):
        return self.driver.find_element(By.XPATH, self.valid_user_search_result_id).is_displayed()




