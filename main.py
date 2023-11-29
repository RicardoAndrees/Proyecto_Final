import pygame
from display import InterfazGrafica
<<<<<<< HEAD
from organismos import Animal
from ambiente import Ambiente
=======
from organismos import Animal, Planta
>>>>>>> 6ed6f3c7dd557cca632736c88b3047508ccd537f

def main():
    pygame.init()

    tiburon = Animal(posicion=[1, 11], vida=100, energia=50, velocidad=1, especie="Tiburón", dieta="Peces", imagen_path="tiburon.png")
    pez = Animal(posicion=[5, 13], vida=80, energia=40, velocidad=1, especie="Pez", dieta="Algas", imagen_path="pez.png")
    planta1 = Planta(posicion=[1, 5], vida=10, energia=10, velocidad=0, imagen_path="brote.PNG")

    organismos = [tiburon, pez]
    matriz_celdas = [[None for _ in range(15)] for _ in range(15)]  
    
    matriz_celdas = [[None for _ in range(15)] for _ in range(15)] 
    ambiente = Ambiente(matriz_celdas, organismos)
    
    interfaz = InterfazGrafica()
    interfaz.organismos = organismos
    interfaz.ejecutar_interfaz()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ambiente.ejecutar_ciclo() 
        interfaz.mover_sprites_aleatoriamente()
        interfaz.mover_organismos_aleatoriamente()
        interfaz.dibujar_ecosistema()
        pygame.display.flip()

if __name__ == "__main__":
    main()
