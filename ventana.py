import pygame
import sys

#colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
MARRON = (139, 69, 19)
AZUL = (0, 0, 255)

#ventana
class InterfazGrafica:
    def __init__(self, ecosistema):
        pygame.init()

        self.ecosistema = ecosistema
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Simulador de Ecosistemas")

    def dibujar_ecosistema(self):
        pass

    def ejecutar_interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.dibujar_ecosistema()
            pygame.display.flip()

#eventos            
class MotorEventos:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        pass

    def execute_events(self):
        pass

class Ecosistema:
    def __init__(self, rows, cols):
        self.matriz_espacial = [[None for _ in range(cols)] for _ in range(rows)]
        self.event_engine = MotorEventos()
        self.organisms = []

    def populate_ecosystem(self):
        #colocar organismos iniciales en la matriz_espacial
        pass

    def run_cycle(self):
        #ejecutar un ciclo del simulador
        pass

if __name__ == "__main__":
    ecosistema = Ecosistema(rows=10, cols=10)
    ecosistema.populate_ecosystem()

    interfaz = InterfazGrafica(ecosistema)
    interfaz.ejecutar_interfaz()
