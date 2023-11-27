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
        
        sprite_path = None 
 
        if self.especie == "Tigre":
            sprite_path = "Tigre.png"
        elif self.especie == "Elefante":
            sprite_path = "Elefante.png"
        elif self.especie == "León":
            sprite_path = "Leon.png"
        elif self.especie == "Cocodrilo":
            sprite_path = "Cocodrilo.png"
        elif self.especie == "Conejo":
            sprite_path = "Conejo.png"
        elif self.especie == "Ciervo":
            sprite_path = "Ciervo.png"
        elif self.especie == "Cuervo":
            sprite_path = "Cuervo.png"
        elif self.especie == "Pez":
            sprite_path = "Pez.png"
        elif self.especie == "Tiburon":
            sprite_path = "Tiburon.png"
        elif self.especie == "Lagartija":
            sprite_path = "Lagartija.png"

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

    def reproducirse(self, pareja, matriz_espacial):
        atributos_adicionales = {
            'especie': self.especie,
            'dieta': self.dieta,
            'rol_trofico': self.rol_trofico
        }
        super().reproducirse(pareja, matriz_espacial, atributos_adicionales)

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
    def __init__(self, factor_abiotico, fondo_color=None, fondo_path=None, arbolito_path=None, size=None):
        self.factor_abiotico = factor_abiotico
        self.fondo_color = fondo_color
        self.fondo_path = fondo_path
        self.size = size
        self.seccion_actual = 0

        if self.size:
            if self.fondo_color:
                self.fondo = pygame.Surface(self.size)
                self.fondo.fill(self.fondo_color)
            elif self.fondo_path:
                self.fondo = pygame.image.load(self.fondo_path)
                self.fondo = pygame.transform.scale(self.fondo, self.size)
        else:
            self.fondo = None  
        self.arbolito_path = arbolito_path
        self.arbolitos = self.cargar_arbolitos(size)
    



    def cargar_arbolitos(self, size):
        arbolitos = []
        if self.arbolito_path:
            arbolito_img = pygame.image.load(self.arbolito_path)
            arbolito_img = pygame.transform.scale(arbolito_img, (20, 20))  
            for _ in range(5):  
                x = random.randint(0, size[0] - 20)
                y = random.randint(0, size[1] - 20)
                arbolitos.append((arbolito_img, (x, y)))
        return arbolitos
    
    def dibujar_fondo(self, screen, seccion_actual):
        seccion_height = self.size[1] // 3
        seccion_rect = pygame.Rect(0, seccion_actual * seccion_height, self.size[0], seccion_height)

        if self.fondo:
            screen.blit(self.fondo, (0, seccion_actual * seccion_height), seccion_rect)

        for arbolito_img, (x, y) in self.arbolitos:
            screen.blit(arbolito_img, (x, y + seccion_actual * seccion_height))

            
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
        for seccion_actual in range(3):
            seccion_height = self.size[1] // 3
            seccion_rect = pygame.Rect(0, seccion_actual * seccion_height, self.size[0], seccion_height)

            self.ambiente_bosque.dibujar_fondo(screen, seccion_actual)
            self.ambiente_desierto.dibujar_fondo(screen, seccion_actual)
            self.ambiente_acuatico.dibujar_fondo(screen, seccion_actual)

            for arbolito_img, (x, y) in self.ambiente_acuatico.arbolitos:
                screen.blit(arbolito_img, (x, y + seccion_actual * seccion_height))

    def populate_ecosystem(self):
        for _ in range(10):
            x = random.randint(0, len(self.matriz_espacial.matriz) - 1)
            y = random.randint(0, len(self.matriz_espacial.matriz[0]) - 1)
            nuevo_organismo = Animal(especie="Tigre", dieta="Carnívoro", posicion=(x, y), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")
            self.add_organism(nuevo_organismo)

        for _ in range(10):
            x = random.randint(0, len(self.matriz_espacial.matriz) - 1)
            y = random.randint(0, len(self.matriz_espacial.matriz[0]) - 1)
            nueva_planta = Planta(posicion=(x, y), vida=50, energia=50, velocidad=1)
            self.add_organism(nueva_planta)


    def run_cycle(self):
        for organismo in self.organisms:
            organismo.interactuar_con_entorno(self.ambientes[self.seccion_actual])
            organismo.envejecer()
            organismo.energia -= 1

            if organismo.esta_vivo():
                pareja = self.obtener_pareja(organismo)
                organismo.reproducirse(pareja, self.matriz_espacial)
                organismo.moverse(self.obtener_direccion(), self.matriz_espacial)

                if isinstance(organismo, Animal):
                    organismo.interactuar_con_otro_organismo(self.obtener_objetivo(organismo), self.matriz_espacial)
            else:
                organismo.morir(self.matriz_espacial)

        self.matriz_espacial.ciclo_de_vida()
        self.matriz_espacial.ciclo_de_vida()
        
    def obtener_pareja(self, organismo):
        posibles_parejas = [o for o in self.organisms if isinstance(o, organismo.__class__) and o != organismo]
        return random.choice(posibles_parejas) if posibles_parejas else None

    def obtener_objetivo(self, organismo):
        if isinstance(organismo, Animal):
            return self.matriz_espacial.obtener_organismo_en_posicion(organismo.posicion)
        elif isinstance(organismo, Planta):
            return random.choice([o for o in self.organisms if isinstance(o, Animal)])

    def obtener_direccion(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class MatrizEspacial:
    def __init__(self, filas, columnas):
        self.matriz = [[None for _ in range(columnas)] for _ in range(filas)]
        self.filas = filas
        self.columnas =columnas
        
    def agregar_organismo(self, organismo):
        if organismo is not None and organismo.posicion is not None:
            x, y = organismo.posicion
            self.matriz[x][y] = organismo

    def eliminar_organismo(self, organismo):
        x, y = organismo.posicion
        self.matriz[x][y] = None

    def obtener_organismo_en_posicion(self, posicion):
        x, y = posicion
        return self.matriz[x][y]

    def mover_organismo(self, organismo, nueva_posicion):
        antigua_posicion = organismo.posicion
        self.matriz[antigua_posicion[0]][antigua_posicion[1]] = None
        self.matriz[nueva_posicion[0]][nueva_posicion[1]] = organismo
        organismo.posicion = nueva_posicion

    def encontrar_posicion_disponible(self, posicion):
        x, y = posicion
        posiciones_disponibles = [
            (x + dx, y + dy) for dx, dy in product([-1, 0, 1], repeat=2) 
            if 0 <= x + dx < len(self.matriz) and 0 <= y + dy < len(self.matriz[0])
        ]
        posiciones_disponibles = [
            pos for pos in posiciones_disponibles if not isinstance(self.matriz[pos[0]][pos[1]], Organismo)
        ]
        return random.choice(posiciones_disponibles) if posiciones_disponibles else None
    
    def ciclo_de_vida(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                organismo = self.matriz[i][j]
                if organismo is not None:
                    organismo.envejecer()
                    organismo.energia -= 1

                    if not organismo.esta_vivo():
                        organismo.morir(self)

                    if isinstance(organismo, Planta) and organismo.energia % 10 == 0:
                        organismo.reproducirse_por_semillas(self)
                        
def main():
    size = (1370, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ecosistema Simulado")
    
    bosque_fondo = "mapa.png"
    arbolito_path = "arbolito.png" 

    bosque = Ambiente(factor_abiotico=0.1, fondo_color=(0, 128, 0), arbolito_path=arbolito_path, size=size)
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
    lagartija = Animal(especie="Lagartija", dieta="Herbívoro", posicion=(14, 14), vida=50, energia=50, velocidad=2, rol_trofico="herbivoro")

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
    seccion_actual = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ecosistema.run_cycle()
        screen.fill((255, 255, 255))
    
        for seccion_actual, ambiente in enumerate(ecosistema.ambientes):
            ecosistema.dibujar_ecosistema(screen, seccion_actual)
            ambiente.dibujar_fondo(screen, seccion_actual)

        pygame.display.flip()

        clock.tick(10)


    pygame.quit()
    sys.exit()

    
if __name__ == "__main__":
    main()
