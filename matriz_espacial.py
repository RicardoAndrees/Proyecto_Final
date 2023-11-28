# matriz_espacial.py
from itertools import product

class MatrizEspacial:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[None] * columnas for _ in range(filas)]

    def agregar_organismo(self, organismo):
        x, y = organismo.posicion
        self.matriz[x][y] = organismo

    def eliminar_organismo(self, organismo):
        x, y = organismo.posicion
        self.matriz[x][y] = None

    def mover_organismo(self, organismo, nueva_posicion):
        x, y = organismo.posicion
        nuevo_x, nuevo_y = nueva_posicion

        self.matriz[x][y] = None
        self.matriz[nuevo_x][nuevo_y] = organismo
        organismo.posicion = nueva_posicion

    def obtener_organismo_en_posicion(self, posicion):
        x, y = posicion
        return self.matriz[x][y]

    def encontrar_posicion_disponible(self, posicion_inicial):
        x, y = posicion_inicial

        for dx, dy in product([-1, 0, 1], repeat=2):
            nueva_x, nueva_y = x + dx, y + dy
            if 0 <= nueva_x < self.filas and 0 <= nueva_y < self.columnas and self.matriz[nueva_x][nueva_y] is None:
                return nueva_x, nueva_y
        else:
            return x, y
