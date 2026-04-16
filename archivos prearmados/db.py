import sqlite3

conn = sqlite3.connect("escuela.db")
cur = conn.cursor()

cur.execute("PRAGMA foreign_keys = ON;")

cur.execute("""
CREATE TABLE IF NOT EXISTS profesor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    especialidad TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    profesor_id INTEGER,
    cupo INTEGER,
    FOREIGN KEY (profesor_id) REFERENCES profesor(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS alumno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS inscripcion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alumno_id INTEGER,
    curso_id INTEGER,
    nota INTEGER,
    FOREIGN KEY (alumno_id) REFERENCES alumno(id),
    FOREIGN KEY (curso_id) REFERENCES curso(id)
)
""")

# Inserts para profesor
cur.executemany(
    "INSERT INTO profesor (nombre, especialidad) VALUES (?,?)",
    [
        ("Juan Perez","Programación"),
        ("Ana Lopez","Base de Datos"),
        ("Luis Gomez","Redes"),
        ("Carla Ruiz","Programación")
    ]
)

# Inserts para curso
cur.executemany(
    "INSERT INTO curso (nombre, profesor_id, cupo) VALUES (?,?,?)",
    [
        ("Python Inicial",1,30),
        ("SQL Básico",2,25),
        ("Redes 1",3,20),
        ("Python Avanzado",4,15)
    ]
)

# Inserts para alumno
cur.executemany(
    "INSERT INTO alumno (nombre) VALUES (?)",
    [
        ("Lucas",),
        ("María",),
        ("Javier",),
        ("Sofía",),
        ("Elena",),
        ("Pablo",)
    ]
)

# Inserts para inscripción
cur.executemany(
    "INSERT INTO inscripcion (alumno_id, curso_id, nota) VALUES (?,?,?)",
    [
        (1,1,9),
        (1,2,8),
        (2,1,10),
        (2,4,7),
        (3,3,6),
        (4,2,8),
        (4,1,7),
        (5,4,9),
        (6,3,6)
    ]
)

conn.commit()

cur.execute("SELECT * FROM alumno")
for fila in cur.fetchall():
    print(fila)

cur.execute("SELECT * FROM curso")
for fila in cur.fetchall():
    print(fila)

cur.execute("SELECT * FROM inscripcion")
for fila in cur.fetchall():
    print(fila)

cur.execute("SELECT * FROM profesor")
for fila in cur.fetchall():
    print(fila)


conn.close()