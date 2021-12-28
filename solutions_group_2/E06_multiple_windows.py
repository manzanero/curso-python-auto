import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMulti(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_multiple_windows(self):
        self.driver.get("https://the-internet.herokuapp.com/windows")
        link = self.driver.find_element(By.CSS_SELECTOR, "#content > div > a")
        link.click()

        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[1])
        time.sleep(3)

        text_object = self.driver.find_element(By.CSS_SELECTOR, "body > div > h3")
        assert text_object.text == "New Window"
        self.driver.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
