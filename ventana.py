import pygame
import sys
import random

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
MARRON = (139, 69, 19)
AZUL = (0, 0, 255)

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

    def moverse(self, direccion, matriz_espacial):
        # Implementar el movimiento del organismo en función de su velocidad
        dx, dy = direccion
        nueva_posicion = (self.posicion[0] + dx, self.posicion[1] + dy)

        # Verificar que la nueva posición esté dentro de la matriz
        if 0 <= nueva_posicion[0] < matriz_espacial.filas and 0 <= nueva_posicion[1] < matriz_espacial.columnas:
            # Actualizar la posición del organismo en la matriz
            matriz_espacial.mover_organismo(self, nueva_posicion)

    def reproducirse(self, pareja, matriz_espacial):
        # Implementar la lógica de reproducción
        if isinstance(pareja, Organismo) and self.__class__ == pareja.__class__:
            # Crear un nuevo organismo y colocarlo en una posición cercana
            nueva_posicion = matriz_espacial.encontrar_posicion_disponible(self.posicion)
            nuevo_organismo = self.__class__(nueva_posicion, vida=50, energia=50, velocidad=5)
            matriz_espacial.agregar_organismo(nuevo_organismo)

    def morir(self, matriz_espacial):
        # Implementar la lógica de la muerte del organismo
        matriz_espacial.eliminar_organismo(self)
        # Puedes también simular el proceso de descomposición o liberar energía al entorno, según tus necesidades.

    def interactuar_con_entorno(self, ambiente):
        # Implementar la interacción del organismo con el ambiente
        # Por ejemplo, ajustar la energía del organismo según el factor abiótico del ambiente
        self.energia += ambiente.factor_abiotico
        
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

    def cazar(self, presa, matriz_espacial):
        # Implementación básica de la lógica de caza
        if isinstance(presa, Organismo) and presa != self and presa.vida > 0:
            presa.vida -= 10
            self.energia += 10

            # Lógica adicional, por ejemplo, manejo de muerte de la presa
            if presa.vida <= 0:
                presa.morir(matriz_espacial)

    def interactuar_con_otro_organismo(self, otro_organismo, matriz_espacial):
        # Implementación de interacciones tróficas
        if isinstance(otro_organismo, Animal) and otro_organismo != self:
            if self.rol_trofico == "carnivoro" and otro_organismo.rol_trofico == "herbivoro":
                # Carnívoros cazan herbívoros
                self.cazar(otro_organismo, matriz_espacial)
            elif self.rol_trofico == "herbivoro" and otro_organismo.rol_trofico == "planta":
                # Herbívoros se alimentan de plantas
                self.comer_planta(otro_organismo, matriz_espacial)
            elif self.rol_trofico == "omnivoro":
                # Omnívoros pueden cazar herbívoros y alimentarse de plantas
                if otro_organismo.rol_trofico == "herbivoro":
                    self.cazar(otro_organismo, matriz_espacial)
                elif otro_organismo.rol_trofico == "planta":
                    self.comer_planta(otro_organismo, matriz_espacial)

    def comer_planta(self, planta, matriz_espacial):
        # Implementación básica de la lógica de comer plantas
        planta.morir(matriz_espacial)  # Simula la planta siendo comida
        self.energia += 20  # Ajusta según tus necesidades

    def reproducirse(self, pareja, matriz_espacial):
        # Implementar la lógica de reproducción para animales
        if isinstance(pareja, Animal) and self.__class__ == pareja.__class__:
            # Crear un nuevo animal y colocarlo en una posición cercana
            nueva_posicion = matriz_espacial.encontrar_posicion_disponible(self.posicion)
            nuevo_animal = self.__class__(especie=self.especie, dieta=self.dieta, posicion=nueva_posicion, vida=50, energia=50, velocidad=5, rol_trofico=self.rol_trofico)
            matriz_espacial.agregar_organismo(nuevo_animal)
            
class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad):
        super().__init__(posicion, vida, energia, velocidad)

    def realizar_fotosintesis(self, ambiente):
        # Implementación básica de fotosíntesis
        self.energia += ambiente.factor_abiotico

    def reproducirse_por_semillas(self, matriz_espacial):
        # Implementación básica de reproducción por semillas
        nueva_posicion = matriz_espacial.encontrar_posicion_disponible(self.posicion)
        nuevo_organismo = Planta(nueva_posicion, vida=50, energia=50, velocidad=1)
        matriz_espacial.agregar_organismo(nuevo_organismo)
        
    def reproducirse(self, matriz_espacial):
        # Implementar la lógica de reproducción para plantas
        nueva_posicion = matriz_espacial.encontrar_posicion_disponible(self.posicion)
        nueva_planta = self.__class__(posicion=nueva_posicion, vida=50, energia=50, velocidad=1)
        matriz_espacial.agregar_organismo(nueva_planta)
        
class Ambiente:
    def __init__(self, factor_abiotico):
        self.factor_abiotico = factor_abiotico

    def afectar_ecosistema(self, ecosistema):
        # Lógica de afectar al ecosistema según el factor abiótico

        # Afectar la energía de los organismos en función del factor abiótico
        for organismo in ecosistema.organisms:
            organismo.energia += self.factor_abiotico * 10  # Ajusta según tus necesidades


    def generar_evento_climatico(self, ecosistema):
        # Genera un evento climático aleatorio
        evento_probabilidad = random.uniform(0, 1)

        # Si la probabilidad supera un umbral, desencadena un evento climático
        if evento_probabilidad > 0.8:
            # Puedes implementar lógica específica del evento, por ejemplo, afectar la velocidad de los organismos
            print("¡Evento climático!")

            # Aquí puedes agregar más lógica específica del evento climático
            # Por ejemplo, podrías reducir la velocidad de todos los organismos en un 50% durante el evento.
            for organismo in ecosistema.organisms:
                organismo.velocidad *= 0.5

    def interactuar_con_ecosistema(self, ecosistema):
        # Lógica específica de interacción del ambiente con el ecosistema
        self.afectar_ecosistema(ecosistema)
        self.generar_evento_climatico(ecosistema)

        # Ajusta otras variables del ecosistema según sea necesario
        # Por ejemplo, podrías cambiar la tasa de reproducción de organismos o introducir nuevos elementos en la matriz espacial

        # Ejemplo: Cambiar la tasa de reproducción de animales en función del factor abiótico
        nueva_tasa_reproduccion = 0.2 + 0.6 * self.factor_abiotico
        ecosistema.matriz_espacial.ciclo_de_vida.tasa_reproduccion = nueva_tasa_reproduccion

        # Puedes agregar más lógica según tus necesidades

class Ecosistema:
    def __init__(self, rows, cols):
        self.matriz_espacial = [[None for _ in range(cols)] for _ in range(rows)]
        self.organisms = []
        self.ambiente = Ambiente(factor_abiotico=0.5)  # Puedes ajustar el factor abiótico según tus necesidades

    def populate_ecosystem(self):
        # Colocar organismos iniciales en la matriz_espacial
        for _ in range(5):
            x = random.randint(0, len(self.matriz_espacial) - 1)
            y = random.randint(0, len(self.matriz_espacial[0]) - 1)
            nuevo_organismo = Animal(especie="Tigre", dieta="Carnívoro", posicion=(x, y), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")
            self.matriz_espacial[x][y] = nuevo_organismo
            self.organisms.append(nuevo_organismo)

    def run_cycle(self):
        # Ejecutar un ciclo del simulador

        # Realizar acciones para cada organismo en el ecosistema
        for organismo in self.organisms:
            # Verificar si el organismo sigue vivo y envejecer
            organismo.envejecer()
            if organismo.esta_vivo():
                # Interactuar con el entorno
                organismo.interactuar_con_entorno(ambiente=self.ambiente, matriz_espacial=self.matriz_espacial)

                # Moverse en una dirección aleatoria (puedes personalizar esto)
                direccion_aleatoria = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                organismo.moverse(direccion_aleatoria, matriz_espacial=self.matriz_espacial)

                # Realizar reproducción después de las interacciones y movimientos
                pareja = self.matriz_espacial.encontrar_pareja(organismo)
                if pareja:
                    organismo.reproducirse(pareja, matriz_espacial=self.matriz_espacial)

        # Actualizar la matriz espacial con los movimientos y reproducciones realizadas
        for organismo in self.organisms:
            self.matriz_espacial.mover_organismo(organismo, organismo.posicion)

        # Realizar eventos climáticos después de la reproducción
        self.ambiente.interactuar_con_ecosistema(self)

        # Ejecutar eventos del motor de eventos
        self.event_engine.execute_events()



# Ventana
class InterfazGrafica:
    def __init__(self, ecosistema):
        pygame.init()

        self.ecosistema = ecosistema
        self.screen_size = (736, 736)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Simulador de Ecosistemas")

        self.fondo = pygame.image.load("mapita.jpg")
        self.fondo = pygame.transform.scale(self.fondo, self.screen_size)

        self.meteorito_visible = False
        self.meteorito_timer = 0
        self.meteorito_delay = 5000  # Establece el tiempo en milisegundos para que el meteorito sea visible

    def actualizar_meteorito(self):
        # Actualiza el temporizador
        current_time = pygame.time.get_ticks()

        # Muestra el meteorito si ha pasado el tiempo establecido
        if current_time - self.meteorito_timer > self.meteorito_delay:
            self.meteorito_visible = True
            self.meteorito_timer = current_time

    def dibujar_ecosistema(self):
        self.screen.blit(self.fondo, (0, 0))

        # Dibujar organismos en la matriz
        for x in range(len(self.ecosistema.matriz_espacial)):
            for y in range(len(self.ecosistema.matriz_espacial[0])):
                organismo = self.ecosistema.matriz_espacial[x][y]
                if organismo:
                    self.screen.blit(organismo.image, (y * 50, x * 50))  # Ajusta según el tamaño de tus celdas

    def dibujar_panel_control(self):
        # Dibuja un fondo para el panel de control
        pygame.draw.rect(self.screen, NEGRO, (0, self.screen_size[1], self.screen_size[0], 50))

        # Muestra información sobre el estado actual del ecosistema
        font = pygame.font.Font(None, 36)
        texto_estado = font.render(f"Organismos: {len(self.ecosistema.organisms)}", True, BLANCO)
        self.screen.blit(texto_estado, (10, self.screen_size[1] + 10))

    def ejecutar_interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.ecosistema.organisms[0].moverse((0, -1), self.ecosistema.matriz_espacial)
            elif keys[pygame.K_DOWN]:
                self.ecosistema.organisms[0].moverse((0, 1), self.ecosistema.matriz_espacial)
            elif keys[pygame.K_LEFT]:
                self.ecosistema.organisms[0].moverse((-1, 0), self.ecosistema.matriz_espacial)
            elif keys[pygame.K_RIGHT]:
                self.ecosistema.organisms[0].moverse((1, 0), self.ecosistema.matriz_espacial)

            # Actualizar el ecosistema
            self.ecosistema.run_cycle()

            # Actualizar el meteorito
            self.actualizar_meteorito()

            # Dibujar el bioma y los organismos
            self.dibujar_ecosistema()

            # Dibujar el panel de control
            self.dibujar_panel_control()

            pygame.display.flip()
            self.clock.tick(10)

# Eventos
# Eventos
# Eventos
class MotorEventos:
    def __init__(self, ecosistema):
        self.events = []
        self.ecosistema = ecosistema

    def add_event(self, event):
        self.events.append(event)

    def execute_events(self):
        for event in self.events:
            if isinstance(event, EventoMeteorito):
                # Ejecutar acciones relacionadas con la llegada de un meteorito
                print("¡Ha llegado un meteorito al ecosistema!")
                # Puedes agregar más lógica aquí según sea necesario
            elif isinstance(event, EventoCambioEstacional):
                event.ejecutar_acciones(self.ecosistema)  # Pasamos el ecosistema como argumento
                # Puedes agregar más eventos específicos aquí según sea necesario
            # Agregar más bloques elif para otros tipos de eventos

        # Limpiar la lista de eventos después de ejecutarlos
        self.events = []


class EventoCambioEstacional:
    def __init__(self, nueva_tasa_reproduccion):
        self.nueva_tasa_reproduccion = nueva_tasa_reproduccion

    def ejecutar_acciones(self, ecosistema):
        # Aquí puedes implementar las acciones que se deben ejecutar cuando ocurre el cambio estacional
        print("¡Cambio estacional! Ajustando la tasa de reproducción de los organismos.")

        # Ajustar la tasa de reproducción de los organismos en el ecosistema
        for organismo in ecosistema.organisms:
            if hasattr(organismo, "tasa_reproduccion"):
                organismo.tasa_reproduccion = self.nueva_tasa_reproduccion
            # Puedes agregar más lógica aquí según tus necesidades




# Definir un evento específico (por ejemplo, EventoMeteorito)
# Definir un evento específico (por ejemplo, EventoMeteorito)
class EventoMeteorito:
    def __init__(self, posicion_impacto):
        self.posicion_impacto = posicion_impacto

    def ejecutar_acciones(self, ecosistema):
        # Aquí puedes implementar las acciones que se deben ejecutar cuando ocurre el evento del meteorito
        print(f"¡Un meteorito ha impactado en la posición {self.posicion_impacto}!")

        # Puedes agregar más lógica aquí, como afectar organismos en esa posición, etc.
        # Por ejemplo, podrías eliminar organismos en esa posición o reducir su vida/energía significativamente.
        organismo_afectado = ecosistema.matriz_espacial[self.posicion_impacto[0]][self.posicion_impacto[1]]
        if organismo_afectado:
            organismo_afectado.vida -= 20  # Reducción de la vida como ejemplo
            organismo_afectado.energia -= 30
            if organismo_afectado.energia <= 0:
                # Eliminar el organismo si su energía llega a cero o menos
                ecosistema.matriz_espacial[organismo_afectado.posicion[0]][organismo_afectado.posicion[1]] = None

                # Puedes agregar más acciones aquí, como generar eventos adicionales o propagar efectos en cascada



# Ecosistema
# Define las clases y funciones anteriores aquí


# Sprite

            
if __name__ == "__main__":
    pygame.init()
    ecosistema = Ecosistema(rows=10, cols=10)
    ecosistema.populate_ecosystem()

    interfaz = InterfazGrafica(ecosistema)

    # Crear una instancia del MotorEventos y pasar el ecosistema
    motor_eventos = MotorEventos(ecosistema)

    # Crear un carnívoro
# Crear un carnívoro
    carnivoro = Animal(especie="León", dieta="Carnívoro", posicion=(0, 0), vida=50, energia=50, velocidad=5, rol_trofico="carnivoro")

# Crear un herbívoro
    herbivoro = Animal(especie="Ciervo", dieta="Herbívoro", posicion=(0, 1), vida=50, energia=50, velocidad=5, rol_trofico="herbivoro")

# Crear un omnívoro
    omnivoro = Animal(especie="Oso", dieta="Omnívoro", posicion=(1, 0), vida=50, energia=50, velocidad=5, rol_trofico="omnivoro")


    # Crear una instancia del MotorEventos en algún lugar de tu código principal
    motor_eventos = MotorEventos(ecosistema)

    # Desencadenar un cambio estacional (puedes ajustar la nueva tasa de reproducción según tus necesidades)
    evento_cambio_estacional = EventoCambioEstacional(nueva_tasa_reproduccion=0.1)
    motor_eventos.add_event(evento_cambio_estacional)

    # Desencadenar un evento de meteorito (puedes ajustar la posición del impacto según tus necesidades)
    evento_meteorito = EventoMeteorito(posicion_impacto=(2, 2))
    motor_eventos.add_event(evento_meteorito)

    # Luego, en tu bucle principal, ejecutas los eventos
    motor_eventos.execute_events()
