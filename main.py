import pygame
import sys
from display import InterfazGrafica
from matriz_espacial import MatrizEspacial
from organismos import Organismo, Animal, Planta

if __name__ == "__main__":
    pygame.init()

    matriz_espacial = MatrizEspacial(filas=15, columnas=15)
    
    interfaz = InterfazGrafica(matriz_espacial)
    interfaz.ejecutar_interfaz()


