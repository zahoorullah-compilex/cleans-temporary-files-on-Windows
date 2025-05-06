from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# chrome  = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
time.sleep(5)

first_name = driver.find_element(By.ID,"input-firstname")
first_name.send_keys("zahoor")
last_name = driver.find_element(By.ID,"input-lastname")
last_name.send_keys("ahmed")
# random_email = str(random.randint(0,99999) + "@gmail.com")
random_email = f"zahoor{random.randint(0,99999)}@gmail.com"

email = driver.find_element(By.ID,"input-email")
email.send_keys(random_email)
telephone = driver.find_element(By.ID, "input-telephone")
telephone.send_keys("+351999888777")
password = driver.find_element(By.ID, "input-password")
password.send_keys("123456")
password_confirm = driver.find_element(By.ID, "input-confirm")
password_confirm.send_keys("123456")

# News newsletter
newsletter = driver.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")   
newsletter.click()
terms = driver.find_element(By.XPATH, value="//label[@for='input-agree']")
terms.click()
continue_button = driver.find_element(By.XPATH, value="//input[@value='Continue']")
continue_button.click()
time.sleep(5)

# assert
assert driver.title == "Your Account Has Been Created!"
time.sleep(5)
driver.quit()