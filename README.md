# Proyecto_Final
Simulador de Ecosistemas
Este código en Python utiliza la biblioteca Pygame para simular un ecosistema.
el código establece las bases para simular un ecosistema con organismos (animales y plantas) en una matriz espacial, representando visualmente la simulación.
Se importan las bibliotecas necesarias, incluyendo Pygame para manejar la interfaz gráfica y varios módulos propios que estan relacionados con la representación y simulación del ecosistema
Se invoca pygame.init() para inicializar la biblioteca Pygame.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Ejecución del Programa: 
Si el script se ejecuta directamente (es decir, no se importa como un módulo en otro script), se llama a la función main() para iniciar la simulación.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

En ecosistema
La clase Ecosistema se inicializa con parámetros como el número de filas (rows), el número de columnas (cols), una lista de ambientes (ambientes), y el tamaño de la ventana (size). La matriz espacial (matriz_espacial) se crea con las dimensiones especificadas.

La función add_organism agrega un organismo al ecosistema, actualizando tanto la lista de organismos como la matriz espacial.

La función dibujar_ecosistema se encarga de representar gráficamente el estado actual del ecosistema en la pantalla. Utiliza Pygame para cargar imágenes de sprites de animales y plantas, ajustando su posición en función de las coordenadas de la matriz espacial y la sección actual de la pantalla.

La función dibujar_fondos se encarga de representar gráficamente los fondos de las secciones en la pantalla.

La función run_cycle realiza un ciclo de simulación para todos los organismos en el ecosistema. Para cada organismo, se lleva a cabo una serie de acciones:

interactuar_con_entorno: El organismo interactua con el ambiente actual.
moverse: El organismo se mueve en una direccion aleatoria según la matriz espacial.
envejecer: La edad del organismo aumenta.
energia: La energía del organismo disminuye.
reproducirse: Si el organismo está vivo, busca una pareja y se reproduce.
Si el organismo ya no está vivo, se elimina de la lista de organismos.

La función obtener pareja busca posibles parejas para un organismo en la lista de organismos. La pareja seleccionada se utiliza en el proceso de reproducción.

La función obtener_direccion devuelve una dirección aleatoria entre arriba, abajo, izquierda o derecha.
este código define un entorno de simulación donde los organismos (tigres y plantas) interactúan con su entorno y entre ellos en un ciclo de simulación continuo. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







