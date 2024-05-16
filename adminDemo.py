from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import email_nopcommerce, password_nopcommerce
import time

class CaptureTitle(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.url = "https://admin-demo.nopcommerce.com/"
    
    def test_login(self):
        driver = self.driver
        with open('test.txt', 'a') as file:
            try:
                #launch browser
                driver.get(self.url)
                self.assertIn("store", driver.title)
                #get title
                title = driver.title
                file.write(f'TITLE:         {title}\n')

                #get email field
                email = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
                #clear existing data
                email.clear()
                #send data
                email.send_keys(email_nopcommerce)
                file.write(f'Email: check\n')

                #get password field
                password = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
                #clear placeholder
                password.clear()
                #send value
                password.send_keys(password_nopcommerce)
                file.write(f'Password: check\n')

                #chechbox
                checkbox = self.wait.until(EC.visibility_of_element_located((By.ID, 'RememberMe'))).click()
                file.write(f'CHECKBOX:  check\n')

                #find button
                button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
                file.write(f'SUBMIT: check\n')

                self.wait.until(EC.title_contains("Dashboard / nopCommerce administration"))

            except Exception as err:
                file.write(f"-----------------ERROR-----------\n{err}")

    def tearDown(self):
        try:
            self.driver.close()
        except Exception as err:
            print(f'Error while closing the browser: {err}')

if __name__ == '__main__':
    unittest.main()



