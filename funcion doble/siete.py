import math

def logaritmeando(num1):
    logaritmeado = math.log(num1,10)
    return logaritmeado


num1 = float(input())

num_log = logaritmeando(num1)

print(num_log)