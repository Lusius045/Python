import mysql.connector as mysql
from mysql.connector import Error

#Cambiar user, password y database por el que tengan ustedes
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "prueba",
    "charset": "utf8mb4",
    "use_unicode": True
}

def get_connection():
    try:
        conn = mysql.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print("Error al conectar:", e)
        return None


if __name__ == "__main__":
    
    conn = get_connection()
    
    if conn:
        cur = conn.cursor() 
        
        # Crear tabla
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
