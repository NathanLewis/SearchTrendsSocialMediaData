#!/usr/bin/env python

from selenium import webdriver
from datetime import datetime

now = datetime.now()
browser = webdriver.Firefox()
browser.get('https://trends.google.com/trending?geo=US')
#browser.save_screenshot('screenie.png')
#driver.execute_script("return document.body.innerHTML")
#browser.execute_script("return document.body.innerHTML")
#print(browser.page_source)
filename = 'trending_' + now.strftime("%Y-%m-%dT%H_%M_%S") + '.html'
with open(filename, 'w') as file:
	file.write(browser.page_source)
