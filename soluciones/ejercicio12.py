"""
entrar en esta página https://the-internet.herokuapp.com/context_menu y
hacer click derecho en el área discontinua con js
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium import webdriver

URL = 'https://the-internet.herokuapp.com/context_menu'


driver = webdriver.Chrome()
try:
    driver.get(URL)

    driver.execute_script('''
    var element = document.getElementById('hot-spot');
    var e = element.ownerDocument.createEvent('MouseEvents');

    e.initMouseEvent('contextmenu', true, true,
    element.ownerDocument.defaultView, 1, 0, 0, 0, 0, false, false, false, false,2, null);
    element.dispatchEvent(e);
    ''')

    # hot_spot = driver.find_element(By.ID, 'hot-spot')
    # action = ActionChains(driver)
    # action.context_click(hot_spot)
    # action.perform()

    Alert(driver).accept()
    driver.save_screenshot('1.png')
finally:
    time.sleep(3)
    driver.quit()
