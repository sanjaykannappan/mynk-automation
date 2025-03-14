from selenium.webdriver.common.by import By

class CheckoutComplete:
    def __init__(self, driver):
        self.driver = driver
        self.success_msg = (By.XPATH, "//h2[@data-test='complete-header']")

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).text
