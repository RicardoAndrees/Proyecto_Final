# main.py
import pygame
from display import InterfazGrafica
from organismos import Animal

def main():
    pygame.init()

    # Crear instancias de la clase Animal con la ruta de la imagen del sprite
    tiburon = Animal(posicion=[1, 11], vida=100, energia=50, velocidad=1, especie="Tiburón", dieta="Peces", imagen_path="tiburon.png")
    pez = Animal(posicion=[5, 13], vida=80, energia=40, velocidad=1, especie="Pez", dieta="Algas", imagen_path="pez.png")

    # Agregar los organismos a la lista
    organismos = [tiburon, pez]

    # Crear la instancia de la interfaz gráfica
    interfaz = InterfazGrafica()
    interfaz.organismos = organismos
    # Ejecutar la interfaz gráfica
    interfaz.ejecutar_interfaz()

if __name__ == "__main__":
    main()
