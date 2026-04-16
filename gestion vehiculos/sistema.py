from concesionaria import Concesionaria
from vehiculo import Auto, Moto

auto1 = Auto("Ford", "Fiesta", 10000, 4)
moto1 = Moto("Yamaha", "FZ", 5000, 250)
auto2 = Auto("Ferrari", "GTB", 20000, 4)

c = Concesionaria()

c.agregar_vehiculo(auto1)
c.agregar_vehiculo(moto1)
c.agregar_vehiculo(auto2)

c.mostrar_vehiculos()
print("Total impuestos:", c.total_impuestos())
