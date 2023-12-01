from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddInternalUser:
    def __init__(self, driver):
        self.driver = driver

    employee_name = "Employee Name"
    contact_number = "contactNo"
    email_address = "email"
    address = "//textarea[@name='address']"
    region = "ddlDropdown"
    user_role = "dropdown_userRole"
    designation_id = "designation"
    service_category = "dropdown_serviceCategory"
    select_level = "dropdown_userLevel"
    username = "id_username"
    user_save = "//button[normalize-space()='Save']"
    save_user_success_message = "toast-bar-success"

    def enterEmployeeName(self,emp_name):
        self.driver.find_elemet(By.ID,self.employee_name).send_keys(emp_name)

    def enterContactNum(self, phone_numb):
        self.driver.find_elemet(By.ID,self.contact_number).send_keys(phone_numb)

    def enterUserEmail(self,email):
        self.driver.find_elemet(By.ID,self.email_address).send_keys(email)

    def enterAddress(self,address):
        self.driver.find_elemet(By.XPATH, self.address).send_keys(address)

    def selectRegion(self):
        regiondrpdwn = Select(self.driver.find_elemet(By.ID, self.region))
        regiondrpdwn.select_by_index(3)

    def selectUserRole(self):
        userRoledrpdwn = Select(self.driver.find_elemet(By.NAME, self.user_role))
        userRoledrpdwn.select_by_index(0)

    def enterDesignation(self, des_name):
        self.driver.find_elemet(By.ID, self.designation_id).send_keys(des_name)

    def selectServiceCategory(self):
        service_category_drpdwn = Select(self.driver.find_elemet(By.NAME, self.service_category))
        service_category_drpdwn.select_by_index(1)

    def selectLevel(self):
        level_drpdwn = Select(self.driver.find_elemet(By.NAME, self.select_level))
        level_drpdwn.select_by_index(1)

    def enterUsername(self,new_username):
        self.driver.find_elemet(By.ID, self.username).send_keys(new_username)

    def clickSave(self):
        self.driver.find_elemet(By.XPATH, self.user_save).click()

    def displaySuccessMessage(self):
        return self.driver.find_elemet(By.ID, self.save_user_success_message).text

    def addUserFillingMandatoryFields(self, emp_name, phone_numb, email,des_name,new_username ):
        self.enterEmployeeName(emp_name)
        self.enterContactNum(phone_numb)
        self.enterUserEmail(email)
        self.selectRegion()
        self.selectUserRole()
        self.enterDesignation(des_name)
        self.selectServiceCategory()
        self.selectLevel()
        self.enterUsername(new_username)
        self.clickSave()



