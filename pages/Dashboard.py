from selenium.webdriver.common.by import By


class DashboardPageClass:
    def __init__(self, driver):
        self.driver = driver

    dashboard_field = 'dashboard-fieldset'
    dashboard_access = "//legend[@class=dashboard-legend]"
    dashboard_manage_user_tab = "(//div[@class='quick-link-box'])[5]"

    def dashboardQuickAccess(self):
        self.driver.find_element(By.CLASS_NAME, self.dashboard_field).is_displayed()

    def clickManageUserTab(self):
        self.driver.find_element(By.XPATH, self.dashboard_manage_user_tab).click()
