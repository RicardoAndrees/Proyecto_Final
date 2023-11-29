from ecosistema import Ecosistema
from motor_eventos import MotorEventos
from matriz_espacial import MatrizEspacial
from ambiente import Ambiente
from organismos import Animal, Planta
from display import InterfazGrafica
import pygame

def main():
    pygame.init()

    tiburon = Animal(posicion=[1, 11], vida=100, energia=50, velocidad=1, especie="Tiburón", dieta="Peces", imagen_path="tiburon.png")
    pez = Animal(posicion=[5, 13], vida=80, energia=40, velocidad=1, especie="Pez", dieta="Algas", imagen_path="pez.png")
    
    matriz_celda_size = (50, 50) 
    girasol = Planta(posicion=[3, 5], vida=50, energia=30, imagen_path="girasol.png", matriz_celda_size=matriz_celda_size)

    arbolito = Planta(posicion=[8, 10], vida=60, energia=40, imagen_path="arbolito.png", matriz_celda_size=matriz_celda_size)



    organismos = [tiburon, pez, girasol, arbolito]
    matriz_celdas = [[None for _ in range(15)] for _ in range(15)]  
    
    num_filas = 10
    num_columnas = 10
    intervalo_ciclico = 1
        
    matriz_espacial = MatrizEspacial(num_filas, num_columnas)
    motor_eventos = MotorEventos(intervalo_ciclico)
    ambiente = Ambiente(matriz_celdas, organismos)
    mi_ecosistema = Ecosistema(matriz_espacial, motor_eventos, ambiente)

    
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