#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with your preferred browser

try:
    # Navigate to your webpage
    driver.get("https://trends.google.com/trending?geo=US")
    time.sleep(2)
    
    # Wait for dropdown to be clickable
    element = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-action='csv']"))  # Replace with your locator
        #EC.element_to_be_clickable((By.CSS_SELECTOR, "[arial-label='Export']"))  # Replace with your locator
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div'))  # Replace with your locator
    )
    element.click()
    
    newelement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div/ul/li[1]'))
    )

    newelement.click()
    
    input("Press Enter to exit")
    
finally:
    # Close the browser window
    driver.quit()
