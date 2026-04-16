from libro import Libro
from biblio import Biblio

print('*** Sistema de biblioteca ***')

biblio1 = Biblio('amoroso')
biblio1.agregar_libro('Cazadores de sombras:los origenes (1.angel mecanico)', 'Cassandra clare', 'Fantasia')
biblio1.agregar_libro('Warhammer: Krieg', 'Steve Lyons', 'Ciencia ficcion')
biblio1.agregar_libro('Metro:2033', 'Dmitry Glukhovsky', 'Ciencia ficcion')

biblio1.buscar_autor('Dmitry Glukhovsky')

biblio1.buscar_genero('Ciencia ficcion')

biblio1.mostrar_libro('Cazadores de sombras:los origenes (1.angel mecanico)')

biblio1.mostrar_todos_libros()