import pygame
import sys
from ecosistema import Ecosistema
from organismos import Animal, Planta
from ambiente import Ambiente

def main():
    size = (1370, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ecosistema Simulado")

    bosque_fondo = "mapa.png"
    arbolito_path = "arbolito.png"

    bosque = Ambiente(factor_abiotico=0.1, fondo_path="pasto.png", size=size)
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
