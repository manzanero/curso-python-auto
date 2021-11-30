import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/hovers")
    image3 = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(5) > img')

    actions = ActionChains(driver)
    actions.move_to_element(image3).perform()

    link3 = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(5) > div > a')
    link3.click()

    time.sleep(3)

finally:
    driver.quit()
