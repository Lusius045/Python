import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="prueba")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS alumno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
)
""")

# INSERT
cur.execute("INSERT INTO alumno (nombre, edad) VALUES (%s, %s)", ("Juan", 20))
cur.execute("INSERT INTO alumno (nombre, edad) VALUES (%s, %s)", ("Ana", 22))
conn.commit()

# SELECT
cur.execute("SELECT * FROM alumno")
print("Lista de alumnos:")
for fila in cur.fetchall():
    print(fila)

# UPDATE
cur.execute("UPDATE alumno SET edad = %s WHERE nombre = %s", (23, "Ana"))
conn.commit()

# DELETE
cur.execute("DELETE FROM alumno WHERE nombre = %s", ("Juan",))
conn.commit()

conn.close()