import requests
from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

step_matcher('re')


@given('una URL')
def step_impl(context):
    context.URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'


@when('se hace una request GET con los parametros A = (?P<a>.+) y B = (?P<b>.+)')
def step_impl(context, a, b):
    data = {
       "a": a,
       "b": b,
    }
    context.response = float(requests.get(context.URL, params=data).text)


@when('se hace una request POST con los parametros A = (?P<a>.+) y B = (?P<b>.+)')
def step_impl(context, a, b):
    data = {
       "a": a,
       "b": b,
    }
    context.response = float(requests.post(context.URL, json=data).json()['result'])


@then('el resultado es (?P<c>.+)')
def step_impl(context, c):
    assert context.response == float(c)


