import time

class SistemaMonitoreo:
    def __init__(self, ecosistema):
        self.ecosistema = ecosistema
        self.registro_eventos = []

    def monitorear_estado(self):
        estado_actual = {
            'num_organismos': len(self.ecosistema.organismos),
            'otros_datos': '... (agrega otros datos relevantes)'
        }
        self.registro_eventos.append({
            'tiempo': time.time(),
            'tipo': 'monitoreo_estado',
            'datos': estado_actual
        })

class HerramientasAnalisis:
    def __init__(self, sistema_monitoreo):
        self.sistema_monitoreo = sistema_monitoreo

    def crear_registro_eventos(self):
        with open('registro_eventos.log', 'w') as log_file:
            for evento in self.sistema_monitoreo.registro_eventos:
                log_file.write(f"{evento['tiempo']} - {evento['tipo']}: {evento['datos']}\n")

sistema_monitoreo = SistemaMonitoreo(mi_ecosistema)
herramientas_analisis = HerramientasAnalisis(sistema_monitoreo)

sistema_monitoreo.monitorear_estado()
herramientas_analisis.crear_registro_eventos()
