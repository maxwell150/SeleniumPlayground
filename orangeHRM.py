from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import username_orange, password_orange

class OrangeHRM(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://opensource-demo.orangehrmlive.com/"
        #open url
        self.driver.get(self.url)

    def test_login(self):

        #get username field
        username = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        username.clear()
        username.send_keys(username_orange)
        #get passwerd field
        password = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        password.clear()
        password.send_keys(password_orange)
        #get submit button
        button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
        WebDriverWait(self.driver, 10).until(EC.title_is("OrangeHRM"))
        print("✓ Test Passed")
        
    def tearDown(self):
        try:
            self.driver.close()
        except Exception as err:
            print(f'Error while closing the browser: {err}')

if __name__ == '__main__':
    unittest.main()