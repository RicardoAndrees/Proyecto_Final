import pygame
from display import InterfazGrafica
from organismos import Animal, Planta

def main():
    pygame.init()

    tiburon = Animal(posicion=[1, 11], vida=100, energia=50, velocidad=1, especie="Tiburón", dieta="Peces", imagen_path="tiburon.png")
    pez = Animal(posicion=[5, 13], vida=80, energia=40, velocidad=1, especie="Pez", dieta="Algas", imagen_path="pez.png")
    planta1 = Planta(posicion=[1, 5], vida=10, energia=10, velocidad=0, imagen_path="brote.PNG")

    organismos = [tiburon, pez]
    interfaz = InterfazGrafica()
    interfaz.organismos = organismos
    interfaz.ejecutar_interfaz()

if __name__ == "__main__":
    main()
