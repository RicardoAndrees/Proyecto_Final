import pygame
import sys
import random
from itertools import product

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

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

# Agregar esta función a la clase Animal
    def calcular_distancia(self, posicion1, posicion2):
        return abs(posicion1[0] - posicion2[0]) + abs(posicion1[1] - posicion2[1])

    # Modificar esta función en la clase Animal
    def reproducirse(self, pareja, matriz_espacial):
        if (
            pareja is not None and
            isinstance(pareja, Animal) and
            pareja.esta_vivo() and
            pareja.especie == self.especie  # Solo se reproducen animales de la misma especie
        ):
            distancia_entre_animales = self.calcular_distancia(self.posicion, pareja.posicion)

            if distancia_entre_animales <= 1:  # Solo se reproducen si están adyacentes
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
        # Tomar decisiones basadas en el entorno
        if self.energia < 30:
            # Si la energía es baja, buscar un recurso
            self.buscar_recurso(matriz_espacial)
        else:
            # Si la energía es suficiente, intentar reproducirse
            pareja = self.obtener_pareja()
            if pareja:
                self.reproducirse(pareja, matriz_espacial)

# Agregar esta función a la clase Animal
    def tomar_decision_avanzada(self, matriz_espacial):
        organismo_cercano = None
        distancia_minima = float('inf')

        for otro_organismo in matriz_espacial.organisms:
            if otro_organismo != self and isinstance(otro_organismo, Organismo) and otro_organismo.esta_vivo():
                distancia = abs(self.posicion[0] - otro_organismo.posicion[0]) + abs(self.posicion[1] - otro_organismo.posicion[1])
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    organismo_cercano = otro_organismo

        if organismo_cercano:
            if isinstance(organismo_cercano, Planta):
                self.buscar_recurso(matriz_espacial)
            elif isinstance(organismo_cercano, Animal):
                if self.rol_trofico == "carnivoro" and organismo_cercano.rol_trofico == "herbivoro":
                    self.cazar(organismo_cercano, matriz_espacial)
                elif self.rol_trofico == "herbivoro" and organismo_cercano.rol_trofico == "planta":
                    self.comer_planta(organismo_cercano, matriz_espacial)
                elif self.rol_trofico == "omnivoro":
                    if organismo_cercano.rol_trofico == "herbivoro":
                        self.cazar(organismo_cercano, matriz_espacial)
                    elif organismo_cercano.rol_trofico == "planta":
                        self.comer_planta(organismo_cercano, matriz_espacial)


class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad):
        super().__init__(posicion, vida, energia, velocidad)

    def realizar_fotosintesis(self, ambiente):
        self.energia += ambiente.factor_abiotico

    def reproducirse_por_semillas(self, matriz_espacial):
        nueva_posicion = matriz_espacial.encontrar_posicion_disponible(self.posicion)
        nuevo_organismo = Planta(nueva_posicion, vida=50, energia=50, velocidad=1)
        matriz_espacial.agregar_organismo(nuevo_organismo)

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

class Ecosistema:
    def __init__(self, rows, cols, ambientes, size):
        self.matriz_espacial = MatrizEspacial(filas=rows, columnas=cols)
        self.organisms = []
        self.rows = rows
        self.cols = cols
        self.ambientes = ambientes
        self.size = size
        self.seccion_actual = 0

    def add_organism(self, organism):
        self.organisms.append(organism)
        self.matriz_espacial.agregar_organismo(organism)

    def dibujar_ecosistema(self, screen, seccion_actual):
        for organismo in self.organisms:
            x, y = organismo.posicion
            if isinstance(organismo, Animal) and hasattr(organismo, 'sprite') and organismo.sprite is not None:
                sprite = organismo.sprite
                if hasattr(sprite, 'get_size'):
                    sprite_size = sprite.get_size()
                    screen.blit(sprite, (y * 20, x * 20 + seccion_actual * self.size[1] // 3))
            else:
                sprite = pygame.image.load("arbolito.png")
                sprite = pygame.transform.scale(sprite, (20, 20))
                screen.blit(sprite, (y * 20, x * 20 + seccion_actual * self.size[1] // 3))

    def dibujar_fondos(self, screen):
        for seccion_actual, ambiente in enumerate(self.ambientes):
            seccion_height = self.size[1] // 3
            seccion_rect = pygame.Rect(0, seccion_actual * seccion_height, self.size[0], seccion_height)
            
            if seccion_actual == 0:  # Primera sección
                ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect)
            else:  # Segunda y tercera sección
                if seccion_actual == 1:
                    ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect)
                elif seccion_actual == 2:
                    # Ajusta el rectángulo para dividir en dos a lo ancho
                    seccion_rect_left = pygame.Rect(0, seccion_actual * seccion_height, self.size[0] // 2, seccion_height)
                    ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect_left)
                    
                    seccion_rect_right = pygame.Rect(self.size[0] // 2, seccion_actual * seccion_height, self.size[0] // 2, seccion_height)
                    ambiente.dibujar_fondo(screen, seccion_actual, seccion_rect_right)
    def populate_ecosystem(self):
        for _ in range(10):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            nuevo_organismo = Animal(especie="Tigre", dieta="Carnívoro", posicion=(x, y), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")
            self.add_organism(nuevo_organismo)

        for _ in range(10):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            nueva_planta = Planta(posicion=(x, y), vida=50, energia=50, velocidad=1)
            self.add_organism(nueva_planta)


    def run_cycle(self):
        for organismo in self.organisms:
            organismo.interactuar_con_entorno(self.ambientes[self.seccion_actual])
            organismo.moverse(self.obtener_direccion(), self.matriz_espacial)
            organismo.envejecer()
            organismo.energia -= 1

            if organismo.esta_vivo():
                pareja = self.obtener_pareja(organismo)
                organismo.reproducirse(pareja, self.matriz_espacial)
            if not organismo.esta_vivo():
                self.organisms.remove(organismo)

    def obtener_pareja(self, organismo):
        candidatos = [
            o for o in self.organisms
            if o != organismo and isinstance(o, organismo.__class__) and o.esta_vivo()
        ]

        if candidatos:
            return random.choice(candidatos)
        return None

    def obtener_direccion(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class MatrizEspacial:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[None] * columnas for _ in range(filas)]

    def agregar_organismo(self, organismo):
        x, y = organismo.posicion
        self.matriz[x][y] = organismo

    def eliminar_organismo(self, organismo):
        x, y = organismo.posicion
        self.matriz[x][y] = None

    def mover_organismo(self, organismo, nueva_posicion):
        x, y = organismo.posicion
        nuevo_x, nuevo_y = nueva_posicion

        self.matriz[x][y] = None
        self.matriz[nuevo_x][nuevo_y] = organismo
        organismo.posicion = nueva_posicion

    def obtener_organismo_en_posicion(self, posicion):
        x, y = posicion
        return self.matriz[x][y]

    def encontrar_posicion_disponible(self, posicion_inicial):
        x, y = posicion_inicial

        for dx, dy in product([-1, 0, 1], repeat=2):
            nueva_x, nueva_y = x + dx, y + dy
            if 0 <= nueva_x < self.filas and 0 <= nueva_y < self.columnas and self.matriz[nueva_x][nueva_y] is None:
                return nueva_x, nueva_y

        return x, y

def main():
    size = (1370, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ecosistema Simulado")

    bosque_fondo = "mapa.png"
    arbolito_path = "arbolito.png"

    bosque = Ambiente(factor_abiotico=0.1, fondo_path="bosque.png", size=size)
    desierto = Ambiente(factor_abiotico=0.05, fondo_path="fondo_desierto.png", size=size)
    acuatico = Ambiente(factor_abiotico=0.15, fondo_color=(0, 0, 255), size=size)

    ambientes = [bosque, desierto, acuatico]
    ecosistema = Ecosistema(rows=20, cols=20, ambientes=ambientes, size=size)
    ecosistema.populate_ecosystem()

    tigre = Animal(especie="Tigre", dieta="Carnívoro", posicion=(5, 5), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")
    elefante = Animal(especie="Elefante", dieta="Herbívoro", posicion=(7, 7), vida=50, energia=50, velocidad=3, rol_trofico="herbivoro")
    leon = Animal(especie="León", dieta="Carnívoro", posicion=(10, 10), vida=50, energia=50, velocidad=4, rol_trofico="carnivoro")
    cocodrilo = Animal(especie="Cocodrilo", dieta="Carnívoro", posicion=(12, 12), vida=50, energia=50, velocidad=6, rol_trofico="carnivoro")
    conejo = Animal(especie="Conejo", dieta="Herbívoro", posicion=(15, 15), vida=50, energia=50, velocidad=2, rol_trofico="herbivoro")
    ciervo = Animal(especie="Ciervo", dieta="Herbívoro", posicion=(3, 3), vida=50, energia=50, velocidad=3, rol_trofico="herbivoro")
    cuervo = Animal(especie="Cuervo", dieta="Omnívoro", posicion=(8, 8), vida=50, energia=50, velocidad=4, rol_trofico="omnivoro")
    pez = Animal(especie="Pez", dieta="Herbívoro", posicion=(2, 2), vida=50, energia=50, velocidad=2, rol_trofico="herbivoro")
    tiburon = Animal(especie="Tiburón", dieta="Carnívoro", posicion=(18, 18), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")
    lagartija = Animal(especie="Lagartija", dieta="Herbívoro", posicion=(16, 16), vida=50, energia=50, velocidad=3, rol_trofico="herbivoro")

    ecosistema.add_organism(tigre)
    ecosistema.add_organism(elefante)
    ecosistema.add_organism(leon)
    ecosistema.add_organism(cocodrilo)
    ecosistema.add_organism(conejo)
    ecosistema.add_organism(ciervo)
    ecosistema.add_organism(cuervo)
    ecosistema.add_organism(pez)
    ecosistema.add_organism(tiburon)
    ecosistema.add_organism(lagartija)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ecosistema.run_cycle()

        for animal in ecosistema.organisms:
            if isinstance(animal, Animal):
                animal.tomar_decision_avanzada(ecosistema.matriz_espacial)
                pareja = ecosistema.obtener_pareja(animal)
                animal.reproducirse(pareja, ecosistema.matriz_espacial)

        screen.fill((255, 255, 255))

        for seccion_actual in range(3):
            ecosistema.dibujar_fondos(screen)
            ecosistema.dibujar_ecosistema(screen, seccion_actual)

        pygame.display.flip()
        clock.tick(10)



    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
