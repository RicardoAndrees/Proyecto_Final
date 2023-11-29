import pygame
import sys

class InterfazGrafica:
    def __init__(self):
        pygame.init()

        self.screen_size = (1340, 736)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Simulador de Ecosistemas")
        self.fondo = pygame.image.load("mapita_2.png")
        self.fondo = pygame.transform.scale(self.fondo, self.screen_size)
        self.font = pygame.font.Font(None, 36) 

        self.num_celdas_x = 15
        self.num_celdas_y = 15
        self.ancho_celda = self.screen_size[0] // self.num_celdas_x
        self.alto_celda = self.screen_size[1] // self.num_celdas_y
        self.matriz_celdas = [[None for _ in range(self.num_celdas_x)] for _ in range(self.num_celdas_y)]

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
                
    def actualizar_sprites(self):
        for sprite in self.sprites_instancias:
            sprite.mover(self.screen_size[0], self.screen_size[1])

    def ejecutar_interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            # Dibujar el ecosistema
            self.dibujar_ecosistema()

            pygame.display.flip()