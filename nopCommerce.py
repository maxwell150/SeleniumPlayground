"""
This script access the given url and searches for the product
'samsung' adds to card and make the order end to end

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
url = "https://demo.nopcommerce.com/"
wait = WebDriverWait(driver, 10)
driver.get(url)
driver.maximize_window()

time.sleep(5)
#access the search the search bar 
search_bar = driver.find_element(By.ID, "small-searchterms")
search_bar.clear()

#enter the product name
search_bar.send_keys("Samsung")

submit_query = driver.find_element(By.CLASS_NAME, "search-box-button" ).click()

add_to_cart = driver.find_element(By.CLASS_NAME, "product-box-add-to-cart-button").click()

shopping_cart_page = driver.find_element(By.CLASS_NAME, "ico-cart").click()

tos_check = driver.find_element(By.ID, "termsofservice").click()

checkout = driver.find_element(By.ID, "checkout").click()

chceckout_as_guest =driver.find_element(By.CLASS_NAME, "checkout-as-guest-button").click()

time.sleep(7)
#enter shipping information
fname = driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Jon")
lname = driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys('Doe')
email = driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("lajon422@gmail.com")
country = driver.find_element(By.ID, "BillingNewAddress_CountryId").click()
country_spec = driver.find_element(By.XPATH, "//option[@value='57']").click()
city = driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Nairobi")
address1 = driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Nairobi CBD")
zip = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("00200-00518")
phone_number = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("254700000000")

submit_ship_details = driver.find_element(By.CLASS_NAME, "new-address-next-step-button").click()

time.sleep(3)

ship_method_check = driver.find_element(By.ID, "shippingoption_0").click()

ship_method_button = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button").click()

time.sleep(4)

payment_method_check = driver.find_element(By.ID, "paymentmethod_0").click() #pay by cheque or money order

payment_method_button = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button").click()

time.sleep(3)

payment_info_button = driver.find_element(By.CLASS_NAME, "payment-info-next-step-button").click()

time.sleep(3)

confirm_order = driver.find_element(By.CLASS_NAME, "confirm-order-next-step-button").click()

time.sleep(3)

driver.close()