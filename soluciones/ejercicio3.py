"""
Imprimir por pantalla la temperatura en Madrid y añadir un mensaje indicando en cual de estas franjas está:
franja 1:  < 25ºC
franja 2:  25ºC < x < 30ºC
franja 3:  > 30ºC
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

T_B = 25
T_A = 30
CIUDAD = "Madrid"

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/search?q=temperatura+en+Madrid&rlz=1C1CHBF_esES937ES937&oq=temperatura+en+Madrid&aqs=chrome..69i57j0i512l9.830j0j7&sourceid=chrome&ie=UTF-8")

    texto_temperatura = driver.find_element(By.ID, 'wob_tm').text

    print(texto_temperatura)

    if float(texto_temperatura) < T_B:
        print("temp baja")
    elif T_B < float(texto_temperatura) < T_A:
        print("temp media")
    else:
        print("temp alta")

finally:
    time.sleep(3)
    driver.close()
