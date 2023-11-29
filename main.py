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

    matriz_espacial = MatrizEspacial(filas=15, columnas=15)
    
    interfaz = InterfazGrafica(matriz_espacial)
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
