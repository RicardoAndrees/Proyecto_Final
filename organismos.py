import pygame
import random

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad, imagen_path):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

        self.sprite = pygame.image.load(imagen_path)
        self.sprite_width, self.sprite_height = self.sprite.get_size()

    def dibujar(self, screen, ancho_celda, alto_celda):
        x = self.posicion[0] * ancho_celda + (ancho_celda - self.sprite_width) // 2
        y = self.posicion[1] * alto_celda + (alto_celda - self.sprite_height) // 2

        screen.blit(self.sprite, (x, y))

    def mover_aleatoriamente(self):
        direccion = random.randint(0, 3)

        if direccion == 0:  
            self.posicion[0] -= 1
        elif direccion == 1:  
            self.posicion[0] += 1
        elif direccion == 2:  
            self.posicion[1] -= 1
        elif direccion == 3:  
            self.posicion[1] += 1


    def reproducir(self, pareja):
        if isinstance(pareja, Organismo):
            nueva_posicion = [(self.posicion[0] + pareja.posicion[0]) // 2, (self.posicion[1] + pareja.posicion[1]) // 2]
            nueva_vida = (self.vida + pareja.vida) // 2
            nueva_energia = (self.energia + pareja.energia) // 2
            nueva_velocidad = (self.velocidad + pareja.velocidad) // 2

            nueva_instancia = Organismo(nueva_posicion, nueva_vida, nueva_energia, nueva_velocidad, "imagen_predeterminada.png")
            return nueva_instancia
        else:
            return None

    def morir(self):
        self.posicion = [-1, -1]


class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia, velocidad, imagen_path)
        self.especie = especie
        self.dieta = dieta
        self.imagen = pygame.image.load(imagen_path)

    def dibujar(self, screen, ancho_celda, alto_celda):
        super().dibujar(screen, ancho_celda, alto_celda)  
        x = self.posicion[0] * ancho_celda
        y = self.posicion[1] * alto_celda
        screen.blit(self.imagen, (x, y))


    def cazar(self, presa):
        if isinstance(presa, Animal) and presa != self:
            probabilidad_caza = random.uniform(0, 1)
            if probabilidad_caza > 0.5:  
                presa.morir()  
                self.energia += 10  

    def reproducir(self, pareja):
        
        if isinstance(pareja, Animal) and pareja.especie == self.especie and pareja != self:
            probabilidad_reproduccion = random.uniform(0, 1)
            if probabilidad_reproduccion > 0.7:  
                nueva_vida = (self.vida + pareja.vida) // 2
                nueva_energia = (self.energia + pareja.energia) // 2
                nueva_velocidad = (self.velocidad + pareja.velocidad) // 2
                nueva_posicion = [(self.posicion[0] + pareja.posicion[0]) // 2, (self.posicion[1] + pareja.posicion[1]) // 2]

                nuevo_animal = Animal(nueva_posicion, nueva_vida, nueva_energia, nueva_velocidad, self.especie, self.dieta)
                return nuevo_animal

        return None  

    def morir(self):
        self.vida = 0
        self.energia = 0



class Planta:
    def __init__(self, posicion, vida, energia, imagen_path, matriz_celda_size):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.sprite = pygame.image.load(imagen_path)

    def dibujar(self, screen, ancho_celda, alto_celda):
        planta_width, planta_height = self.sprite.get_size()
        escala_ancho = ancho_celda / planta_width
        escala_alto = alto_celda / planta_height

        nueva_ancho = int(planta_width * escala_ancho)
        nueva_alto = int(planta_height * escala_alto)

        planta_escalada = pygame.transform.scale(self.sprite, (nueva_ancho, nueva_alto))

        x = self.posicion[0] * ancho_celda
        y = self.posicion[1] * alto_celda

        screen.blit(planta_escalada, (x, y))

    def fotosintesis(self):
        self.energia += 5

    def reproducir(self):
        nueva_posicion = [self.posicion[0] + random.choice([-1, 0, 1]), self.posicion[1] + random.choice([-1, 0, 1])]
        nueva_vida = (self.vida + random.randint(0, 10)) // 2
        nueva_energia = (self.energia + random.randint(0, 5)) // 2
        nueva_velocidad = self.velocidad

        nueva_instancia = Planta(nueva_posicion, nueva_vida, nueva_energia, nueva_velocidad, self.tipo)
        return nueva_instancia

    def morir(self):
        self.posicion = [-1, -1]  

