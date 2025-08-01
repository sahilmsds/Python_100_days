from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # Wait for the search box to be clickable
wait = WebDriverWait(driver, 10)
# search = wait.until(EC.element_to_be_clickable((By.NAME, "search")))

# search.send_keys("Python", Keys.ENTER)

# Challange
URL = "https://secure-retreat-92358.herokuapp.com/"
driver.get(URL)
first_name = wait.until(EC.element_to_be_clickable((By.NAME, "fName")))
first_name.send_keys("Vishwa")

last_name = wait.until(EC.element_to_be_clickable((By.NAME, "lName")))
last_name.send_keys("Karma")

email_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
email_field.send_keys("abc@yuva.in")
submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")))
submit_button.click()