class Curso:
    def __init__(self, titulo, profesor, especialidad):
        self.titulo = titulo
        self.profesor = profesor
        self.especialidad = especialidad

    @staticmethod
    def validarTitulo(titulo):
        if len(titulo) > 0:
            print("el titulo es valido") 
        else:
            print("el titulo es invaldio")

    @classmethod 
    def desdeString(cls, nuevoCurso):
        partes = nuevoCurso.split('-')

        if len(partes) == 3:
            curso = Curso(partes[0], partes[1], partes[2])
            return cls(curso)
    