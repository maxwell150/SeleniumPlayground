from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

def wait_and_click(by, value):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element

order_success = {}

try:
    # Search for product
    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "small-searchterms")))
    search_bar.clear()
    search_bar.send_keys("Laptop")
    search_bar.send_keys(Keys.RETURN)

    # Add to cart and proceed to checkout
    wait_and_click(By.CLASS_NAME, "product-box-add-to-cart-button")
    wait_and_click(By.CLASS_NAME, "ico-cart")
    wait_and_click(By.ID, "termsofservice")
    wait_and_click(By.ID, "checkout")
    wait_and_click(By.CLASS_NAME, "checkout-as-guest-button")

    # Enter shipping information
    driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Jon")
    driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys('Doe')
    driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("lajon422@gmail.com")
    driver.find_element(By.ID, "BillingNewAddress_CountryId").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[@value='57']"))).click()
    driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Nairobi")
    driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Nairobi CBD")
    driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("00200-00518")
    driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("254700000000")
    wait_and_click(By.CLASS_NAME, "new-address-next-step-button")

    # Shipping and payment method
    wait_and_click(By.ID, "shippingoption_0")
    wait_and_click(By.CLASS_NAME, "shipping-method-next-step-button")
    wait_and_click(By.ID, "paymentmethod_0")
    wait_and_click(By.CLASS_NAME, "payment-method-next-step-button")
    wait_and_click(By.CLASS_NAME, "payment-info-next-step-button")
    wait_and_click(By.CLASS_NAME, "confirm-order-next-step-button")

    # Capture order details
    order_number = driver.find_element(By.XPATH, "//div[@class='order-number']").text
    details_link = driver.find_element(By.XPATH, "//div[@class='details-link']//a").get_attribute('href')
    order_success['order_number'] = order_number
    order_success['details_link'] = details_link
    print(order_success)    

except (NoSuchElementException, ElementClickInterceptedException) as err:
    print(f"-----ERROR-----\n{str(err)}\n---------------------")

finally:
    driver.quit()
