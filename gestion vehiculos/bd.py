import sqlite3

conn = sqlite3.connect("mi_base.db")
cars = conn.cursor()

# Crear tabla si no existe
cars.execute("""
CREATE TABLE IF NOT EXISTS vehiculo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT,
    modelo TEXT,
    precio REAL,
    tipo TEXT,
    puertas INTEGER,
    cilindrada INTEGER
)
""")
conn.commit()

