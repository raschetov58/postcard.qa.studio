from selenium import webdriver

def test_smoke():
    driver = webdriver.Chrome()

    driver.get("http://selenium.dev")

    driver.quit()