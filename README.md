# Proyecto_Final
Simulador de Ecosistemas
Este código en Python utiliza la biblioteca Pygame para simular un ecosistema.
el código establece las bases para simular un ecosistema con organismos (animales y plantas) en una matriz espacial, representando visualmente la simulación.
Se importan las bibliotecas necesarias, incluyendo Pygame para manejar la interfaz gráfica y varios módulos propios que estan relacionados con la representación y simulación del ecosistema
Se invoca pygame.init() para inicializar la biblioteca Pygame.

En el main principal
Matriz Espacial 
Se crea una matriz espacial de dimensiones 15x15 mediante la instancia de la clase MatrizEspacial.

Interfaz Gráfica
Se crea una interfaz gráfica mediante la instancia de la clase InterfazGrafica, pasando la matriz espacial como argumento.

Manejo de Eventos: 
Se verifica si hay eventos de Pygame, como la solicitud de cerrar la ventana, y se manejan adecuadamente.

Simulación del Ambiente: 
Se llama al método estático ejecutar_ciclo de la clase Ambiente. Este método contiene la lógica principal de la simulación, como la interacción entre los organismos y su entorno.

Movimiento Aleatorio: 
Se llama a métodos de la interfaz gráfica para mover sprites y organismos aleatoriamente.

Dibujar Ecosistema: 
Se llama a métodos de la interfaz gráfica para dibujar el estado actual del ecosistema.

Ejecución del Programa: Si el script se ejecuta directamente (es decir, no se importa como un módulo en otro script), se llama a la función main() para iniciar la simulación.


