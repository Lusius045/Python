class Cuenta:
    def __init__(self, nombre, saldo):
        self.titular = nombre
        self.saldo = saldo

    def __str__(self):
        return f"Titular: {self.titular} - Saldo: {self.saldo}"

    def depositarMonto(self, num):
        try:
            self.saldo = self.saldo + num
        except Exception as e:
            print(e)

    def retirarMonto(self, num):
        try:
            if num > 0 and (self.saldo - num) >= 0:
                self.saldo = self.saldo - num
            else:
                print("no puede retirar saldo negativo")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    persona = Cuenta("Pepe", 100)

    print(persona)