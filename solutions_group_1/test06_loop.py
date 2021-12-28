from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = driver.find_element(By.CSS_SELECTOR, '#content > div > button')

    for i in range(10):
        add_button.click()

    added_buttons = driver.find_elements(By.CSS_SELECTOR, '[class="added-manually"]')

    while added_buttons:
        added_buttons[-1].click()
        added_buttons = driver.find_elements(By.CSS_SELECTOR, '[class="added-manually"]')

finally:
    driver.quit()
