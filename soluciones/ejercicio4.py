"""
marcar los checks de esta url https://the-internet.herokuapp.com/checkboxes
con el resultado de hacer una petición GET a esta otra url: https://mtp.alejmans.dev/maas/proxy/test/checkbox .

true => debe estar marcado, false => debe estar desmarcado
"""
import time

import requests
from selenium import webdriver

from pageobjects.checkbox_page import CheckboxPage

URL1 = "https://the-internet.herokuapp.com/checkboxes"
URL2 = "https://mtp.alejmans.dev/maas/proxy/test/checkbox"

response = requests.get(URL2)

valor_checkbox_1 = response.json()["checkbox 1"]
valor_checkbox_2 = response.json()["checkbox 2"]

print(valor_checkbox_1)
print(valor_checkbox_2)

driver = webdriver.Chrome()
try:
    driver.get(URL1)
    page = CheckboxPage(driver)

    esta_marcado_checkbox_1 = page.checkbox_1().get_property("checked")
    esta_marcado_checkbox_2 = page.checkbox_2().get_property("checked")

    if valor_checkbox_1 and not esta_marcado_checkbox_1:
        page.checkbox_1().click()
    if valor_checkbox_2 and not esta_marcado_checkbox_2:
        page.checkbox_2().click()
    if not valor_checkbox_1 and esta_marcado_checkbox_1:
        page.checkbox_1().click()
    if not valor_checkbox_2 and esta_marcado_checkbox_2:
        page.checkbox_2().click()
finally:
    time.sleep(3)
    driver.quit()
