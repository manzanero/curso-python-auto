from selenium import webdriver  # hay que haber ejecutado `pip install selenium` para que funcione la importación
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www3.animeflv.net/")

    link = driver.find_element(By.CSS_SELECTOR, "a[href*='one-piece']")
    link.click()

    episodio = driver.find_element(By.CSS_SELECTOR, "#episodeList > li:nth-child(2) > a > p")
    ultimo_episodio = int(episodio.text.split()[1])

    assert ultimo_episodio == 1003

finally:
    driver.quit()
