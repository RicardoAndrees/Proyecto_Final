from organismos import Animal, Planta
from matriz_espacial import MatrizEspacial
from motor_eventos import MotorEventos

class Ecosistema:
    def __init__(self, matriz_espacial, motor_eventos, ambiente):
        self.matriz_espacial = matriz_espacial
        self.organismos = []
        self.motor_eventos = motor_eventos
        self.ambiente = ambiente

    def ciclo_vida(self):
        self.motor_eventos.realizar_ciclo()
        for organismo in self.organismos:
            organismo.mover()
            organismo.vida -= 1

            if organismo.vida <= 0:
                organismo.morir()
                self.organismos.remove(organismo)

            pareja = self.encontrar_pareja(organismo)
            if pareja:
                nuevo_organismo = organismo.reproducir(pareja)
                if nuevo_organismo:
                    self.organismos.append(nuevo_organismo)

    def encontrar_pareja(self, organismo):
        for otro_organismo in self.organismos:
            if (
                isinstance(otro_organismo, type(organismo)) and
                otro_organismo != organismo and
                abs(otro_organismo.posicion[0] - organismo.posicion[0]) < 2 and
                abs(otro_organismo.posicion[1] - organismo.posicion[1]) < 2
            ):
                return otro_organismo
        return None

    def cadena_alimenticia(self):
        for organismo in self.organismos:
            if isinstance(organismo, Planta):
                organismo.fotosintesis()
            elif isinstance(organismo, Animal):
                presa = self.encontrar_presa(organismo)
                if presa:
                    organismo.cazar(presa)

    def encontrar_presa(self, depredador):
        for organismo in self.organismos:
            if (
                isinstance(organismo, Animal) and
                organismo != depredador and
                abs(organismo.posicion[0] - depredador.posicion[0]) < 2 and
                abs(organismo.posicion[1] - depredador.posicion[1]) < 2
            ):
                return organismo
        return None
