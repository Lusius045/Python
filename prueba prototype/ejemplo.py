class Personaje:
    def __init__(self, nombre, nivel, habilidades):
        self.nombre = nombre
        self.nivel = nivel
        self.habilidades = habilidades  # lista

    def clonar(self):
        # Creamos un nuevo Personaje con los valores actuales
        nuevo_nombre = self.nombre
        nuevo_nivel = self.nivel
        nuevas_habilidades = [h for h in self.habilidades]  # copia manual de la lista

        # Devolvemos un objeto nuevo con esos datos
        return Personaje(nuevo_nombre, nuevo_nivel, nuevas_habilidades)

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel}) - Habilidades: {self.habilidades}"


# --- Uso del Prototype manual ---

prototipo_mago = Personaje(
    nombre="Mago Base",
    nivel=1,
    habilidades=["Hechizo Débil", "Escudo Mágico"]
)

# Clonamos el prototipo
jugador1 = prototipo_mago.clonar()
jugador1.nombre = "Merlín"
jugador1.nivel = 10
jugador1.habilidades.append("Bola de Fuego")

jugador2 = prototipo_mago.clonar()
jugador2.nombre = "Gandalf"
jugador2.nivel = 7

# Mostramos resultados
print(jugador1)
print(jugador2)
print(prototipo_mago)