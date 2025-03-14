import unittest
from selenium import webdriver
from page_objects.login import LoginPage
import time

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")  # login URL
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")  # Valid credentials
        time.sleep(2)  # Add sleep to see the results; 
        # Check whether login was successful
        self.assertTrue(self.driver.current_url == "https://www.saucedemo.com/inventory.html")  # Landing page URL

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid_user", "invalid_password")  # Invalid credentials
        time.sleep(2)
        error_msg = login_page.get_error_message()
        self.assertEqual(error_msg, "Epic sadface: Username and password do not match any user in this service")  # check error message

if __name__ == "__main__":
    unittest.main()
