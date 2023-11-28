from Organismo import Organismo

class Animal(Organismo):
    def __init__(self, especie, dieta, posicion, vida, energia, velocidad):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta

    def cazar(self):
        pass
