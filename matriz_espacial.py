class MatrizEspacial:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.matriz = [[None for _ in range(num_columnas)] for _ in range(num_filas)]

    def agregar_organismo(self, organismo, posicion):
        fila, columna = posicion
        if 0 <= fila < self.num_filas and 0 <= columna < self.num_columnas:
            self.matriz[fila][columna] = organismo

    def obtener_organismo(self, posicion):
        fila, columna = posicion
        if 0 <= fila < self.num_filas and 0 <= columna < self.num_columnas:
            return self.matriz[fila][columna]
        return None
