import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_js_alert(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        alert_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(1) > button")
        alert_button.click()

        alert = self.driver.switch_to.alert
        alert.accept()

        result = self.driver.find_element(By.ID, "result")
        result_text = result.text

        assert result_text == "You successfully clicked an alert"

    def test_js_confirm_accept(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        confirm_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")
        confirm_button.click()

        alert = self.driver.switch_to.alert
        alert.accept()

        result = self.driver.find_element(By.ID, "result")
        result_text = result.text

        assert result_text == "You clicked: Ok"

    def test_js_confirm_cancel(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        confirm_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(2) > button")
        confirm_button.click()

        alert = self.driver.switch_to.alert
        alert.dismiss()

        result = self.driver.find_element(By.ID, "result")
        result_text = result.text

        assert result_text == "You clicked: Cancel"

    def test_js_prompt(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        prompt_button = self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(3) > button")
        prompt_button.click()

        alert = self.driver.switch_to.alert
        a = "asdf"
        alert.send_keys(a)
        alert.accept()

        time.sleep(2)
        result = self.driver.find_element(By.ID, "result")
        result_text = result.text

        assert result_text == "You entered: " + a
        assert a in result_text

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
