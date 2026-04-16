from vehiculo import Auto,Moto

class Concesionaria:
    def __init__(self):
        self.autos = []
    
    def agregarAuto(self, marca, modelo, precio):
        autonuevo = Auto(marca, modelo, precio)
        self.autos.append(autonuevo)
    
    def agregarMoto(self, marca, modelo, precio):
        motoNueva = Moto(marca, modelo, precio)
        self.autos.append(motoNueva)

    def listarVehiculos(self):
        for v in self.autos:
            print(f"Marca: {v.marca} - Modelo: {v.modelo} - Precio: {v.precio}")


if __name__ == "__main__":
    sis = Concesionaria()

    sis.agregarAuto("Toyota","Corolla",15000)
    sis.agregarMoto("Honda","Pinfloro",10000)

    sis.listarVehiculos()