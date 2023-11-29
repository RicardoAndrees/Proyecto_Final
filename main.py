import pygame
from display import InterfazGrafica
from organismos import Animal
from ambiente import Ambiente
from organismos import Animal, Planta


def main():
    pygame.init()

    tiburon = Animal(posicion=[1, 11], vida=100, energia=50, velocidad=1, especie="Tiburón", dieta="Peces", imagen_path="tiburon.png")
    pez = Animal(posicion=[5, 13], vida=80, energia=40, velocidad=1, especie="Pez", dieta="Algas", imagen_path="pez.png")

    organismos = [tiburon, pez]
    matriz_celdas = [[None for _ in range(15)] for _ in range(15)]  
    
    ambiente = Ambiente(matriz_celdas, organismos)
    
    interfaz = InterfazGrafica()
    interfaz.organismos = organismos
    interfaz.ejecutar_interfaz()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        ambiente.ejecutar_ciclo() 
        interfaz.mover_sprites_aleatoriamente()
        interfaz.mover_organismos_aleatoriamente()
        interfaz.dibujar_ecosistema()
        pygame.display.flip()

if __name__ == "__main__":
    main()
