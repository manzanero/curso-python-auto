import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/windows")
    new_window = driver.find_element(By.CSS_SELECTOR, '#content > div > a')
    new_window.click()

    driver.switch_to.window(driver.window_handles[1])

    text = driver.find_element(By.CSS_SELECTOR, 'body > div > h3')
    assert text.is_displayed()

    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(3)

finally:
    driver.quit()
