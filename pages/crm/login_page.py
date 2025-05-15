from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.mailpit.mailpit_api import MailpitAPI
class CRMLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        # Wait for the email input to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )

        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")

        email_input.clear()
        email_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        # Click the Login button to submit the form
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Login')]")
        login_button.click()

        # Get OTP via API
        mailpit_api = MailpitAPI()
        otp_code = mailpit_api.get_latest_otp(username)
        print("OTP code:", otp_code)

        # Use the new verify_otp method to enter OTP and submit
        self.verify_otp(otp_code)




    def verify_otp(self, otp_code, timeout=30):
        """
        Wait for OTP input field, enter the OTP code, and submit.
        """
        otp_input = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-input-otp="true"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", otp_input)
        otp_input.click()
        otp_input.clear()
        otp_input.send_keys(otp_code)

    
    
    def logout(self):
        # Optionally dismiss toast or wait for it to disappear
        try:
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Toastify__toast"))
            )
        except:
            pass

        # Click profile avatar
        profile_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "radix-:rh:"))
        )
        profile_button.click()

        # Click logout
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Logout')]"))
        )
        logout_button.click()

        # Verify logout success
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("login")
        )



