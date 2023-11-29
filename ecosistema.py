import pygame
import random
from matriz_espacial import MatrizEspacial
from organismos import Animal, Planta

class Ecosistema:
    def __init__(self, rows, cols, ambientes, size):
        self.matriz_espacial = MatrizEspacial(filas=rows, columnas=cols)
        self.organisms = []
        self.rows = rows
        self.cols = cols
        self.ambientes = ambientes or []  # Provide a default value or handle an empty list
        self.size = size
        self.seccion_actual = 0

    def add_organism(self, organism):
        self.organisms.append(organism)
        self.matriz_espacial.agregar_organismo(organism)

    def populate_ecosystem(self):
        for _ in range(10):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            nuevo_organismo = Animal(especie="Tigre", dieta="Carnívoro", posicion=(x, y), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")
            self.add_organism(nuevo_organismo)

        for _ in range(10):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            nueva_planta = Planta(posicion=(x, y), vida=50, energia=50, velocidad=1)
            self.add_organism(nueva_planta)

    def interactuar_con_ecosistema(self):
        for organismo in self.organisms:
            organismo.interactuar_con_entorno(self.ambientes[self.seccion_actual])
            organismo.envejecer()
            organismo.energia -= 1

            if organismo.esta_vivo():
                self.add_organism(organismo.reproducirse(self.matriz_espacial))
                
        # Eliminar organismos muertos
        self.organisms = [organismo for organismo in self.organisms if organismo.esta_vivo()]

