from selenium.webdriver.common.by import By


class LoginPageClass:

    def __init__( self, driver ):
        self.driver = driver

    username = 'username'
    password = 'id_password'
    terms_and_conditions_checkbox = 'check1'
    sign_in_button = "//button[normalize-space()='Sign In']"
    error_message_id = "toast-bar-error"
    forgot_password = 'Forgot Password?'

    def enterUsername( self, username ):
        self.driver.find_element(By.ID, self.username).send_keys(username)

    def enterPassword( self, password ):
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def tapTermsAndConditions( self ):
        self.driver.find_element(By.ID, self.terms_and_conditions_checkbox).click()

    def clickSignIn( self ):
        self.driver.find_element(By.XPATH, self.sign_in_button).click()

    def errorMessage( self ):
        return self.driver.find_element(By.ID, self.error_message_id).text
        # message = self.driver.find_element(By.ID, self.error_message_id)
        # message_text = message.text
        # assert message_text == self.incorrect_credential_text

    def clickForgotPassword( self ):
        self.driver.find_element(By.LINK_TEXT, self.forgot_password).click()
