from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.XPATH, "//input[@type='submit' and @id='login-button']")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
