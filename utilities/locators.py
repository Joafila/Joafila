from selenium.webdriver.common.by import By


class ResetPasswordField:
    new_password_field = (By.NAME, "newPassword")
    confirm_password_field = (By.NAME, "confirmPassword")
    reset_password_button = (By.XPATH, "//button[@class='btn btn-background-color upload-btn']")
    reset_warning_message = (By.CLASS_NAME, "invalid-message-icon-box")
