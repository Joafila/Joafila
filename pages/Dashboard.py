from selenium.webdriver.common.by import By

from pages.ManageUsers import ManageUserClass


class DashboardPageClass:
    def __init__( self, driver ):
        self.driver = driver

    # header elements
    dashboard_bell_icon = 'notificationIconHeader'
    dashboard_close_notification = "//img[@src='images/modal-close.png']"
    dashboard_menu_link = "//a[normalize-space()='Dashboard']"
    action_required_id = 'Action Required'
    action_required_back_icon_id = "//img[@alt='Back']"
    # dashboard quick links are tab elements
    dashboard_field = 'dashboard-fieldset'
    dashboard_access = "//legend[@class=dashboard-legend]"
    dashboard_manage_client_ship_tab = "(//div[@class='quick-link-box'])[1]"
    dashboard_manage_user_tab = "(//div[@class='quick-link-box'])[5]"
    dashboard_reports_tab = "(//div[@class='quick-link-box'])[4]"

    def clickBellIcon(self):
        self.driver.find_element(By.CLASS_NAME, self.dashboard_bell_icon).click()

    def clickNotificationCrossIcon(self):
        self.driver.find_element(By.XPATH, self.dashboard_close_notification).click()

    def clickDashboardMenuLink(self):
        self.driver.find_element(By.XPATH, self.dashboard_menu_link).click()

    def clickActionRequired(self):
        self.driver.find_element(By.LINK_TEXT, self.action_required_id).click()

    def clickActionRequiredBackIcon(self):
        self.driver.find_element(By.XPATH, self.action_required_back_icon_id).click()

    def dashboardQuickAccess(self):
        self.driver.find_element(By.CLASS_NAME, self.dashboard_field).is_displayed()

    # Quick Access or Tabs function start
    def clickManageClientShipTab(self):
        self.driver.find_element(By.XPATH, self.dashboard_manage_client_ship_tab).click()

    def clickManageUserTab(self):
        self.driver.find_element(By.XPATH, self.dashboard_manage_user_tab).click()
        return ManageUserClass(self.driver)

    def clickReportsTab(self):
        self.driver.find_element(By.XPATH, self.dashboard_reports_tab).click()
