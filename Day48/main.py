from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org/")
event_times= driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events_dict = {}

for time, name in zip(event_times, event_names):
    
    print(time.text)
    events_dict[time.text] = name.text
print(events_dict)
driver.quit()
