from abc import ABC, abstractmethod

# -----------------------------
# 1) PRODUCTO (Interfaz)
# -----------------------------
class Animal(ABC):             # Clase abstracta: todos los animales deben hacer este sonido
    @abstractmethod
    def hacer_sonido(self):
        pass

# -----------------------------
# 2) PRODUCTOS CONCRETOS
# -----------------------------
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"
    
class Pez(Animal):
    def hacer_sonido(self):
        return "Glu glu"

# -----------------------------
# 3) CREATOR (declara el factory method)
# -----------------------------
class CreadorDeAnimales(ABC):
    @abstractmethod
    def crear_animal(self) -> Animal:   # El factory method
        pass

    # Método que usa al animal sin saber cuál es
    def escuchar_sonido(self):
        animal = self.crear_animal()    # llama al factory method
        return animal.hacer_sonido()    # usa el objeto creado

# -----------------------------
# 4) CREATOR CONCRETOS (crean animales específicos)
# -----------------------------
class CreadorDePerros(CreadorDeAnimales):
    def crear_animal(self) -> Animal:
        return Perro()                  # Decide crear un Perro

class CreadorDeGatos(CreadorDeAnimales):
    def crear_animal(self) -> Animal:
        return Gato()                   # Decide crear un Gato

class CreadordePez(CreadorDeAnimales):
    def crear_animal(self) -> Animal:
        return Pez()  

# -----------------------------
# 5) CÓDIGO CLIENTE
# -----------------------------
def cliente(creador: CreadorDeAnimales):
    print("El animal hace:", creador.escuchar_sonido())

# Ejecución
print("---- Usando CreadorDePerros ----")
cliente(CreadorDePerros())

print("\n---- Usando CreadorDeGatos ----")
cliente(CreadorDeGatos())

cliente(CreadordePez())