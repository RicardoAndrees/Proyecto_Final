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
            pygame.image.load("Lagartija.png"),
            pygame.image.load("leon.png"),
            pygame.image.load("Cocodrilo.png"),
            pygame.image.load("Ciervo.png"),
            pygame.image.load("Conejo.png"),
            pygame.image.load("Elefante.png"),
            pygame.image.load("Cuervo.png"),
            pygame.image.load("Tiburon.png")
        ]

        self.font = pygame.font.Font(None, 36)  # Tamaño de la fuente

        self.num_celdas_x = 15
        self.num_celdas_y = 15
        self.ancho_celda = self.screen_size[0] // self.num_celdas_x
        self.alto_celda = self.screen_size[1] // self.num_celdas_y

        self.num_sprites = len(self.sprites)

        # Matriz que representa las celdas, inicialmente todas vacías
        self.matriz_celdas = [[None for _ in range(self.num_celdas_x)] for _ in range(self.num_celdas_y)]

        self.sprites_posiciones = [None] * self.num_sprites
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
        return self.matriz_celdas[posicion[1]][posicion[0]] is not None

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

        if antigua_posicion is not None:
            # Liberar la celda ocupada por el sprite anterior
            self.matriz_celdas[antigua_posicion[1]][antigua_posicion[0]] = None

        nueva_posicion = list(antigua_posicion) if antigua_posicion is not None else [random.randint(0, self.num_celdas_x - 1), random.randint(0, self.num_celdas_y - 1)]

        if direccion == pygame.K_LEFT and nueva_posicion[0] > 0:
            nueva_posicion[0] -= 1
        elif direccion == pygame.K_RIGHT and nueva_posicion[0] < self.num_celdas_x - 1:
            nueva_posicion[0] += 1
        elif direccion == pygame.K_UP and nueva_posicion[1] > 0:
            nueva_posicion[1] -= 1
        elif direccion == pygame.K_DOWN and nueva_posicion[1] < self.num_celdas_y - 1:
            nueva_posicion[1] += 1
    
        if not self.hay_sprite_en_celda(nueva_posicion):
            self.matriz_celdas[nueva_posicion[1]][nueva_posicion[0]] = indice
            self.sprites_posiciones[indice] = nueva_posicion
            pygame.time.delay(500)

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
