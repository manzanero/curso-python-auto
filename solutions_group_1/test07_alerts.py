import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button1 = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(1) > button')
    button1.click()
    driver.switch_to.alert.accept()

    button2 = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > button')
    button2.click()
    driver.switch_to.alert.accept()

    button2 = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > button')
    button2.click()
    driver.switch_to.alert.dismiss()

    button3 = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > button')
    button3.click()
    driver.switch_to.alert.send_keys('ewfqwedgerbqerg')
    driver.switch_to.alert.accept()

    time.sleep(3)

finally:
    driver.quit()
