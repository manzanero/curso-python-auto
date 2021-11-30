from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/tables")

    rows1 = driver.find_elements(By.CSS_SELECTOR, "#table1 > tbody > tr")  # list
    rows2 = driver.find_elements(By.CSS_SELECTOR, "#table2 > tbody > tr")  # list
    rows = rows1 + rows2                                                   # list

    for row in rows:
        row_txt = row.text                    # 'Smith John jsmith@gmail.com $50.00 http://www.jsmith.com edit delete'
        split_row = row_txt.split()           # ['Smith', 'John', 'jsmith@gmail.com', '$50.00', ...]
        dollars_txt = split_row[3]            # '$50.00'
        dollars_int = int(dollars_txt[1:-3])  # 50

        if dollars_int > 50:
            print(f'{split_row[0]} {split_row[1]}')

finally:
    driver.quit()
