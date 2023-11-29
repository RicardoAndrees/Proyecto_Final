# main.py

import pygame
from interfaz_grafica import InterfazGrafica
from animal import Animal

if __name__ == "__main__":
    pygame.init()

    tiburon = Animal((1, 2), 100, 80, 5, "Gran Tiburón Blanco", "Peces y mamíferos marinos")
    

    interfaz = InterfazGrafica()
    interfaz.ejecutar_interfaz()
