import pygame
import sys
import random
import time

class InterfazGrafica:
    def __init__(self):
        pygame.init()

        self.screen_size = (736, 736)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Simulador de Ecosistemas")

        self.fondo = pygame.image.load("mapita_sn.jpg")
        self.fondo = pygame.transform.scale(self.fondo, self.screen_size)

        self.sprites = [
            pygame.image.load("m9.png"),
            pygame.image.load("leon.png"),
            pygame.image.load("m9.png")
        ]

        self.num_celdas_x = 15
        self.num_celdas_y = 15
        self.ancho_celda = self.screen_size[0] // self.num_celdas_x
        self.alto_celda = self.screen_size[1] // self.num_celdas_y

        self.num_sprites = len(self.sprites)
        self.sprites_posiciones = [[random.randint(0, self.num_celdas_x - 1), random.randint(0, self.num_celdas_y - 1)] for _ in range(self.num_sprites)]
        self.sprites_direcciones = [None] * self.num_sprites
        self.tiempo_aleatorio = time.time()

    def generar_direccion_aleatoria(self):
        return random.choice([pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])

    def mover_sprites_aleatoriamente(self):
        tiempo_actual = time.time()

        if tiempo_actual - self.tiempo_aleatorio > 1:
            self.sprites_direcciones = [self.generar_direccion_aleatoria() for _ in range(self.num_sprites)]
            self.tiempo_aleatorio = tiempo_actual

        for i in range(self.num_sprites):
            self.actualizar_posicion_sprite(i, self.sprites_direcciones[i])

    def hay_sprite_en_celda(self, posicion):
        return posicion in self.sprites_posiciones

    def dibujar_ecosistema(self):
        self.screen.blit(self.fondo, (0, 0))

        for i in range(self.num_celdas_x):
            for j in range(self.num_celdas_y):
                x = i * self.ancho_celda
                y = j * self.alto_celda

                pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.ancho_celda, self.alto_celda), 2)

        for i in range(self.num_sprites):
            sprite_width, sprite_height = self.sprites[i].get_size()
            x = self.sprites_posiciones[i][0] * self.ancho_celda + (self.ancho_celda - sprite_width) // 2
            y = self.sprites_posiciones[i][1] * self.alto_celda + (self.alto_celda - sprite_height) // 2
            self.screen.blit(self.sprites[i], (x, y))

    def actualizar_posicion_sprite(self, indice, direccion):
        nueva_posicion = list(self.sprites_posiciones[indice])

        if direccion == pygame.K_LEFT and nueva_posicion[0] > 0:
            nueva_posicion[0] -= 1
        elif direccion == pygame.K_RIGHT and nueva_posicion[0] < self.num_celdas_x - 1:
            nueva_posicion[0] += 1
        elif direccion == pygame.K_UP and nueva_posicion[1] > 0:
            nueva_posicion[1] -= 1
        elif direccion == pygame.K_DOWN and nueva_posicion[1] < self.num_celdas_y - 1:
            nueva_posicion[1] += 1

        if not self.hay_sprite_en_celda(nueva_posicion):
            self.sprites_posiciones[indice] = nueva_posicion
            pygame.time.delay(1000)

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
