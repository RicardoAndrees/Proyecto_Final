from ecosistema import Ecosistema
from registro_eventos import RegistroEventos
from matriz_espacial import MatrizEspacial
from ambiente import Ambiente
from organismos import Animal, Planta
from display import InterfazGrafica
import pygame

def main():
    pygame.init()

    tiburon = Animal(posicion=[2, 10], vida=100, energia=50, velocidad=1, especie="Tiburón", dieta="Peces", imagen_path="tiburon.png")
    pez = Animal(posicion=[5, 11], vida=80, energia=40, velocidad=1, especie="Pez", dieta="Algas", imagen_path="pez.png")
    
    matriz_celda_size = (50, 50) 
    girasol = Planta(posicion=[1, 1], vida=50, energia=30, imagen_path="girasol.png", matriz_celda_size=matriz_celda_size)
    arbolito = Planta(posicion=[3, 7], vida=50, energia=30, imagen_path="arbolito.png", matriz_celda_size=matriz_celda_size)
    lechuga = Planta(posicion=[6, 4], vida=50, energia=30, imagen_path="lechuga.png", matriz_celda_size=matriz_celda_size)
    abedul = Planta(posicion=[8, 8], vida=50, energia=30, imagen_path="abedul.png", matriz_celda_size=matriz_celda_size)
    mariajuana = Planta(posicion=[10, 2], vida=50, energia=30, imagen_path="mariajuana.png", matriz_celda_size=matriz_celda_size)

    organismos = [tiburon, pez, girasol, arbolito, lechuga, abedul, mariajuana]

    matriz_celdas = [[None for _ in range(15)] for _ in range(15)]  
    
    num_filas = 10
    num_columnas = 10
    intervalo_ciclico = 1
        
    matriz_espacial = MatrizEspacial(num_filas, num_columnas)
    registro_eventos = RegistroEventos()
    ambiente = Ambiente(matriz_celdas, organismos)
    mi_ecosistema = Ecosistema(matriz_espacial, registro_eventos, ambiente)

    
    interfaz = InterfazGrafica()
    interfaz.organismos = organismos
    interfaz.ejecutar_interfaz()
    
    return mi_ecosistema, sistema_monitoreo, herramientas_analisis, interfaz, ambiente

if __name__ == "__main__":
    mi_ecosistema, sistema_monitoreo, herramientas_analisis, interfaz, ambiente = main()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        ambiente.ejecutar_ciclo()
        interfaz.mover_sprites_aleatoriamente()
        interfaz.mover_organismos_aleatoriamente()
        interfaz.dibujar_ecosistema()
        pygame.display.flip()