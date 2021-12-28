import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")


    def marcar_checks(check1, check2):
        if check1:
            try:
                not_checked1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:not([checked]):nth-child(1)")
                not_checked1.click()
            except NoSuchElementException:
                pass
        else:
            try:
                checked1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox][checked]:nth-child(1)")
                checked1.click()
            except NoSuchElementException:
                pass

        if check2:
            try:
                not_checked2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:not([checked]):nth-child(3)")
                not_checked2.click()
            except NoSuchElementException:
                pass
        else:
            try:
                checked2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox][checked]:nth-child(3)")
                checked2.click()
            except NoSuchElementException:
                pass

    marcar_checks(True, True)
    time.sleep(3)
    marcar_checks(False, False)
    time.sleep(3)
    marcar_checks(True, False)
    time.sleep(3)
    marcar_checks(False, True)
    time.sleep(3)
finally:
    driver.quit()

