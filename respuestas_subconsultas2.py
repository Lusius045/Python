import sqlite3

# Conexión a la base
conn = sqlite3.connect("empresa_simple.db")
cur = conn.cursor()

# 1) Crear tablas e insertar datos
cur.execute("DROP TABLE IF EXISTS proyecto")
cur.execute("DROP TABLE IF EXISTS empleado")
cur.execute("DROP TABLE IF EXISTS departamento")

cur.execute("CREATE TABLE departamento (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
cur.execute("CREATE TABLE empleado (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, salario REAL, dep_id INTEGER, FOREIGN KEY (dep_id) REFERENCES departamento(id))")
cur.execute("CREATE TABLE proyecto (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, empleado_id INTEGER, FOREIGN KEY (empleado_id) REFERENCES empleado(id))")

cur.executemany("INSERT INTO departamento (nombre) VALUES (?)", [("Recursos Humanos",), ("IT",), ("Ventas",)])
cur.executemany("INSERT INTO empleado (nombre, salario, dep_id) VALUES (?,?,?)", [
    ("Ana", 2500, 1),
    ("Luis", 3000, 2),
    ("Carla", 3200, 2),
    ("Pedro", 2000, 3),
    ("Sofia", 2700, 1)
])
cur.executemany("INSERT INTO proyecto (nombre, empleado_id) VALUES (?,?)", [
    ("Sistema RRHH", 1),
    ("Web Corporativa", 2),
    ("Aplicación Móvil", 3),
    ("Campaña Ventas", 4),
    ("ChatBot Soporte", 2)
])
conn.commit()

# 2) Empleados que ganan más que el promedio
cur.execute("""SELECT nombre FROM empleado WHERE salario > (SELECT AVG(salario) FROM empleado)""")
print("2)", cur.fetchall())

# 3) Empleados que trabajan en el mismo departamento que 'Luis'
cur.execute("""SELECT nombre FROM empleado WHERE dep_id = (SELECT dep_id FROM empleado WHERE nombre = 'Luis')""")
print("3)", cur.fetchall())

# 4) Empleados que no participan en ningún proyecto
cur.execute("""SELECT nombre FROM empleado WHERE id NOT IN (SELECT empleado_id FROM proyecto)""")
print("4)", cur.fetchall())

# 5) Departamentos con empleados que ganan más que el promedio general
cur.execute("""SELECT DISTINCT d.nombre FROM departamento d JOIN empleado e ON d.id = e.dep_id WHERE e.salario > (SELECT AVG(salario) FROM empleado)""")
print("5)", cur.fetchall())

# 6) Empleados con salario más alto en su departamento
cur.execute("""SELECT nombre FROM empleado e1 WHERE salario = (SELECT MAX(salario) FROM empleado e2 WHERE e2.dep_id = e1.dep_id)""")
print("6)", cur.fetchall())

# 7) Proyectos donde el empleado gana más que el promedio de su departamento
cur.execute("""SELECT p.nombre FROM proyecto p JOIN empleado e ON e.id = p.empleado_id WHERE e.salario > (SELECT AVG(salario) FROM empleado WHERE dep_id = e.dep_id)""")
print("7)", cur.fetchall())

# 8) Departamento con el salario promedio más alto
cur.execute("""SELECT nombre FROM departamento WHERE id = (SELECT dep_id FROM empleado GROUP BY dep_id ORDER BY AVG(salario) DESC LIMIT 1)""")
print("8)", cur.fetchall())

# 9) Aumentar salario 10% a los empleados con salario menor al promedio
cur.execute("""UPDATE empleado SET salario = salario * 1.1 WHERE salario < (SELECT AVG(salario) FROM empleado)""")
conn.commit()

# Verificar resultado
cur.execute("SELECT nombre, salario FROM empleado")
print("9)", cur.fetchall())

# 10) Eliminar proyectos de empleados con salario menor al promedio
cur.execute("""DELETE FROM proyecto WHERE empleado_id IN (SELECT id FROM empleado WHERE salario < (SELECT AVG(salario) FROM empleado))""")
conn.commit()

cur.execute("SELECT * FROM proyecto")
print("10)", cur.fetchall())

conn.close()