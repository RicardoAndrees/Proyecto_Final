# Proyecto_Final
Simulador de Ecosistemas.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
Matriz Espacial

El metodo de inicialización crea una matriz bidimensional de tamaño filas x columnas e inicializa todas las celdas con None. Esta matriz se utilizará para representar el espacio espacial donde los organismos interactúan.

El metodo agregar organismo, agrega un organismo a la matriz en la posición correspondiente según las coordenadas del organismo.

Seguido de este metodo esta paara eliminar el organismo

Mover oganismo mueve un organismo desde su posición actual a una nueva posición en la matriz. Actualiza las entradas de la matriz para reflejar el cambio de posición del organismo.

obtener organismo: Dada una posición en la matriz, devuelve el organismo presente en esa posición.

El metodo encontrar posicion busca una posición adyacente disponible a la posición inicial dada. Luego, verifica si las nuevas coordenadas están dentro de los límites de la matriz y si la celda está vacía. Si encuentra una posición disponible, la devuelve; de lo contrario, devuelve la posición inicial.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

En organismos

Inicializa un organismo con una posición en la matriz, niveles de vida, energía y velocidad.

el metodo moverse ,mueve el organismo en una dirección dada en la matriz espacial, siempre y cuando la nueva posición esté dentro de los límites de la matriz.

el metodo reproducirse genera un nuevo organismo en una posición disponible cercana. Puede recibir atributos adicionales para la creación del nuevo organismo.

El metodo morir Elimina el organismo de la matriz espacial.

El metodo interaccion con el entorno aumenta la energía del organismo en función del factor abiótico del ambiente.

El ultimo metodo verifica si se esta vivo o no.

    --------------------------------

    Clase Animal (hereda de Organismo):

        Inicializa un animal con características específicas como especie, dieta y rol trófico. Asigna un sprite a partir de una imagen según la especie.

        El metodo cazar reduce la vida de una presa y aumenta la energía del depredador.

        comer_planta(self, planta, matriz_espacial): Consume una planta y aumenta la energía del animal.

        El metodo calcular distancia, calcula la distancia manhattan entre dos posiciones.

        El metodo reproducirse reproduce un nuevo animal si las condiciones son adecuadas.

        El metodo para buscar recurso mueve al animal hacia la planta más cercana.

        El medoto tomar decisiones oma decisiones sobre buscar recursos o reproducirse según su estado de energía.

        Tomar decisiones avanzadas, toma decisiones avanzadas basadas en la presencia de otros organismos en el ecosistema

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

La clase Ambiente, representa un entorno en el que se desarrolla el ecosistema simulado. 

Inicializa un ambiente con un factor abiótico dado.

Se puede especificar un fondo mediante la ruta de la imagen (fondo_path) o un color de fondo (fondo_color).
También se pueden proporcionar rutas de imágenes para representar árboles 

Metodo cargar_arbolitos(self, size):
Carga imágenes de árboles y las escala a un tamaño de 20x20 píxeles.
Genera una lista de tuplas que contienen la imagen del árbol y su posición aleatoria en el área superior del fondo.

Método dibujar_fondo:
Dibuja el fondo en la pantalla en función de la sección actual.
Si la sección actual es 0, dibuja el fondo en la parte superior.
Si la sección actual es 1, dibuja el fondo izquierdo.
Si la sección actual es 2, dibuja el fondo izquierdo en la parte superior y el fondo derecho en la parte inferior.

Método afectar_ecosistema:
Aumenta la energía de todos los organismos en el ecosistema multiplicando el factor abiótico por 10 y sumándolo a la energía de cada organismo.

Método generar_evento_climatico:
Genera un evento climático con una probabilidad del 20%.
Si se activa, reduce la velocidad de todos los organismos en el ecosistema a la mitad.

Método interactuar_con_ecosistema:
Llama a los métodos afectar_ecosistema y generar_evento_climatico, afectando así al ecosistema.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Clase InterfazGrafica:

Inicializa la interfaz gráfica de Pygame.
Crea la ventana de visualización con el título "Simulador de Ecosistemas".
Carga imágenes de fondo (mapita_2.png) y sprites de varios organismos (como "Lagartija", "León", "Cocodrilo", etc.).
Define parámetros como el tamaño de la pantalla, el número de celdas en x e y, y el ancho y alto de cada celda.
Inicializa matrices para almacenar información sobre las posiciones de los sprites y las direcciones de movimiento.

Método generar_direccion_aleatoria:
Genera aleatoriamente una dirección de movimiento (izquierda, derecha, arriba o abajo).

Método mover_sprites_aleatoriamente:
Mueve los sprites aleatoriamente en la pantalla.
Los sprites tienen diferentes límites de movimiento, y algunos de ellos tienen direcciones restringidas.

Método hay_sprite_en_celda:
Verifica si hay un sprite en una celda dada.

Método dibujar_ecosistema:
Dibuja el fondo, las celdas y los sprites en la pantalla.

Método actualizar_posicion_sprite:
Actualiza la posición de un sprite en función de su dirección de movimiento y verifica si hay colisiones o límites.

Método ejecutar_interfaz:
Inicia un bucle que maneja eventos de Pygame y actualiza continuamente la simulación.

Método main:
Inicia una instancia de la clase InterfazGrafica y ejecuta la simulación.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------