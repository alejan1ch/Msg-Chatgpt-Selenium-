from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Login():
    def __init__(self, driver):
        # Navigate to LinkedIn login page
        driver.get("https://www.linkedin.com/login")
        sleep(1)

        # Enter login credentials
        self.email = driver.find_element(By.ID, "username")
        self.password = driver.find_element(By.ID, "password")
        self.email.send_keys(os.getenv('EMAIL'))
        self.password.send_keys(os.getenv('PASSWORD'))
        self.password.submit()
        sleep(1)