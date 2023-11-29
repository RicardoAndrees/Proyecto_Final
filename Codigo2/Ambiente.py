# ambiente.py
import random

class Ambiente:
    def __init__(self):
        self.temperatura = 25 
        self.lluvia = 50 

    def simular_cambio_climatico(self):
        self.temperatura += random.uniform(-1, 1)  
        self.lluvia += random.uniform(-5, 5)  

        self.temperatura = max(0, min(40, self.temperatura)) 
        self.lluvia = max(0, min(100, self.lluvia)) 

    def obtener_estado_climatico(self):
        return f'Temperatura: {self.temperatura}°C, Nivel de lluvia: {self.lluvia}%'
