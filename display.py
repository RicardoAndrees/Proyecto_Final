import pygame
import sys
import random
import time
from organismos import Animal, Planta

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
        
        self.plantas = [
            pygame.image.load("girasol.png"),
            pygame.image.load("arbolito.png"),
            pygame.image.load("lechuga.png"),
            pygame.image.load("abedul.png"), 
            pygame.image.load("mariajuana.png")   
        ]
        self.font = pygame.font.Font(None, 36) 

        self.num_celdas_x = 15
        self.num_celdas_y = 15
        self.ancho_celda = self.screen_size[0] // self.num_celdas_x
        self.alto_celda = self.screen_size[1] // self.num_celdas_y

        self.num_sprites = len(self.sprites)

        self.matriz_celdas = [[None for _ in range(self.num_celdas_x)] for _ in range(self.num_celdas_y)]

        self.indice_cocodrilo = 1
        self.indice_lagartija = 2
        self.indice_leon = 3
        self.indice_tigre = 4
        self.indice_cuervo = 5
        self.indice_elefante = 6
        self.indice_tiburon = 7
        self.indice_conejo = 8
        self.indice_pez = 9
        self.indice_ciervo = 10

        self.rango_x_general = (9, 15)  
        self.rango_y_general = (0, self.num_celdas_y - 1)  

        self.organismos = [
            Animal(posicion=[1, 11], vida=100, energia=50, velocidad=1, especie="Tiburón", dieta="Peces", imagen_path="tiburon.png"),

        ]


        self.rango_x_tiburon = (1, 5) 
        self.rango_y_tiburon = (11, 14) 

        for i in range(self.num_sprites):
            sprite = self.sprites[i]
            rango_x_sprite = (0, self.num_celdas_x - 1)
            rango_y_sprite = (0, self.num_celdas_y - 1)

            if i == self.indice_tiburon or i == self.indice_pez:
                rango_x_sprite = self.rango_x_tiburon
                rango_y_sprite = self.rango_y_tiburon

        self.sprites_posiciones = [None] * self.num_sprites 


        self.sprites_direcciones = [None] * self.num_sprites
        self.tiempo_aleatorio = time.time()
        self.clock = pygame.time.Clock()

    def generar_direccion_aleatoria(self):
        return random.choice([pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])

    def mover_sprites_aleatoriamente(self):
        self.clock.tick(1)  
        tiempo_actual = time.time()

        if tiempo_actual - self.tiempo_aleatorio > 1:
            self.sprites_direcciones = [self.generar_direccion_aleatoria() for _ in range(self.num_sprites)]
            self.tiempo_aleatorio = tiempo_actual

        for i in range(self.num_sprites):
            direccion = self.sprites_direcciones[i]
            rango_x_sprite = self.rango_x_general
            rango_y_sprite = self.rango_y_general

            if i == self.indice_tiburon or i == self.indice_pez:
                rango_x_sprite = self.rango_x_tiburon
                rango_y_sprite = self.rango_y_tiburon

            posicion = self.sprites_posiciones[i]
            if posicion is not None and (
                rango_x_sprite[0] <= posicion[0] <= rango_x_sprite[1] and
                rango_y_sprite[0] <= posicion[1] <= rango_y_sprite[1]
            ):
                self.actualizar_posicion_sprite(i, direccion, rango_x_sprite, rango_y_sprite)

                posicion = self.sprites_posiciones[i]
                if posicion is not None and not (rango_x_sprite[0] <= posicion[0] <= rango_x_sprite[1] and
                        rango_y_sprite[0] <= posicion[1] <= rango_y_sprite[1]):
                    nueva_posicion = [posicion[0] % self.num_celdas_x, posicion[1] % self.num_celdas_y]
                    self.sprites_posiciones[i] = nueva_posicion
                    self.matriz_celdas[posicion[1]][posicion[0]] = None
                    self.matriz_celdas[nueva_posicion[1]][nueva_posicion[0]] = i



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
    

        for i in range(self.num_sprites):
            sprite_width, sprite_height = self.sprites[i].get_size()
            x = self.sprites_posiciones[i][0] * self.ancho_celda + (self.ancho_celda - sprite_width) // 2
            y = self.sprites_posiciones[i][1] * self.alto_celda + (self.alto_celda - sprite_height) // 2

            self.screen.blit(self.sprites[i], (x, y))

        for organismo in self.organismos:
            organismo.dibujar(self.screen, self.ancho_celda, self.alto_celda)

    def mover_organismos_aleatoriamente(self):
        self.clock.tick(10)  
        tiempo_actual = time.time()

        if tiempo_actual - self.tiempo_aleatorio > 1:
            for organismo in self.organismos:
                organismo.mover_aleatoriamente()  
            self.tiempo_aleatorio = tiempo_actual

        for i in range(self.num_sprites):
            direccion = self.sprites_direcciones[i]

            if self.sprites_posiciones[i] is not None:
                nueva_posicion = self.sprites_posiciones[i].copy()

                if i in [self.indice_tiburon, self.indice_pez]:
                    nueva_posicion[0] += random.choice([-1, 0, 1])
                    nueva_posicion[1] += random.choice([-1, 0, 1])

                    nueva_posicion[0] = max(self.rango_x_tiburon[0], min(self.rango_x_tiburon[1], nueva_posicion[0]))
                    nueva_posicion[1] = max(self.rango_y_tiburon[0], min(self.rango_y_tiburon[1], nueva_posicion[1]))
                else:
                    nueva_posicion[0] += random.choice([-1, 0, 1])
                    nueva_posicion[1] += random.choice([-1, 0, 1])

                    nueva_posicion[1] = min(10, nueva_posicion[1])

                    nueva_posicion[0] = max(9, min(15, nueva_posicion[0]))

                nueva_posicion[0] = nueva_posicion[0] % self.num_celdas_x
                nueva_posicion[1] = nueva_posicion[1] % self.num_celdas_y

                if not self.hay_sprite_en_celda(nueva_posicion):
                    if self.sprites_posiciones[i] is not None:
                        self.matriz_celdas[self.sprites_posiciones[i][1]][self.sprites_posiciones[i][0]] = None
                    self.matriz_celdas[nueva_posicion[1]][nueva_posicion[0]] = i
                    self.sprites_posiciones[i] = nueva_posicion
            else:
                nueva_posicion = [0, 0]
                self.matriz_celdas[nueva_posicion[1]][nueva_posicion[0]] = i
                self.sprites_posiciones[i] = nueva_posicion


    def actualizar_posicion_sprite(self, indice, direccion, rango_x_sprite, rango_y_sprite):
        if self.sprites_posiciones[indice] is not None:
            nueva_posicion = self.sprites_posiciones[indice].copy()
        else:
            nueva_posicion = [0, 0]  

        if direccion == pygame.K_LEFT:
            nueva_posicion[0] -= 1
        elif direccion == pygame.K_RIGHT:
            nueva_posicion[0] += 1
        elif direccion == pygame.K_UP:
            nueva_posicion[1] -= 1
        elif direccion == pygame.K_DOWN:
            nueva_posicion[1] += 1

        nueva_posicion[0] = max(rango_x_sprite[0], min(rango_x_sprite[1], nueva_posicion[0]))
        nueva_posicion[1] = max(rango_y_sprite[0], min(rango_y_sprite[1], nueva_posicion[1]))

        return nueva_posicion

    def panel_de_control(self):
        pass

    def ejecutar_interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.mover_sprites_aleatoriamente()
            self.mover_organismos_aleatoriamente()
            self.dibujar_ecosistema()
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    interfaz = InterfazGrafica()
    interfaz.ejecutar_interfaz()
