"""
Escribe, en Python, un programa que muestre en pantalla los números del 0 al 100,
sustituyendo los múltiplos de 3 por la palabra "Fizz" y, a su vez, los múltiplos
de 5 por "Buzz". Cuando, al mismo tiempo, son múltiplos de 3 y 5, utiliza "FizzBuzz"
"""

FIZZ = "Fizz"
BUZZ = "Buzz"

for i in range(100 + 1):
    es_divisible_por_3 = i % 3 == 0
    es_divisible_por_5 = i % 5 == 0

    if es_divisible_por_5 and es_divisible_por_3:
        print(FIZZ + BUZZ)
    elif es_divisible_por_3:
        print(FIZZ)
    elif es_divisible_por_5:
        print(BUZZ)
    else:
        print(i)
