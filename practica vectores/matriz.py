matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Recorrer todo
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"({i},{j}) = {matriz[i][j]}")