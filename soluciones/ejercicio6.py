"""
crear 10 elementos dándole a "add" en esta web
https://the-internet.herokuapp.com/add_remove_elements/
y luego borrarlos dándole a "delete"
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Page(object):

    def __init__(self, driver):
        self.btn_add = lambda: driver.find_element(By.CSS_SELECTOR, "#content > div > button")
        self.lista_btn_delete = lambda: driver.find_elements(By.CSS_SELECTOR, "#elements > button")


driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    page = Page(driver)
    for i in range(10):
        page.btn_add().click()

    for boton in page.lista_btn_delete():
        boton.click()

    driver.execute_script('scroll(0, 1000)')

finally:
    time.sleep(3)
    driver.quit()
