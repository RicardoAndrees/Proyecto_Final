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
        self.ambientes = ambientes
        self.size = size
        self.seccion_actual = 0

    def add_organism(self, organism):
        self.organisms.append(organism)
        self.matriz_espacial.agregar_organismo(organism)

    def dibujar_ecosistema(self, screen, seccion_actual):
        for organismo in self.organisms:
            x, y = organismo.posicion
            if isinstance(organismo, Animal) and hasattr(organismo, 'sprite') and organismo.sprite is not None:
                sprite = organismo.sprite
                if hasattr(sprite, 'get_size'):
                    sprite_size = sprite.get_size()
                    screen.blit(sprite, (y * 20, x * 20 + seccion_actual * self.size[1] // 3))
            else:
                sprite = pygame.image.load("arbolito.png")
                sprite = pygame.transform.scale(sprite, (20, 20))
                screen.blit(sprite, (y * 20, x * 20 + seccion_actual * self.size[1] // 3))

    def dibujar_fondos(self, screen):
        for seccion_actual, ambiente in enumerate(self.ambientes):
            seccion_height = self.size[1] // 3
            seccion_rect = pygame.Rect(0, seccion_actual * seccion_height, self.size[0], seccion_height)
            
            if seccion_actual == 0: 
                ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect)
            else: 
                if seccion_actual == 1:
                    ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect)
                elif seccion_actual == 2:
                    seccion_rect_left = pygame.Rect(0, seccion_actual * seccion_height, self.size[0] // 2, seccion_height)
                    ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect_left)
                    
                    seccion_rect_right = pygame.Rect(self.size[0] // 2, seccion_actual * seccion_height, self.size[0] // 2, seccion_height)
                    ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect_right)
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


    def run_cycle(self):
        for organismo in self.organisms:
            organismo.interactuar_con_entorno(self.ambientes[self.seccion_actual])
            organismo.moverse(self.obtener_direccion(), self.matriz_espacial)
            organismo.envejecer()
            organismo.energia -= 1

            if organismo.esta_vivo():
                pareja = self.obtener_pareja(organismo)
                organismo.reproducirse(pareja, self.matriz_espacial)
            if not organismo.esta_vivo():
                self.organisms.remove(organismo)

    def obtener_pareja(self, organismo):
        candidatos = [
            o for o in self.organisms
            if o != organismo and isinstance(o, organismo.__class__) and o.esta_vivo()
        ]

        if candidatos:
            return random.choice(candidatos)
        return None

    def obtener_direccion(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
