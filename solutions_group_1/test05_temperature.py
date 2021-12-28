import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Temperaturas(unittest.TestCase):

    def test_temperatura_en_barcelona_entre_0_y_100_C(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/search?q=tiempo+en+barcelona")
        temp = int(driver.find_element(By.ID, 'wob_tm').text)
        self.assertGreater(temp, 0)
        self.assertLess(temp, 100)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
