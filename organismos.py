import pygame
from itertools import product


class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

    def moverse(self, direccion, matriz_espacial):
        dx, dy = direccion
        nueva_posicion = (self.posicion[0] + dx, self.posicion[1] + dy)

        if (
            0 <= nueva_posicion[0] < matriz_espacial.filas and
            0 <= nueva_posicion[1] < matriz_espacial.columnas
        ):
            matriz_espacial.mover_organismo(self, nueva_posicion)

    def reproducirse(self, pareja, matriz_espacial, atributos_adicionales=None):
        if atributos_adicionales is None:
            atributos_adicionales = {}
        nueva_posicion = matriz_espacial.encontrar_posicion_disponible(self.posicion)
        nuevos_atributos = {
            'posicion': nueva_posicion,
            'vida': 50,
            'energia': 50,
            'velocidad': 5,
            **atributos_adicionales
        }
        nuevo_organismo = self.__class__(**nuevos_atributos)
        matriz_espacial.agregar_organismo(nuevo_organismo)

    def morir(self, matriz_espacial):
        matriz_espacial.eliminar_organismo(self)

    def interactuar_con_entorno(self, ambiente):
        self.energia += self.energia * ambiente.factor_abiotico

    def envejecer(self):
        self.vida -= 1

    def esta_vivo(self):
        return self.vida > 0

class Animal(Organismo):
    def __init__(self, especie, dieta, posicion, vida, energia, velocidad, rol_trofico):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.rol_trofico = rol_trofico
        self.sprite = None

        especies_sprites = {
            "Tigre": "tigre.png",
            "Elefante": "elefante.png",
            "León": "leon.png",
            "Cocodrilo": "cocodrilo.png",
            "Conejo": "conejo.png",
            "Ciervo": "ciervo.png",
            "Cuervo": "cuervo.png",
            "Pez": "pez.png",
            "Tiburón": "tiburon.png",
            "Lagartija": "lagartija.png"
        }

        sprite_path = especies_sprites.get(self.especie)
        if sprite_path is not None:
            self.sprite = pygame.image.load(sprite_path)
            self.sprite = pygame.transform.scale(self.sprite, (20, 20))

    def cazar(self, presa, matriz_espacial):
        if isinstance(presa, Organismo) and presa != self and presa.vida > 0:
            presa.vida -= 10
            self.energia += 10

            if presa.vida <= 0:
                presa.morir(matriz_espacial)

    def interactuar_con_otro_organismo(self, otro_organismo, matriz_espacial):
        if isinstance(otro_organismo, Animal) and otro_organismo != self:
            if self.rol_trofico == "carnivoro" and otro_organismo.rol_trofico == "herbivoro":
                self.cazar(otro_organismo, matriz_espacial)
            elif self.rol_trofico == "herbivoro" and otro_organismo.rol_trofico == "planta":
                self.comer_planta(otro_organismo, matriz_espacial)
            elif self.rol_trofico == "omnivoro":
                if otro_organismo.rol_trofico == "herbivoro":
                    self.cazar(otro_organismo, matriz_espacial)
                elif otro_organismo.rol_trofico == "planta":
                    self.comer_planta(otro_organismo, matriz_espacial)

    def comer_planta(self, planta, matriz_espacial):
        planta.morir(matriz_espacial)
        self.energia += 20

    def calcular_distancia(self, posicion1, posicion2):
        return abs(posicion1[0] - posicion2[0]) + abs(posicion1[1] - posicion2[1])

    def reproducirse(self, pareja, matriz_espacial):
        if (
            pareja is not None and
            isinstance(pareja, Animal) and
            pareja.esta_vivo() and
            pareja.especie == self.especie 
        ):
            distancia_entre_animales = self.calcular_distancia(self.posicion, pareja.posicion)

            if distancia_entre_animales <= 1:  
                atributos_adicionales = {
                    'especie': self.especie,
                    'dieta': self.dieta,
                    'rol_trofico': self.rol_trofico
                }
                super().reproducirse(pareja, matriz_espacial, atributos_adicionales)

    def buscar_recurso(self, matriz_espacial):
        planta_cercana = None
        distancia_minima = float('inf')

        for organismo in matriz_espacial.organisms:
            if isinstance(organismo, Planta) and organismo.esta_vivo():
                distancia = abs(self.posicion[0] - organismo.posicion[0]) + abs(self.posicion[1] - organismo.posicion[1])
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    planta_cercana = organismo

        if planta_cercana:
            direccion = (planta_cercana.posicion[0] - self.posicion[0], planta_cercana.posicion[1] - self.posicion[1])
            self.moverse(direccion, matriz_espacial)
    def tomar_decision(self, matriz_espacial):

        if self.energia < 30:

            self.buscar_recurso(matriz_espacial)
        else:

            pareja = self.obtener_pareja()
            if pareja:
                self.reproducirse(pareja, matriz_espacial)

    def tomar_decision_avanzada(self, ecosistema):
        if hasattr(ecosistema, 'matriz_espacial') and ecosistema.matriz_espacial:
            for otro_organismo in ecosistema.matriz_espacial.organisms:
                if otro_organismo != self and isinstance(otro_organismo, Organismo) and otro_organismo.esta_vivo():
                    distancia = abs(self.posicion[0] - otro_organismo.posicion[0]) + abs(self.posicion[1] - otro_organismo.posicion[1])
                    if distancia < distancia_minima:
                        distancia_minima = distancia
                        organismo_cercano = otro_organismo

            if organismo_cercano:
                if isinstance(organismo_cercano, Planta):
                    self.buscar_recurso(ecosistema.matriz_espacial)
                elif isinstance(organismo_cercano, Animal):
                    if self.rol_trofico == "carnivoro" and organismo_cercano.rol_trofico == "herbivoro":
                        self.cazar(organismo_cercano, ecosistema.matriz_espacial)
                    elif self.rol_trofico == "herbivoro" and organismo_cercano.rol_trofico == "planta":
                        self.comer_planta(organismo_cercano, ecosistema.matriz_espacial)
                    elif self.rol_trofico == "omnivoro":
                        if organismo_cercano.rol_trofico == "herbivoro":
                            self.cazar(organismo_cercano, ecosistema.matriz_espacial)
                        elif organismo_cercano.rol_trofico == "planta":
                            self.comer_planta(organismo_cercano, ecosistema.matriz_espacial)

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad):
        super().__init__(posicion, vida, energia, velocidad)

    def realizar_fotosintesis(self, ambiente):
        self.energia += ambiente.factor_abiotico

    def reproducirse_por_semillas(self, matriz_espacial):
        nueva_posicion = matriz_espacial.encontrar_posicion_disponible(self.posicion)
        nuevo_organismo = Planta(nueva_posicion, vida=50, energia=50, velocidad=1)
        matriz_espacial.agregar_organismo(nuevo_organismo)
