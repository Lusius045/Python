cur.execute("USE instituto")

cur.executemany(
"INSERT INTO profesor (nombre, especialidad) VALUES (%s,%s)",
[("Juan Perez","Programación"),("Ana Lopez","Base de Datos"),
("Luis Gomez","Redes"),("Carla Ruiz","Programación")]
)

cur.executemany(
"INSERT INTO curso (nombre, profesor_id, cupo) VALUES (%s,%s,%s)",
[("Python Inicial",1,30),("SQL Básico",2,25),
("Redes 1",3,20),("Python Avanzado",4,15)]
)

cur.executemany(
"INSERT INTO alumno (nombre) VALUES (%s)", 
[("Lucas",),("María",),("Javier",),("Sofía",),("Elena",),("Pablo",)]
)

cur.executemany(
"INSERT INTO inscripcion (alumno_id, curso_id, nota) VALUES (%s,%s,%s)",
[(1,1,9),(1,2,8),(2,1,10),(2,4,7),(3,3,6),(4,2,8),
(4,1,7),(5,4,9),(6,3,6)]
)

conn.commit()
conn.close()