from vehiculo import *
from bd import conn, cars

class Concesionaria:

    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Auto):
            cars.execute(
                "INSERT INTO vehiculo (marca, modelo, precio, tipo, puertas) VALUES (?, ?, ?, ?, ?)",
                (vehiculo.marca, vehiculo.modelo, vehiculo.precio, "Auto", vehiculo.puertas)
            )
        elif isinstance(vehiculo, Moto):
            cars.execute(
                "INSERT INTO vehiculo (marca, modelo, precio, tipo, cilindrada) VALUES (?, ?, ?, ?, ?)",
                (vehiculo.marca, vehiculo.modelo, vehiculo.precio, "Moto", vehiculo.cilind)
            )
        conn.commit()


    def mostrar_vehiculos(self):
        cars.execute("SELECT * FROM vehiculo")
        filas = cars.fetchall()
        for v in filas:
            print(v)

    def total_impuestos(self):
        total = 0
        cars.execute("SELECT * FROM vehiculo")
        filas = cars.fetchall()
        for v in filas:
            id, marca, modelo, precio, tipo, puertas, cilindrada = v
            if tipo == "Auto":
                vehiculo = Auto(marca, modelo, precio, puertas)
            elif tipo == "Moto":
                vehiculo = Moto(marca, modelo, precio, cilindrada)
            total += vehiculo.impuesto()
        return total
    
    def limpiarBD(self):
        cars.execute("DELETE FROM vehiculo")
        conn.commit()