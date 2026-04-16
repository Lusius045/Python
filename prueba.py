class Cuenta:
    def __init__(self, nombre_cliente="Sin nombre", numero_cuenta="Sin número", tipo_interes=0.0, saldo=0.0):
        self.nombre_cliente = nombre_cliente
        self.numero_cuenta = numero_cuenta
        self.tipo_interes = tipo_interes
        self.saldo = saldo

    def __str__(self):
        return f"Nombre: {self.nombre_cliente}, Número de cuenta: {self.numero_cuenta}, Tipo de interes: {self.tipo_interes} Saldo: {self.saldo}"
   
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        else:
            print("Error: La cantidad a ingresar debe ser positiva.")
            return False
   
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                return True
            else:
                print("Error: Saldo insuficiente.")
                return False
        else:
            print("Error: La cantidad a retirar debe ser positiva.")
            return False
    
    def transferencia(self, cuenta_destino, importe):
        if self.retirar(importe):
            cuenta_destino.ingresar(importe)
            print("Transferencia realizada con éxito.")
        else:
            print("Error: No se pudo realizar la transferencia.")


if __name__ == "__main__":
    obj = Cuenta("Pepe", 1, saldo=300)
    cuenta_destino = Cuenta("Julian", 3, 2, 1)

    print(obj)
    
    obj.ingresar(200)
    print(obj)
    obj.retirar(100)
    print(obj)
    obj.transferencia(cuenta_destino, 100)
    print(obj)
    print(cuenta_destino)