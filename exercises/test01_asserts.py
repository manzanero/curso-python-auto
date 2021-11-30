import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import win32api

while True:
    driver = webdriver.Chrome()
    try:
        driver.get("https://www3.animeflv.net/")
        link_serie = driver.find_element(By.CSS_SELECTOR, "#mCSB_1_container > ul > li:nth-child(1) > a")
        link_serie.click()
        link_episodio = driver.find_element(By.CSS_SELECTOR, "#episodeList > li:nth-child(2) > a > p")
        assert link_episodio.text == "Episodio 999"
        win32api.MessageBox(0, 'Nuevo episodio', 'Alerta')
    except AssertionError:
        pass
    finally:
        driver.quit()
        time.sleep(10)

