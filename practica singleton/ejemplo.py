class Logger:
    _instancia = None   # Atributo de clase donde guardamos la única instancia

    def __new__(cls):
        # Si NO existe la instancia, la creo
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            print("📌 Creando instancia única de Logger")
        else:
            print("📌 Usando instancia ya existente de Logger")
        
        # Siempre devuelvo la MISMA instancia
        return cls._instancia

    def log(self, mensaje):
        print(f"[LOG]: {mensaje}")

    def getInstance(cls):
        return cls._instancia

logger1 = Logger()
logger2 = Logger()
logger3 = Logger()

logger1.log("Hola mundo")
logger2.log("Esto también va al mismo logger")

print(logger1 is logger2)  # True
print(logger2 is logger3)  # True