# AgenteInteligente.py
Robot de Limpieza

Un agente inteligente en programación es un sistema de software o hardware capaz de percibir su entorno, procesar información y tomar decisiones autónomas para alcanzar ciertos objetivos. Estos agentes pueden adaptarse, aprender y mejorar su rendimiento con el tiempo mediante técnicas como la inteligencia artificial (IA) y el aprendizaje por refuerzo.

Ventajas de Python para crear un agente inteligente
Python es una excelente opción para desarrollar agentes inteligentes debido a varias razones:

Bibliotecas especializadas: Ofrece librerías como TensorFlow, scikit-learn, OpenAI Gym y Pandas que facilitan el aprendizaje automático y la toma de decisiones.

Funciones y librerías utilizadas:

random y time: Se usan para generar posiciones aleatorias en el entorno y simular retrasos en las acciones del robot.
AgenteInteligente (clase): Define al agente con atributos como posición, batería y métodos para percibir el entorno, tomar decisiones, moverse, aspirar y recargar.
percibir_entorno(): Escanea la cuadrícula en busca de suciedad (O, Y), obstáculos (X, mueble) y muestra su ubicación.
tomar_decision(): Determina qué acción realizar en función del estado del entorno.
aspirar(): Aspira la suciedad (O), pero no puede eliminar Y.
navegar(): Mueve al robot por la cuadrícula evitando obstáculos.
ir_a_recargar_si_es_necesario() y ir_a_recargar(): Administra la batería del robot y lo lleva a recargarse si es necesario.
pasar_tiempo(): Simula el paso de las horas y la carga de batería.
obtener_entorno(): Genera aleatoriamente un entorno con suciedad, obstáculos y muebles.



Este código simula un agente reactivo con cierto grado de inteligencia para la toma de decisiones basado en la percepción de su entorno.

Simula un robot aspirador operando en un entorno de 6x6. Su objetivo principal es limpiar la suciedad detectada mientras evita obstáculos y administra su nivel de batería. El robot percibe su entorno, toma decisiones basadas en la información disponible y actúa en consecuencia. Además, maneja un sistema básico de recarga de batería y navegación.

Estructura y funcionamiento del código
El código se divide en tres partes principales:

Definición del entorno: Se genera una cuadrícula 6x6 con obstáculos, muebles y diferentes tipos de suciedad.
Implementación del agente inteligente: Se define la clase AgenteInteligente, que contiene atributos y métodos para la toma de decisiones y ejecución de acciones.
Simulación del robot de limpieza: Se ejecuta un bucle de 24 iteraciones (simulando 24 horas), donde el agente percibe el entorno, actúa y administra su energía.
1. Definición del entorno (obtener_entorno())
El entorno es un diccionario donde cada celda de la cuadrícula 6x6 está representada por una tupla (fila, columna).

Elementos del entorno
Espacios vacíos (None): Lugares sin suciedad ni obstáculos.
Suciedad ligera ("O"): Puede ser aspirada sin problemas.
Suciedad difícil ("Y"): No puede ser aspirada por el robot.
Obstáculos ("X"): Bloquean el paso del robot.
Muebles ("mueble"): También bloquean el paso del robot.
Para poblar el entorno, se seleccionan posiciones aleatorias donde se colocan estos elementos. Se asegura que no haya dos elementos en la misma casilla.

2. Implementación del agente (class AgenteInteligente)
Esta clase define el comportamiento del robot de limpieza. Se inicializa con un nivel de batería de 100% y una posición inicial (0,0).

Atributos principales
entorno: Almacena la cuadrícula con los obstáculos y suciedad.
acciones_posibles: Lista de acciones que el robot puede tomar (aspirar, revisar_entorno, navegar).
posicion_actual: Coordenadas actuales del robot dentro de la cuadrícula.
bateria: Nivel de energía disponible, que disminuye con cada acción.
horas_transcurridas: Controla el tiempo transcurrido para evaluar cuándo debe recargar.
Métodos importantes
percibir_entorno()
El robot revisa todas las celdas y muestra qué hay en cada una. Luego, informa su posición actual.

tomar_decision()
Determina qué acción realizar:

Si hay suciedad ("O" o "Y") en la cuadrícula, decide aspirar.
Si no hay suciedad visible, decide revisar el entorno.
aspirar()
Si la celda actual tiene "O", se limpia con éxito.
Si la celda tiene "Y", el robot no puede limpiarla.
Cada acción de aspirado reduce la batería en 1%.
navegar()
El robot intenta moverse a una nueva posición en cuatro direcciones (derecha, abajo, izquierda, arriba). Solo se mueve si la nueva posición está dentro de los límites de la cuadrícula y no hay obstáculos ("X" o "mueble").

ir_a_recargar_si_es_necesario() e ir_a_recargar()
Si han pasado 2 horas, el robot verifica su batería:

Si tiene 15% o menos, va a su estación de recarga.
Si la batería está baja, aumenta entre 5% y 10% por iteración hasta llegar al 100%.
pasar_tiempo()
Simula el paso del tiempo en la simulación. Aumenta la batería de forma progresiva cuando está en la estación de carga.

3. Simulación del robot de limpieza
El robot se ejecuta en un bucle de 24 iteraciones, representando 24 horas. En cada ciclo:
