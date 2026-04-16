lista = [2,4,6,7,9,10,33,79]
contPar = 0
contImpar = 0

for i in range (len(lista)):
    if lista[i] % 2 == 0:
        contPar += 1
    else:
        contImpar += 1

tupla = (contPar, contImpar)

print(f"Pares: {tupla[0]}")
print(f"Impares: {tupla[1]}")