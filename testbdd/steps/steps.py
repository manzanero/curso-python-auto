import time

from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given('chrome is up')
def step_impl(context):
    time.sleep(3)


@when('the user gets animeflv page')
def step_impl(context):
    context.driver.get("https://www3.animeflv.net/")


@when('the user clicks one peace link')
def step_impl(context):
    link_serie = context.driver.find_element(By.CSS_SELECTOR, "#mCSB_1_container > ul > li:nth-child(1) > a")
    link_serie.click()


@then('the last episode is the (?P<num>.+)th')
def step_impl(context, num):
    link_episodio = context.driver.find_element(By.CSS_SELECTOR, "#episodeList > li:nth-child(2) > a > p")
    if link_episodio.text != f"Episodio {num}":
        raise AssertionError(f"{link_episodio.text} no es el episodio Episodio {num}")
