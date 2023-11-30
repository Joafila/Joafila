from selenium.webdriver.common.by import By


class ManageUserClass:
    def __init__(self, driver):
        self.driver = driver

    manage_client_search_bar_id = "//input[@id='searchQueryInput']"
    clear_all_btn_id = "(//button[@type='button'][normalize-space()='Clear All'])[2]"
    add_client_id = "//button[normalize-space()='Add Client']"
    no_records_message = "//div[@class='ag-center-cols-viewport']"
    manage_user_role_permission_id = "//div[@class='row mt-row']//button[@type='button'][normalize-space()='Manage Users Roles & Permissions']"
    valid_user_search_result_id = "(//div[@role='gridcell'][normalize-space()='Tim'])[1]"

    manage_client_back_button_id = "//img[@class='back-btn-responsive manage-client-back-button']"

    def clickSearchBar(self, user_name):
        # self.driver.find_element(By.XPATH, self.manage_client_search_bar_id).click()
        self.driver.find_element(By.XPATH, self.manage_client_search_bar_id).send_keys(user_name)

    def clickClearButton(self):
        self.driver.find_element(By.XPATH, self.clear_all_btn_id).click()

    def noRecordsMessage(self):
        return self.driver.find_element(By.XPATH, self.no_records_message).text

    def clickManageUserRolesPermissionBtn(self):
        self.driver.find_element(By.XPATH, self.manage_user_role_permission_id).click()

    def displayValidResult(self):
        return self.driver.find_element(By.XPATH,self.valid_user_search_result_id).is_displayed()

    def clickAddClient(self):
        self.driver.find_element(By.XPATH, self.add_client_id).click()

    def clickBackIcon(self):
        self.driver.find_element(By.XPATH, self.manage_client_back_button_id).click()
