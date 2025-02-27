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
    
    # Create Select object
    #select = Select(dropdown_element)
    
    # Select by visible text
    #select.select_by_visible_text("Download CSV")  # Replace with your desired text
    
    input("Press Enter to exit")
    
finally:
    # Close the browser window
    driver.quit()

#<li class="W7g1Rb-rymPhb-ibnC6b W7g1Rb-rymPhb-ibnC6b-OWXEXe-hXIJHe W7g1Rb-rymPhb-ibnC6b-OWXEXe-SfQLQb-Woal0c-RWgCYc O68mGe-OQAXze-OWXEXe-SfQLQb-Woal0c-RWgCYc" jsaction="click:o6ZaF; keydown:RDtNu; keyup:JdS61c; focusin:MeMJlc; focusout:bkTmIf; mousedown:teoBgf; mouseup:NZPHBc; mouseenter:SKyDAe; mouseleave:xq3APb; touchstart:jJiBRc; touchmove:kZeBdd; touchend:VfAz8; change:uOgbud;" tabindex="0" role="menuitem" aria-label="Download CSV" data-action="csv"><span class="RBHQF-ksKsZd" jscontroller="LBaJxb" jsname="m9ZlFb"></span><span class="frX3lc-vlkzWd W7g1Rb-rymPhb-sNKcce"></span><span class="W7g1Rb-rymPhb-KkROqb"><i class="google-material-icons notranslate W7g1Rb-rymPhb-Abojl W7g1Rb-rymPhb-H09UMb-bN97Pc" aria-hidden="true"><span class="google-symbols">csv</span></i></span><span class="W7g1Rb-rymPhb-Gtdoyb"><span class="W7g1Rb-rymPhb-fpDzbe-fmcmS" jsname="K4r5Ff">Download CSV</span></span><span class="W7g1Rb-rymPhb-JMEf7e"></span></li>
