import pygame
import random

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad, imagen_path):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

        # Carga la imagen del sprite
        self.sprite = pygame.image.load(imagen_path)
        # Obtén las dimensiones del sprite
        self.sprite_width, self.sprite_height = self.sprite.get_size()

    def dibujar(self, screen, ancho_celda, alto_celda):
        x = self.posicion[0] * ancho_celda + (ancho_celda - self.sprite_width) // 2
        y = self.posicion[1] * alto_celda + (alto_celda - self.sprite_height) // 2

        # Dibuja el sprite en la pantalla
        screen.blit(self.sprite, (x, y))

    def mover_aleatoriamente(self):
        # Genera una dirección aleatoria: 0 izquierda, 1 derecha, 2 arriba, 3 abajo
        direccion = random.randint(0, 3)

        if direccion == 0:  # Izquierda
            self.posicion[0] -= 1
        elif direccion == 1:  # Derecha
            self.posicion[0] += 1
        elif direccion == 2:  # Arriba
            self.posicion[1] -= 1
        elif direccion == 3:  # Abajo
            self.posicion[1] += 1

    def reproducir(self, pareja):
        # Lógica para la reproducción con otro organismo
        pass

    def morir(self):
        # Lógica para la muerte del organismo
        pass


class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad, imagen_path)
        self.especie = especie
        self.dieta = dieta
        self.imagen = pygame.image.load(imagen_path)

    def dibujar(self, screen, ancho_celda, alto_celda):
        super().dibujar(screen, ancho_celda, alto_celda)  # Llama a la función dibujar de la clase Organismo
        x = self.posicion[0] * ancho_celda
        y = self.posicion[1] * alto_celda
        screen.blit(self.imagen, (x, y))

    def cazar(self, presa):
        # Lógica para cazar a otra entidad
        pass

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, tipo):
        super().__init__(posicion, vida, energia, velocidad)
        self.tipo = tipo

    def fotosintesis(self):
        # Lógica para realizar la fotosíntesis
        pass

    def reproducir(self):
        # Lógica para la reproducción por semillas
        pass
