from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class MailpitPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://178.128.114.165:7040"

    def load(self):
        self.driver.get(self.base_url)

    def get_latest_otp_for_email(self, email):
        self.load()
        
        wait = WebDriverWait(self.driver, 10)
        
        # Wait for the search input and enter the email address
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']")))
        search_input.clear()
        search_input.send_keys(email)
        
        # Wait for email list to update (assuming class 'email-list-item')
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.email-list-item")))
        
        # Click the first email in the list (latest)
        first_email = self.driver.find_element(By.CSS_SELECTOR, "div.email-list-item")
        first_email.click()
        
        # Wait for email body to load
        email_body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.email-body")))
        
        # Get the email body text
        body_text = email_body.text
        
        # Extract 6-digit OTP code from email text
        otp_match = re.search(r'\b(\d{6})\b', body_text)
        if otp_match:
            return otp_match.group(1)
        else:
            raise Exception("OTP code not found in email body")
