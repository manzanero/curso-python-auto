"""
El ejercicio para mañana miércoles sería el siguiente:

Dada esta url = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

pasar los parámetros "a=1" y "b=2" como parámetros de una petición GET e imprimir el resultado
pasar un diccionario {'a':1,'b'=2} como payload de una petición POST e imprimir el resultado
si el resustado en ambos casos no es 3 elevar una excepción: AssertionError()

"""
import unittest

import requests

URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'

A = 1
B = 2


class TestRequests(unittest.TestCase):

    def test_request_get(self):
        parametros = {
            "a": A,
            "b": B
        }
        response = requests.get(URL, params=parametros)
        self.assertEqual(float(response.text), 3)

    def test_request_post(self):
        data = {
            "a": A,
            "b": B
        }
        response = requests.post(URL, json=data)
        self.assertEqual(float(response.json()["result"]), 3)


if __name__ == '__main__':
    unittest.main()
