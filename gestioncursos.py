class Persona:
    def __init__ (self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__ (self):
        return f"{self.nombre} ({self.email})"
    
class Estudiante(Persona):
    def __init__ (self, nombre, email, cursosIns, cantIns):
        super().__init__(self, nombre, email)
        self.cursosIns = [] 
        self.cantIns = 0

    def inscribirseCurso (self, cursos):
        self.cursosIns.append(cursos)
        self.cantIns +=1

    def mostrarCursos (self):
        for c in self.cursosIns:
            print (c)
    
    def presentacion(self):
        return f"Soy {self.nombre} y estoy cursando {self.cantIns} cursos"

class Profesor(Persona):
    def __init__ (self, nombre, email, especialidad):
        super().__init__(self, nombre, email)
        self.especialidad = especialidad 

    def __str__ (self):
        return f"Profesor {self.nombre}, {self.especialidad}"
    
    def presentacion(self):
        return f"Soy Profesor {self.nombre} y enseño {self.especialidad}"
    
class Curso:
    def __init__(self, titulo, profesor, estudiantes):
        self.titulo = titulo
        self.profesor = Profesor
        self.estudiantes = []

    #def agregarEstudiantes(self):

    #    comp = True

    #    estudiante = Estudiante("Pepe","Pepe123@gmail.com")

    #    for e in self.estudiantes:
    #        if estudiante.nombre == estudiantes.nombre:
    #            raise ValueError ("El estudiante ya existe")
    #            comp = False

    #    if comp == True:
    #        self.estudiantes.append(estudiante)


    def listarEstudiantes(self):
        for e in self.estudiantes:
            print(e)

    def __str__(self):
        return f"Curso: {self.titulo} - Profesor: {self.profesor.nombre}"

    @classmethod
    def desdeString (cls, titulo, profesor, estudiantes):
        cls.titulo = titulo
        cls.profesor = Profesor("Juan","juan123@gmail.com","Informatica")
        cls.estudiantes = []
        
    @staticmethod
    def validarTitulo (estudiantes):
        for t in estudiantes.titulo:
            if t == "":
                print("El titulo no es valido, ya que está vacio")
                estudiantes.pop(t)