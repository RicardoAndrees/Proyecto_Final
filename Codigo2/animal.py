from organismo import Organismo

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especies, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especies = especies
        self.dieta = dieta

    def cazar(self):
        pass

    def mover_celda(self, ancho_celda, alto_celda, num_celdas_x, num_celdas_y):
        # Mueve el animal en una celda
        self.rect.x += ancho_celda

        # Verifica si el animal ha llegado al final de una fila
        if self.rect.x >= ancho_celda * num_celdas_x:
            self.rect.x = 0
            self.rect.y += alto_celda

        # Verifica si el animal ha llegado al final de la matriz
        if self.rect.y >= alto_celda * num_celdas_y:
            self.rect.y = 0