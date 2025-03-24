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

# List of User-Agent strings
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Mobile/15E148 Safari/604.1"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0"
    # Add more User-Agent strings as needed
]

random_user_agent = random.choice(user_agents)

country = 'US'
if len(sys.argv) > 1:
    country = sys.argv[1]

options = Options()
prefs = { 'download.prompt_for_download': False,
        "download.default_directory" : f'{os.path.dirname(os.path.abspath(__file__))}/Data/{country}' }
options.add_experimental_option("prefs", prefs)
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
#options.add_argument("window-size=1920,1080")
options.add_argument(f"--user-agent={random_user_agent}")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)  

try:
    # Navigate to your webpage
    driver.get(f"https://trends.google.com/trending?geo={country}")
    time.sleep(1)
    
    # Wait for dropdown to be clickable
    element = WebDriverWait(driver, 100).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, "[arial-label='Export']"))  # Replace with your locator
        # XPATH for the Export button
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div'))
    )
    element.click()
    
    time.sleep(1)

    newelement = WebDriverWait(driver, 10).until(
                                                    # XPATH for the Download CSV dropdown item
        EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[5]/div[1]/c-wiz/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/div/div/ul/li[1]'))
    )

    time.sleep(1)

    newelement.click()
    
    time.sleep(1)
    
finally:
    # Close the browser window
    driver.quit()
