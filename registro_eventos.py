# registro_eventos.py

class RegistroEventos:
    def __init__(self):
        self.eventos = []
        self.intervalo_ciclico = None  # O simplemente elimina esta línea si no se usa

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def guardar_registro(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for evento in self.eventos:
                archivo.write(f"{evento}\n")

    def __str__(self):
        return "\n".join(self.eventos)

class HerramientasAnalisis:
    @staticmethod
    def analizar_registro(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                eventos = archivo.readlines()
                # Implementa la lógica de análisis según tus necesidades
                # Puedes procesar los eventos y extraer información útil.
                # Este es un ejemplo básico de impresión:
                print("Análisis de Registro:")
                for evento in eventos:
                    print(evento.strip())
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")

# Puedes agregar más funcionalidades según tus necesidades.
