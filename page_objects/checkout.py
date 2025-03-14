from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname_field = (By.ID, "first-name")
        self.lastname_field = (By.ID, "last-name")
        self.postalcode_field = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.firstname_field).send_keys(firstname)
    
    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname_field).send_keys(lastname)

    def enter_postalcode(self, postalcode):
        self.driver.find_element(*self.postalcode_field).send_keys(postalcode)

    def click_continue_btn(self):
        self.driver.find_element(*self.continue_btn).click()

    def checkout_form(self, firstname, lastname, postalcode):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_postalcode(postalcode)
        self.click_continue_btn()

