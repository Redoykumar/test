from selenium import webdriver
from selenium.webdriver.chrome.options import Options

_driver = None

def create_driver(headless=True):
    global _driver
    options = Options()
    if headless:
        # options.add_argument("--headless")
        options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    _driver = webdriver.Chrome(options=options)
    return _driver

def quit_driver():
    global _driver
    if _driver:
        _driver.quit()
        _driver = None
