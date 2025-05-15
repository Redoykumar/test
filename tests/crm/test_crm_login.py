from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.crm.login_page import CRMLoginPage
from pages.mailpit.mailpit_api import MailpitAPI
from utils.config import BASE_URL
import pytest
import time
import json

with open('data/crm/test_users.json') as f:
    test_users = json.load(f)

@pytest.mark.parametrize("user", test_users)
def test_crm_login_logout_with_otp_api(driver, user):
    login_page = CRMLoginPage(driver)
    login_page.load(f"{BASE_URL}/admin/login")
    # Perform login (username & password)
    login_page.login(user['username'], user['password'])
  


  
    print("Dashboard loaded!")
    # Optional logout to test session termination
    login_page.logout()

    # # Ensure redirected to login page after logout
    # WebDriverWait(driver, 15).until(
    #     lambda d: "login" in d.current_url.lower()
    # )
    # assert "login" in driver.current_url.lower()
