from libro import Libro

class Biblio:

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, titulo, autor, genero):
        libro = Libro(titulo, autor, genero)
        self.libros.append(libro)

    def buscar_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                print(f'Libro del autor {libro.autor}: Titulo:{libro.titulo} - Genero:{libro.genero}')
                
    def buscar_genero(self, genero):
        for libro in self.libros:
            if libro.genero == genero:
                print(f'Libro del genero {libro.genero}: Titulo:{libro.titulo} - Autor:{libro.autor}')

    def mostrar_todos_libros(self):
        for libro in self.libros:
            print(f'''Titulo: {libro.titulo}
            Autor: {libro.autor}
            Genero: {libro.genero}''')
        print (f'Cantidad de libros {libro.id_libro}')

    def mostrar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                print(f'''Titulo: {libro.titulo}
                Autor: {libro.autor}
                Genero: {libro.genero}''')

    

    