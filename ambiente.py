import pygame
import random

class Ambiente:
    def __init__(self, factor_abiotico, fondo_path=None, fondo_color=None, arbolito_path=None, size=None):
        self.factor_abiotico = factor_abiotico
        self.fondo_path = fondo_path
        self.fondo_color = fondo_color
        self.size = size

        if self.fondo_path:
            original_fondo = pygame.image.load(self.fondo_path)
            original_width, original_height = original_fondo.get_size()

            top_width = self.size[0]
            top_height = self.size[1] // 3
            self.fondo_top = pygame.transform.scale(original_fondo, (top_width, top_height))

            bottom_width = self.size[0]
            bottom_height = self.size[1] // 3
            self.fondo_left = pygame.transform.scale(original_fondo, (bottom_width, bottom_height))
            self.fondo_right = pygame.transform.scale(original_fondo, (bottom_width, bottom_height))

        elif self.fondo_color:
            self.fondo_top = pygame.Surface((self.size[0], self.size[1] // 3))
            self.fondo_top.fill(self.fondo_color)

            self.fondo_left = pygame.Surface((self.size[0] // 2, self.size[1] // 3))
            self.fondo_left.fill(self.fondo_color)

            self.fondo_right = pygame.Surface((self.size[0] // 2, self.size[1] // 3))
            self.fondo_right.fill(self.fondo_color)
        else:
            self.fondo_top = None
            self.fondo_left = None
            self.fondo_right = None

        self.arbolito_path = arbolito_path
        self.arbolitos = self.cargar_arbolitos(size)

    def cargar_arbolitos(self, size):
        arbolitos = []
        if self.arbolito_path:
            arbolito_img = pygame.image.load(self.arbolito_path)
            arbolito_img = pygame.transform.scale(arbolito_img, (20, 20))
            for _ in range(5):
                x = random.randint(0, size[0] - 20)
                y = random.randint(0, size[1] // 3 - 20)
                arbolitos.append((arbolito_img, (x, y)))
        return arbolitos

    def dibujar_fondo(self, screen, seccion_actual, seccion_rect):
        if seccion_actual == 0:  # Primera sección
            if self.fondo_top:
                screen.blit(self.fondo_top, (0, seccion_actual * seccion_rect.height))
        else:  # Segunda y tercera sección
            if seccion_actual == 1:
                screen.blit(self.fondo_left, (0, seccion_actual * seccion_rect.height))
            elif seccion_actual == 2:
                # Ajusta el rectángulo para dividir en dos a lo alto
                seccion_rect_bottom = pygame.Rect(0, seccion_actual * seccion_rect.height + seccion_rect.height // 2, self.size[0], seccion_rect.height // 2)
                screen.blit(self.fondo_left, (0, seccion_actual * seccion_rect.height))
                screen.blit(self.fondo_right, (self.size[0] // 2, seccion_actual * seccion_rect.height + seccion_rect.height // 2))

    def afectar_ecosistema(self, ecosistema):
        for organismo in ecosistema.organisms:
            organismo.energia += self.factor_abiotico * 10

    def generar_evento_climatico(self, ecosistema):
        evento_probabilidad = random.uniform(0, 1)

        if evento_probabilidad > 0.8:
            print("¡Evento climático!")
            for organismo in ecosistema.organisms:
                organismo.velocidad *= 0.5

    def interactuar_con_ecosistema(self, ecosistema):
        self.afectar_ecosistema(ecosistema)
        self.generar_evento_climatico(ecosistema)
