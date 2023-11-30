from selenium.webdriver.common.by import By


class ForgotPasswordPageClass:
    email = 'userEmailId'
    request_new_password = "button[class='btn btn-background-color upload-btn']"
    proceed_confirmation_yes_btn = "button[class='btn btn-background-color yes-btn ']"
    proceed_confirmation_no_btn = "//button[normalize-space()='No']"
    forgot_password_error_message_id = 'invalid-login-email-message'

    def __init__( self, driver ):
        self.driver = driver

    def enterRegisteredEmail( self, email ):
        self.driver.find_element(By.ID, self.email).send_keys(email)

    def clickRequestNewPassword( self ):
        self.driver.find_element(By.CSS_SELECTOR, self.request_new_password).click()

    def clickConfirmationYes( self ):
        self.driver.find_element(By.CSS_SELECTOR, self.proceed_confirmation_yes_btn).click()

    def clickConfirmationNo( self ):
        self.driver.find_element(By.XPATH, self.proceed_confirmation_no_btn).click()

    def errorToContactAdmin( self ):
        return self.driver.find_element(By.CLASS_NAME, self.forgot_password_error_message_id).text
