num_str = input("Ingrese un numero para ver su tabla de multiplicar: ")
num = int(num_str)

for i in range (1,11):
    numero = num*i
    print(f"{num} x {i} = {numero}")