class Libro:

    id_libro = 0

    def __init__ (self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor  
        self.genero = genero
        Libro.id_libro += 1

    @classmethod
    def get_id_libro(cls):
        return cls.id_libro