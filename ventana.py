import pygame
import sys
import random

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
            **atributos_adicionales  # Agrega atributos adicionales aquí
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

        if self.especie == "Tigre":
            sprite_path = "Tigre.png"
        elif self.especie == "Elefante":
            sprite_path = "Elefante.png"
        elif self.especie == "León":
            sprite_path = "Leon.png"
        # Agrega las rutas para las otras especies aquí

        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (20, 20))  # Ajustar el tamaño según necesites


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

    # La función reproducirse no se sobrescribe aquí ya que no agrega ningún comportamiento adicional

class Ambiente:
    def __init__(self, factor_abiotico):
        self.factor_abiotico = factor_abiotico

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
    def __init__(self, rows, cols, ambiente):
        self.matriz_espacial = MatrizEspacial(filas=rows, columnas=cols)
        self.organisms = []
        self.rows = rows
        self.cols = cols
        self.ambiente = ambiente 

    def add_organism(self, organism):
        self.organisms.append(organism)

    def dibujar_ecosistema(self, screen):
        for organismo in self.organisms:
            x, y = organismo.posicion
            if isinstance(organismo, Animal):
                sprite = organismo.sprite
            else:
                sprite = pygame.image.load("arbolito.png")  # Cambia "planta_sprite.png" con tu imagen de planta
                sprite = pygame.transform.scale(sprite, (20, 20))  # Ajusta el tamaño según necesites

            screen.blit(sprite, (y * 20, x * 20))

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
            organismo.interactuar_con_entorno(self.ambiente)
            organismo.envejecer()
            organismo.energia -= 1

            if organismo.esta_vivo():
                pareja = self.obtener_pareja(organismo)
                organismo.reproducirse(pareja, self.matriz_espacial)
                organismo.moverse(self.obtener_direccion(), self.matriz_espacial)

                # Verifica si el organismo es un Animal antes de llamar a interactuar_con_otro_organismo
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
        posiciones_disponibles = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]
        posiciones_disponibles = [(x, y) for x, y in posiciones_disponibles if 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0])]
        posiciones_disponibles = [pos for pos in posiciones_disponibles if self.matriz[pos[0]][pos[1]] is None]
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
# ... (código anterior)

def main():
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ecosistema Simulado")

    ambiente = Ambiente(factor_abiotico=0.1)
    ecosistema = Ecosistema(rows=20, cols=20, ambiente=ambiente)
    ecosistema.populate_ecosystem()

    # Crear instancias de animales y plantas y agregarlas al ecosistema
    tigre = Animal(especie="Tigre", dieta="Carnívoro", posicion=(5, 5), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")
    elefante = Animal(especie="Elefante", dieta="Herbívoro", posicion=(7, 7), vida=50, energia=50, velocidad=3, rol_trofico="herbivoro")
    leon = Animal(especie="León", dieta="Carnívoro", posicion=(10, 10), vida=50, energia=50, velocidad=4, rol_trofico="carnivoro")
   
    ecosistema.add_organism(tigre)
    ecosistema.add_organism(elefante)
    ecosistema.add_organism(leon)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Aquí puedes agregar lógica para manejar eventos de teclado si es necesario
                pass

        ecosistema.run_cycle()

        screen.fill(NEGRO)

        # Llama a la función para dibujar el ecosistema
        ecosistema.dibujar_ecosistema(screen)

        pygame.display.flip()
        clock.tick(10)  # Ajusta la velocidad de la simulación

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
