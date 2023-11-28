import pygame
import sys
import random
import time
from organismo import Organismo
from animal import Animal

class InterfazGrafica:
    def __init__(self):
        pygame.init()

        self.screen_size = (1340, 736)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Simulador de Ecosistemas")

        self.fondo = pygame.image.load("mapita_2.png")
        self.fondo = pygame.transform.scale(self.fondo, self.screen_size)

        self.sprites = [
            pygame.image.load("Lagartija.png"),
            pygame.image.load("leon.png"),
            pygame.image.load("Cocodrilo.png"),
            pygame.image.load("Ciervo.png"),
            pygame.image.load("Conejo.png"),
            pygame.image.load("Elefante.png"),
            pygame.image.load("Cuervo.png"),
            pygame.image.load("Tiburon.png"),
            pygame.image.load("Tigre.png"),
            pygame.image.load("Pez.png")
        ]

        self.font = pygame.font.Font(None, 36) 

        self.num_celdas_x = 15
        self.num_celdas_y = 15
        self.ancho_celda = self.screen_size[0] // self.num_celdas_x
        self.alto_celda = self.screen_size[1] // self.num_celdas_y

        self.num_sprites = len(self.sprites)

        self.matriz_celdas = [[None for _ in range(self.num_celdas_x)] for _ in range(self.num_celdas_y)]

        self.indice_tiburon = 7
        self.indice_pez = 9

        velocidad_tiburon = 2
        velocidad_pez = 1

        self.sprites_posiciones[self.indice_tiburon] = [1, 11]
        self.rango_x_tiburon = (1, 5)
        self.rango_y_tiburon = (11, 14)
        self.sprites[self.indice_tiburon] = Animal("Tiburon", "Carnivoro", [1, 11], 100, 100, velocidad_tiburon)

        self.sprites_posiciones[self.indice_pez] = [2, 11]
        self.rango_x_pez = (2, 6)
        self.rango_y_pez = (11, 14)
        self.sprites[self.indice_pez] = Animal("Pez", "Herbivoro", [2, 11], 50, 50, velocidad_pez)

        for i in range(self.num_sprites):
            if self.sprites_posiciones[i] is None:
                self.sprites_posiciones[i] = [random.randint(0, self.num_celdas_x - 1), random.randint(0, self.num_celdas_y - 1)]

        self.sprites_direcciones = [None] * self.num_sprites
        self.tiempo_aleatorio = time.time()

    def generar_direccion_aleatoria(self):
        return random.choice([pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])

    def mover_sprites_aleatoriamente(self):
        tiempo_actual = time.time()

        rango_x_sprite = (0, self.num_celdas_x - 1)
        rango_y_sprite = (0, self.num_celdas_y - 1)

        if tiempo_actual - self.tiempo_aleatorio > 1:
            self.sprites_direcciones = [self.generar_direccion_aleatoria() for _ in range(self.num_sprites)]
            self.tiempo_aleatorio = tiempo_actual

        for i in range(self.num_sprites):
            sprite = self.sprites[i]

            if i == self.indice_tiburon:
                rango_x_sprite = self.rango_x_tiburon
                rango_y_sprite = self.rango_y_tiburon
            elif i == self.indice_pez:
                rango_x_sprite = self.rango_x_pez
                rango_y_sprite = self.rango_y_pez

            posicion = self.sprites_posiciones[i]
            if not (rango_x_sprite[0] <= posicion[0] <= rango_x_sprite[1] and
                    rango_y_sprite[0] <= posicion[1] <= rango_y_sprite[1]):
                self.sprites_direcciones[i] = self.generar_direccion_aleatoria()
                velocidad = self.sprites[i].velocidad
                # Actualizar la posición según la velocidad del animal
                for _ in range(velocidad):
                    self.actualizar_posicion_sprite(i, self.sprites_direcciones[i])

        self.tiempo_aleatorio = tiempo_actual  # Mover la actualización del tiempo al final
            
    def hay_sprite_en_celda(self, posicion):
        if 0 <= posicion[1] < self.num_celdas_y and 0 <= posicion[0] < self.num_celdas_x:
            return self.matriz_celdas[posicion[1]][posicion[0]] is not None
        else:
            return False


    def dibujar_ecosistema(self):
        self.screen.blit(self.fondo, (0, 0))

        for i in range(self.num_celdas_x):
            for j in range(self.num_celdas_y):
                x = i * self.ancho_celda
                y = j * self.alto_celda

                pygame.draw.rect(self.screen, (89, 167, 80), (x, y, self.ancho_celda, self.alto_celda), 2)

                numero_celda = str(j * self.num_celdas_x + i + 1)
                texto_surface = self.font.render(numero_celda, True, (255, 255, 255))
                texto_rect = texto_surface.get_rect(center=(x + self.ancho_celda // 2, y + self.alto_celda // 2))
                self.screen.blit(texto_surface, texto_rect)

        for i in range(self.num_sprites):
            sprite_width, sprite_height = self.sprites[i].get_size()
            x = self.sprites_posiciones[i][0] * self.ancho_celda + (self.ancho_celda - sprite_width) // 2
            y = self.sprites_posiciones[i][1] * self.alto_celda + (self.alto_celda - sprite_height) // 2
            
            self.screen.blit(self.sprites[i], (x, y))

    def actualizar_posicion_sprite(self, indice, direccion):
        antigua_posicion = self.sprites_posiciones[indice]

        if antigua_posicion is not None and 0 <= antigua_posicion[0] < self.num_celdas_x and 0 <= antigua_posicion[1] < self.num_celdas_y:
            self.matriz_celdas[antigua_posicion[1]][antigua_posicion[0]] = None

        nueva_posicion = list(antigua_posicion) if antigua_posicion is not None else [1, 11]

        if direccion == pygame.K_LEFT and self.num_celdas_x > nueva_posicion[0] > 0:
            nueva_posicion[0] -= 1
        elif direccion == pygame.K_RIGHT and self.num_celdas_x > nueva_posicion[0] < self.num_celdas_x - 1:
            nueva_posicion[0] += 1
        elif direccion == pygame.K_UP and self.num_celdas_y > nueva_posicion[1] > 0:
            nueva_posicion[1] -= 1
        elif direccion == pygame.K_DOWN and self.num_celdas_y > nueva_posicion[1] < self.num_celdas_y - 1:
            nueva_posicion[1] += 1

        if indice == self.indice_tiburon:
            nueva_posicion[0] = max(self.rango_x_tiburon[0], min(self.rango_x_tiburon[1], nueva_posicion[0]))
            nueva_posicion[1] = max(self.rango_y_tiburon[0], min(self.rango_y_tiburon[1], nueva_posicion[1]))

        if 0 <= nueva_posicion[0] < self.num_celdas_x and 0 <= nueva_posicion[1] < self.num_celdas_y:
            if not self.hay_sprite_en_celda(nueva_posicion):
                self.matriz_celdas[nueva_posicion[1]][nueva_posicion[0]] = indice
                self.sprites_posiciones[indice] = nueva_posicion


    def ejecutar_interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.mover_sprites_aleatoriamente()
            self.dibujar_ecosistema()
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    interfaz = InterfazGrafica()
    interfaz.ejecutar_interfaz()
