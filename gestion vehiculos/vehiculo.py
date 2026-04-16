class Vehiculo:
    
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.precio}"
    
    def setPrecio(self, nuevoPrecio):
        try:
            if nuevoPrecio < 0:
                raise ValueError("El precio no puede ser negativo")
            self.precio = nuevoPrecio
        except ValueError as e:
            print(e)
            
    @staticmethod
    def es_valido(precio):
        return precio > 0

class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio, puertas):
        super().__init__(marca, modelo, precio)
        self.puertas = puertas

    def __str__(self):
        return f"{self.marca} {self.modelo}, puertas: {self.puertas} - {self.precio}"
    
    def impuesto(self):
        imp = (self.precio/100)*10
        print(f"impuesto del 10%: {imp}")
        return imp

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, cilind):
        super().__init__(marca, modelo, precio)
        self.cilind = cilind

    def __str__(self):
        return f"{self.marca} {self.modelo}, cilindrada: {self.cilind} - {self.precio}"
    
    def impuesto(self):
        imp = (self.precio/100)*5
        print(f"impuesto del 5%: {imp}")
        return imp