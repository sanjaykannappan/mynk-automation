from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver, itemname):
        self.driver = driver
        self.add_to_cart_button = (By.ID, itemname)
        self.select_cart_icon = (By.XPATH, "//a[@data-test='shopping-cart-link']")

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_cart_icon(self):
        self.driver.find_element(*self.select_cart_icon).click()
    