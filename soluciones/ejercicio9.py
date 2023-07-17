"""
entrar en esta página https://the-internet.herokuapp.com/hovers y clickar en el enlace
que aparece al poner el ratón encima de uno de los iconos
"""
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

URL = 'https://the-internet.herokuapp.com/hovers'


driver = webdriver.Chrome()
try:
    driver.get(URL)
    action = webdriver.ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(3) > img')
    action.move_to_element(element)
    action.perform()

    link = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(3) > div > a')
    link.click()

finally:
    time.sleep(3)
    driver.quit()
