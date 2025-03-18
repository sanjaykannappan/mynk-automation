import unittest
from selenium import webdriver
from page_objects.login import LoginPage
from page_objects.products import ProductPage
from page_objects.carts import CartPage
from page_objects.checkout import CheckoutPage
from page_objects.checkout_overview import CheckoutOverview
from page_objects.checkout_complete import CheckoutComplete
from selenium.webdriver.chrome.service import Service
from faker import Faker
import time

class AddToCartCheckoutTest1(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver
        service = Service(executable_path='./driver/chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/") 
        self.fake = Faker()

    def tearDown(self):
        self.driver.quit()
    
    
    def test_add_to_cart_and_checkout(self):
        
        #step 1 : login to the website "saucedemo.com"

        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(2)

        #step 2 : choose the product and add to cart
        product_page = ProductPage(self.driver, "add-to-cart-sauce-labs-bolt-t-shirt")
        product_page.add_to_cart() 
        product_page.click_cart_icon()

        # Step 3: Proceed to the checkout page
        cart_page = CartPage(self.driver)
        cart_page.proceed_to_checkout() 

        # Step 4: Fill in checkout form
        checkout_page = CheckoutPage(self.driver)

        fake_firstname = self.fake.name()
        fake_lastname = self.fake.name()
        fake_postalcode = self.fake.postalcode()
        
        checkout_page.checkout_form(fake_firstname,fake_lastname,fake_postalcode)
       
        #step 5: checkout-overview page
        checkout_overview = CheckoutOverview(self.driver)
        checkout_overview.proceed_to_finish()
        time.sleep(3)


        #step 6: final confirmation page
        checkout_complete = CheckoutComplete(self.driver)
        success_message = checkout_complete.get_success_message()

        # compare the expected and actual assert value 
        self.assertIn("Thank you for your order!", success_message)

if __name__ == "__main__":
    unittest.main()
