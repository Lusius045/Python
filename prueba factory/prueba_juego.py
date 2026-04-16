class Personaje:
    def atacar(self):
        raise NotImplementedError()


class Dragon(Personaje):
    def __init__(self):
        self.hp = 300
        self.daño_base = 50

    def atacar(self):
        print("🔥 El dragón lanza fuego. Daño:", self.daño_base)


class Elfo(Personaje):
    def __init__(self):
        self.hp = 120
        self.daño_base = 25

    def atacar(self):
        print("🏹 El elfo dispara una flecha. Daño:", self.daño_base)


class Guerrero(Personaje):
    def __init__(self):
        self.hp = 200
        self.daño_base = 35

    def atacar(self):
        print("🗡️ El guerrero ataca con espada. Daño:", self.daño_base)


class CreadorPersonaje:
    def crear(self):
        raise NotImplementedError()


