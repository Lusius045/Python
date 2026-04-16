from abc import ABC, abstractmethod

# ======================================================
# 1) PRODUCTOS ABSTRACTOS
# ======================================================

class Personaje(ABC):
    @abstractmethod
    def atacar(self):
        pass


class Arma(ABC):
    @abstractmethod
    def usar(self):
        pass


# ======================================================
# 2) PRODUCTOS CONCRETOS - ORCOS
# ======================================================

class GuerreroOrco(Personaje):
    def atacar(self):
        return "El guerrero orco ataca con brutalidad."


class HachaOrca(Arma):
    def usar(self):
        return "El hacha orca corta con fuerza salvaje."


# ======================================================
# 3) PRODUCTOS CONCRETOS - ELFOS
# ======================================================

class GuerreroElfo(Personaje):
    def atacar(self):
        return "El guerrero elfo ataca con elegancia y precisión."


class ArcoElfico(Arma):
    def usar(self):
        return "El arco élfico dispara una flecha mágica."


# ======================================================
# 4) FÁBRICA ABSTRACTA
# ======================================================

class FabricaRaza(ABC):

    @abstractmethod
    def crear_personaje(self) -> Personaje:
        """Crea un personaje compatible con la familia."""

    @abstractmethod
    def crear_arma(self) -> Arma:
        """Crea un arma compatible con la familia."""


# ======================================================
# 5) FÁBRICAS CONCRETAS
# ======================================================

class FabricaOrcos(FabricaRaza):

    def crear_personaje(self) -> Personaje:
        return GuerreroOrco()

    def crear_arma(self) -> Arma:
        return HachaOrca()


class FabricaElfos(FabricaRaza):

    def crear_personaje(self) -> Personaje:
        return GuerreroElfo()

    def crear_arma(self) -> Arma:
        return ArcoElfico()


# ======================================================
# 6) CÓDIGO CLIENTE
# ======================================================

def iniciar_juego(fabrica: FabricaRaza):
    """
    El cliente NO conoce las clases concretas.
    Solo sabe que recibe una fábrica compatible.
    """
    personaje = fabrica.crear_personaje()
    arma = fabrica.crear_arma()

    print(personaje.atacar())
    print(arma.usar())


# ======================================================
# 7) USO
# ======================================================

print("=== JUEGO CON ORCOS ===")
fabrica_orcos = FabricaOrcos()
iniciar_juego(fabrica_orcos)

print("\n=== JUEGO CON ELFOS ===")
fabrica_elfos = FabricaElfos()
iniciar_juego(fabrica_elfos)