# ecosistema.py
from registro_eventos import RegistroEventos, HerramientasAnalisis
from organismos import Animal, Planta
class Ecosistema:
    def __init__(self, matriz_espacial, motor_eventos, ambiente):
        self.matriz_espacial = matriz_espacial
        self.organismos = []
        self.motor_eventos = motor_eventos
        self.ambiente = ambiente

        # Inicializar el registro de eventos
        self.registro_eventos = RegistroEventos()

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

        # Agregar eventos al registro
        self.registro_eventos.agregar_evento("Ciclo de vida completado.")

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

        # Agregar eventos al registro
        self.registro_eventos.agregar_evento("Cadena alimenticia actualizada.")

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

    def guardar_registro(self):
        # Guardar el registro en un archivo
        self.registro_eventos.guardar_registro("registro_ecosistema.txt")

# En algún punto donde quieras analizar el registro
HerramientasAnalisis.analizar_registro("registro_ecosistema.txt")
