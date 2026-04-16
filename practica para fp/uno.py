nums = [0,0,0]
suma = 0

for i in range(len(nums)):
    numero = input("ingrese el numero " + str(i+1) +":")
    nums[i] = int(numero)

for n in nums:
    suma += n
print("Suma: ",suma)

prom = suma/3

print("Promedio: ", prom)