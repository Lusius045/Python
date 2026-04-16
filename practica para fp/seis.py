lista = [10, 5, 25, 8, 15, 30, 12]
maximo = lista[0]
indice_maximo = 0

for i in range(1, len(lista)):
    if lista[i] > maximo:
        maximo = lista[i]
        indice_maximo = i

print(f"El valor máximo es: {maximo}")
print(f"El índice del valor máximo es: {indice_maximo}")