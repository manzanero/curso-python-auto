import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

use_step_matcher("re")


@given(u'estoy en el portal de Renfe')
def step_impl(context):
    context.driver.get("https://www.renfe.es/")

    time.sleep(5)

    cookies = context.driver.find_element(By.ID, 'onetrust-accept-btn-handler')

    while not cookies.is_displayed():
        time.sleep(1)

    cookies.click()


@when(u'selecciono origen Madrid')
def step_impl(context):
    origin = context.driver.find_element(By.ID, 'origin')

    actions = ActionChains(context.driver)

    actions.move_to_element(origin)
    actions.click(origin)
    actions.send_keys('Madrid')
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.RETURN)

    actions.perform()


@when(u'selecciono destino Barcelona')
def step_impl(context):
    destination = context.driver.find_element(By.ID, 'destination')

    actions = ActionChains(context.driver)
    actions.move_to_element(destination).click(destination).send_keys('Barcelona')
    actions.send_keys(Keys.DOWN).send_keys(Keys.RETURN).perform()

    buy = context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    buy.click()

    time.sleep(5)


@then(u'llego a la lista de billetes')
def step_impl(context):
    billetes = context.driver.find_elements(By.CSS_SELECTOR, '[class="booking-list-element-price"]')

    if not billetes:
        raise AssertionError('No se ha cargado la lista de billetes')


@when(u'selecciono un billete')
def step_impl(context):
    billetes = context.driver.find_elements(By.CSS_SELECTOR, '[class="booking-list-element-price"]')

    for billete in billetes:
        if billete.is_displayed():
            billete.click()
            break

    continuar = context.driver.find_element(By.ID, 'buttonBannerContinuar')
    continuar.click()


@then(u'el inicio de sesión es requerido')
def step_impl(context):
    time.sleep(5)
