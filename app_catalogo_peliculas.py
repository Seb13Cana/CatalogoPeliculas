from pelicula import Pelicula
from catalogo_peliculas import CatalogoPeliculas as catalogo

print('*** Catsalogo de peliculas ***')
opcion = None

while opcion != 4:
    try:
        print('''
        1. Agregar pelicula
        2. Mostrar peliculas
        3. Eliminar Archivo
        4. Salir''')
        opcion = int(input('Por favor, ingresa una opción: '))

        if opcion == 1:
            nombre_pelicula = input('Ingresa el nombre de la pelicula: ')
            genero_pelicula = input('Ingresa el genero de la pelicula: ')
            anio_pelicula   = input('Ingresa el Año de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula,genero_pelicula,anio_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == 2:
            catalogo.listar_peliculas()
        elif opcion == 3:
            catalogo.eliminar_peliculas()

    except Exception as ex:
        print(f'Ocurrio un error: {ex}')
        opcion = None
else:
    print('Termino el programa')