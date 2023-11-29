import random
from organismos import Animal, Planta
class Ambiente:
    def __init__(self, matriz_celdas, organismos):
        self.matriz_celdas = matriz_celdas
        self.organismos = organismos

    def ejecutar_ciclo(self):
        for organismo in self.organismos:
            organismo.mover_aleatoriamente()
        self.aplicar_eventos_aleatorios()


    def aplicar_eventos_aleatorios(self):
        for i in range(2): 
            evento = random.choice(["sequia", "lluvia", "plaga"])
            if evento == "sequia":
                self.aplicar_sequia()
            elif evento == "lluvia":
                self.aplicar_lluvia()
            elif evento == "plaga":
                self.aplicar_plaga()

    def aplicar_sequia(self):
        for organismo in self.organismos:
            if isinstance(organismo, Animal):
                organismo.energia -= 10
            elif isinstance(organismo, Planta):
                organismo.energia -= 5

    def aplicar_lluvia(self):
        for organismo in self.organismos:
            if isinstance(organismo, Planta):
                organismo.energia += 10

    def aplicar_plaga(self):
        for organismo in self.organismos:
            if isinstance(organismo, Animal):
                probabilidad_muerte = random.uniform(0, 1)
                if probabilidad_muerte > 0.7: 
                    organismo.morir()
