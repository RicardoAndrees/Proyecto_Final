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
        self.screen_size = (736, 736)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Simulador de Ecosistemas")

        self.fondo = pygame.image.load("mapita.jpg") 
        self.fondo = pygame.transform.scale(self.fondo, self.screen_size)

        self.sprite = Sprite((0, 0), "tigreso.jpg")

    def dibujar_ecosistema(self):
        self.screen.blit(self.fondo, (0, 0))
    
    def dibujar_sprite(self, sprite):
        self.screen.blit(sprite.image, sprite.rect)

    def ejecutar_interfaz(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.sprite.move('UP')
            elif keys[pygame.K_DOWN]:
                self.sprite.move('DOWN')
            elif keys[pygame.K_LEFT]:
                self.sprite.move('LEFT')
            elif keys[pygame.K_RIGHT]:
                self.sprite.move('RIGHT')

            self.dibujar_ecosistema()
            self.dibujar_sprite(self.sprite)
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

class Sprite(pygame.sprite.Sprite):
    def __init__(self, initial_position, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.speed = 1 
        self.image.set_colorkey((255, 255, 255))

    def move(self, direction):
        if direction == 'UP':
            self.rect.y -= self.speed
        elif direction == 'DOWN':
            self.rect.y += self.speed
        elif direction == 'LEFT':
            self.rect.x -= self.speed
        elif direction == 'RIGHT':
            self.rect.x += self.speed


if __name__ == "__main__":
    pygame.init()
    ecosistema = Ecosistema(rows=10, cols=10)
    ecosistema.populate_ecosystem()

    interfaz = InterfazGrafica(ecosistema)
    interfaz.ejecutar_interfaz()
