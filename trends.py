#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random
import time
import sys
import os

# Sleeping for random amounts of time in hopes of appearing more human
time.sleep(random.randrange(2, 120, 1))

options = Options()
prefs = { 'download.prompt_for_download': False,
        "download.default_directory" : f'{os.path.dirname(os.path.abspath(__file__))}/Data' }
options.add_experimental_option("prefs", prefs)
options.add_argument("--headless")
options.add_argument("window-size=1920,1080")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)  

country = 'US'
if len(sys.argv) > 1:
    country = sys.argv[1]

try:
    # Navigate to your webpage
    driver.get(f"https://trends.google.com/trending?geo={country}")
    time.sleep(random.randrange(3, 4, 1))
    
    # Wait for dropdown to be clickable
    element = WebDriverWait(driver, 100).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, "[arial-label='Export']"))  # Replace with your locator
        # XPATH for the Export button
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div'))  # Replace with your locator
    )
    element.click()
    
    time.sleep(random.randrange(1, 3, 1))

    newelement = WebDriverWait(driver, 10).until(
                                                    # XPATH for the Download CSV dropdown item
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div/ul/li[1]'))
    )

    time.sleep(random.randrange(2, 5, 1))

    newelement.click()
    
    time.sleep(random.randrange(4, 6, 1))
    
finally:
    # Close the browser window
    driver.quit()
