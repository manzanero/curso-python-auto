"""
entrar en esta página https://the-internet.herokuapp.com/context_menu y
hacer click derecho en el área discontinua
"""
import time

import velenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver

URL = 'https://the-internet.herokuapp.com/challenging_dom'


driver = webdriver.Chrome()
driver2 = velenium.VisualDriver()
try:
    driver.get(URL)

    element = velenium.VisualElement(driver2, 'captura.png', target=velenium.UP)
    element.click()

    element = velenium.VisualElement(driver2, 'captura.png')
    element.click()

    element = velenium.VisualElement(driver2, 'captura.png', target=velenium.DOWN)
    element.click()

finally:
    time.sleep(3)
    driver.quit()
