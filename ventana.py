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

        self.sprite_m9 = pygame.image.load("m9.png")

        self.num_celdas_x = 15
        self.num_celdas_y = 15
        self.ancho_celda = self.screen_size[0] // self.num_celdas_x
        self.alto_celda = self.screen_size[1] // self.num_celdas_y

        self.valores_celdas = [[0 for _ in range(self.num_celdas_x)] for _ in range(self.num_celdas_y)]
        self.posicion_sprite = [random.randint(0, self.num_celdas_x - 1), random.randint(0, self.num_celdas_y - 1)]
        self.direccion_sprite = None
        self.tiempo_aleatorio = time.time()


    def generar_direccion_aleatoria(self):
        return random.choice([pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])

    def mover_sprite_aleatoriamente(self):
        tiempo_actual = time.time()

        if tiempo_actual - self.tiempo_aleatorio > 1:
            self.direccion_sprite = self.generar_direccion_aleatoria()
            self.tiempo_aleatorio = tiempo_actual

        self.actualizar_posicion_sprite(self.direccion_sprite)

    def dibujar_ecosistema(self):
        self.screen.blit(self.fondo, (0, 0))

        for i in range(self.num_celdas_x):
            for j in range(self.num_celdas_y):
                x = i * self.ancho_celda 
                y = j * self.alto_celda

                pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.ancho_celda, self.alto_celda), 2)
        
        x = self.posicion_sprite[0] * self.ancho_celda
        y = self.posicion_sprite[1] * self.alto_celda
        self.screen.blit(self.sprite_m9, (x, y))
    
    def actualizar_posicion_sprite(self, direccion):
        nueva_posicion = list(self.posicion_sprite)

        if direccion == pygame.K_LEFT and nueva_posicion[0] > 0:
            nueva_posicion[0] -= 1
        elif direccion == pygame.K_RIGHT and nueva_posicion[0] < self.num_celdas_x - 1:
            nueva_posicion[0] += 1
        elif direccion == pygame.K_UP and nueva_posicion[1] > 0:
            nueva_posicion[1] -= 1
        elif direccion == pygame.K_DOWN and nueva_posicion[1] < self.num_celdas_y - 1:
            nueva_posicion[1] += 1

        self.posicion_sprite = nueva_posicion
        pygame.time.delay(2000)

    def ejecutar_interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.mover_sprite_aleatoriamente()
            self.dibujar_ecosistema()
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    interfaz = InterfazGrafica()
    interfaz.ejecutar_interfaz()
