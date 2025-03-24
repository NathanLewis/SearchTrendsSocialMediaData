#! venv/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import random
import time
import os

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

def automate_xcom_login():

    random_user_agent = random.choice(user_agents)

    # Set up Chrome driver (adjust path as needed)
    options = Options()
    prefs = { 'download.prompt_for_download': False,
            "download.default_directory" : f'{os.path.dirname(os.path.abspath(__file__))}/Data/x.com' }
    options.add_experimental_option("prefs", prefs)
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    #options.add_argument("--auto-open-devtools-for-tabs")
    #options.add_argument("window-size=1920,1080")
    options.add_argument(f"--user-agent={random_user_agent}")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

    
    try:
        # Navigate to X.com login page
        driver.get("https://x.com/i/flow/login")

        username_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
        
        # Wait for login form elements
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, username_path))
        )
        
        # Enter credentials (replace with actual values)
        username_input.send_keys("")

        #next_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]'

        next_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div'
        next_input = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, next_path))
        )

        input("Press any key to continue")
        next_input.click()

        time.sleep(1)
        html_content = driver.execute_script("return document.documentElement.outerHTML")
        with open('password_page.html', 'w', encoding='utf-8') as f:
            f.write(html_content)

        #password_input = driver.find_element(By.NAME, "password")
        password_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        password_input = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, password_path))
        )
        password_input.send_keys('')
        
        # Take screenshot
        #screenshot_path = "xcom_screenshot.png"
        #driver.save_screenshot(screenshot_path)
        #print(f"Screenshot saved as {screenshot_path}")

        #input("Press any key to exit")
        
    except TimeoutException:
        print("Timed out waiting for page elements")
        input("Press any key to exit")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Clean up
        input("Press any key to exit")
        driver.quit()

if __name__ == "__main__":
    automate_xcom_login()
