from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = driver.find_element(By.CSS_SELECTOR, "#content > div > button")

    for i in range(20):
        add_button.click()

    for i in range(20):
        driver.find_element(By.CSS_SELECTOR, "#elements > button:nth-child(1)").click()

    # delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")
    # while len(delete_buttons) > 0:
    #     delete_buttons[0].click()
    #
    #     delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")

finally:
    driver.quit()
