class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def impuesto(self):
        return "El vehículo no tiene impuestos"
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio):
        super().__init__(marca,modelo,precio)
        self.precio = precio * 0.10

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio):
        super().__init__(marca,modelo,precio)
        self.precio = precio * 0.05