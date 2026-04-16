from abc import ABC, abstractmethod

# Clase abstracta: NO se puede crear un Animal directamente
class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass    # No tiene implementación

# Subclase concreta: esta sí se puede crear
class Perro(Animal):
    def sonido(self):
        return "Guau!"

class Gato(Animal):
    def sonido(self):
        return "Miau!"


# ---------- Uso ----------
# animal = Animal()  # ❌ ERROR: una clase abstracta NO se puede instanciar

perro = Perro()
gato = Gato()

print(perro.sonido())  # "Guau!"
print(gato.sonido())   # "Miau!"