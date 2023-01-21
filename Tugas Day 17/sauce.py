import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome(ChromeDriverManager().install())

    def test_Login_Positive(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

    def test_Login_Negative(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"user-name").send_keys("user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)

        response_message = driver.find_element(By.ID,"login_button_container").text
        self.assertEqual(response_message, "Epic sadface: Username and password do not match any user in this service")

    def test_Add_Item_To_Cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID,"shopping_cart_container").click()

    def test_Add_Item_To_Cart_And_Checkout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        time.sleep(10)
        driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
        time.sleep(5)

unittest.main()


