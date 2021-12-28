
import requests

param1 = "1"
param2 = "2"

url = "https://ammtp.pythonanywhere.com/testapp/post_example"
parametros = {
    "param1": param1,
    "param2": param2,
}

data = "123"

response = requests.post(url, params=parametros, data=data)

#print(response.text)

valor1 = response.json()['request']['params']["param1"]
valor2 = response.json()['request']['params']["param2"]
valor3 = response.json()['request']['body']

assert valor1 == param1
assert valor2 == param2
assert valor3 == data
