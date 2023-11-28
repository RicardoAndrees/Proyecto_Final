import pygame
import sys
from display import InterfazGrafica
from matriz_espacial import MatrizEspacial
from organismos import Organismo, Animal, Planta

if __name__ == "__main__":
    pygame.init()

    # Crear una instancia de MatrizEspacial
    matriz_espacial = MatrizEspacial(filas=15, columnas=15)

    # Inicializar la interfaz gráfica con la matriz espacial
    interfaz = InterfazGrafica(matriz_espacial)
    interfaz.ejecutar_interfaz()


