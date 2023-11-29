import time
import random

class MotorEventos:
    def __init__(self, intervalo_ciclico):
        self.intervalo_ciclico = intervalo_ciclico
        self.tiempo_ultimo_ciclo = time.time()

    def realizar_ciclo(self):
        tiempo_actual = time.time()
        if tiempo_actual - self.tiempo_ultimo_ciclo > self.intervalo_ciclico:
            print("Realizando acciones cíclicas...")
            self.tiempo_ultimo_ciclo = tiempo_actual

    def generar_evento_aleatorio(self):
        probabilidad_evento = random.uniform(0, 1)
        if probabilidad_evento > 0.8:
            print("Se generó un evento aleatorio!")
