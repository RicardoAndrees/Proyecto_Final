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




