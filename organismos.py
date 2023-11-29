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
        # Lógica para la caza de otra entidad
        if isinstance(presa, Animal) and presa != self:
            # El animal caza solo si la presa es un animal y no es él mismo
            probabilidad_caza = random.uniform(0, 1)
            if probabilidad_caza > 0.5:  # 50% de probabilidad de éxito en la caza
                presa.morir()  # La presa muere
                self.energia += 10  # El depredador gana energía por cazar

    def reproducir(self, pareja):
        # Lógica para la reproducción con otro animal
        if isinstance(pareja, Animal) and pareja.especie == self.especie and pareja != self:
            probabilidad_reproduccion = random.uniform(0, 1)
            if probabilidad_reproduccion > 0.7:  # 70% de probabilidad de reproducción exitosa
                # Creamos un nuevo animal con características promedio de ambos padres
                nueva_vida = (self.vida + pareja.vida) // 2
                nueva_energia = (self.energia + pareja.energia) // 2
                nueva_velocidad = (self.velocidad + pareja.velocidad) // 2
                nueva_posicion = [(self.posicion[0] + pareja.posicion[0]) // 2, (self.posicion[1] + pareja.posicion[1]) // 2]

                nuevo_animal = Animal(nueva_posicion, nueva_vida, nueva_energia, nueva_velocidad, self.especie, self.dieta)
                return nuevo_animal

        return None  # No se reproduce si la pareja no es del mismo tipo o si es él mismo

    def morir(self):
        # Lógica para la muerte del animal
        self.vida = 0
        self.energia = 0



class Planta(Organismo):
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

