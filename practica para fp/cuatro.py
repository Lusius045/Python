lista = [1, 2, 2, 3, 4]
nueva_lista = []

for elemento in lista:
    if not nueva_lista or elemento != nueva_lista[-1]:
        nueva_lista.append(elemento)

print(nueva_lista)