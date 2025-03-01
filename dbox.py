#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#from datetime import datetime
import time
import os

options = Options()
prefs = { 'download.prompt_for_download': False,
        "download.default_directory" : f'{os.path.dirname(os.path.abspath(__file__))}/Data' }
options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)  

try:
    # Navigate to your webpage
    driver.get("https://trends.google.com/trending?geo=US")
    time.sleep(2)
    
    # Wait for dropdown to be clickable
    element = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, "[arial-label='Export']"))  # Replace with your locator
        # XPATH for the Export button
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div'))  # Replace with your locator
    )
    element.click()
    
    newelement = WebDriverWait(driver, 10).until(
                                                    # XPATH for the Download CSV dropdown item
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div/ul/li[1]'))
    )

    newelement.click()
    
    #input("Press Enter to exit")
    time.sleep(2)
    
finally:
    # Close the browser window
    driver.quit()
