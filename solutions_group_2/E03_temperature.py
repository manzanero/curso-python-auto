from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get("https://www.eltiempo.es/madrid.html")
    texto_temperatura = driver.find_element(By.CSS_SELECTOR, ".c-tib-text")
    temperatura = int(texto_temperatura.text[:-1])
    assert 50 < temperatura < 100

except Exception:
    driver.save_screenshot("temp/screenshot.png")
    raise

finally:
    driver.quit()
