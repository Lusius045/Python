from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 'morado')
rectangulo1= Rectangulo(5,10,'Rosa salmon')
print(cuadrado1)
print(rectangulo1)
print(f'Area cuadrado: {cuadrado1.calcular_area()}')
print(f'Area rectangulo: {rectangulo1.calcular_area()}')