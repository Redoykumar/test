def test_sample_login(driver):
    driver.get("http://178.128.114.165:73/admin/login")
    assert "Login" in driver.title
