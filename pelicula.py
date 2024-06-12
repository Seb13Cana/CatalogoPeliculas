#Creamos la clase de la pelicula
class Pelicula:

    def __init__(self, nombre, genero, anio):
        self.nombre = nombre
        self.genero = genero
        self.anio = anio

    def __str__(self):
        return f'Pelicula {self.nombre}, Genero: {self.genero}, Año: {self.anio}'
