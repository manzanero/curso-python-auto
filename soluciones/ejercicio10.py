"""
entrar en esta página https://the-internet.herokuapp.com/windows y clickar en el enlace
después cerrar la nueva ventana y luego la ventana inicial
"""
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

URL = 'https://the-internet.herokuapp.com/windows'


driver = webdriver.Chrome()
try:
    driver.get(URL)
    link = driver.find_element(By.CSS_SELECTOR, '#content > div > a')
    link.click()

    parent = driver.window_handles[0]
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    driver.close()

    driver.quit()


finally:
    time.sleep(3)
    driver.quit()
