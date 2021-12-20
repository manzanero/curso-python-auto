from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/tables")

filas = driver.find_elements(By.CSS_SELECTOR, "#table1 > tbody > tr")

max_due = 0
max_name = ""

for fila in filas:
    info_lista = fila.text.split()
    name = info_lista[0]

    due = float(info_lista[3].lstrip('$'))

    if due > max_due:
        max_due = due
        max_name = name

print(max_name)

driver.quit()
