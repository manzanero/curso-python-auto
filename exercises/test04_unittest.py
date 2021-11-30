import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def test_something(self):
        driver = webdriver.Chrome()
        driver.get("https://www.python.org/")
        self.assertEqual(driver.title, "Welcome to Python.org")
        driver.quit()


if __name__ == '__main__':
    unittest.main()
