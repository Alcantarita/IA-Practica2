##Laboratorio 2: Búsqueda No Informada##

  Este repositorio contiene la implementación de dos soluciones usando búsqueda no informada mediante el algoritmo Depth-First Search (DFS) en Python. Ambas implementaciones utilizan una estructura de datos de pila (Stack) para explorar el espacio de soluciones.

#Contenido
  4-Puzzle utilizando DFS:
  El problema del 4-puzzle se resuelve mediante la implementación del algoritmo DFS.
  Se usa una pila para almacenar los posibles movimientos y un conjunto para rastrear los estados ya visitados.
  El objetivo es ordenar una secuencia de números del 1 al 4.
  Archivo: dfs_4_puzzle.py
  Laberinto utilizando DFS:
  El problema del laberinto se resuelve utilizando DFS para encontrar un camino desde el punto de inicio hasta la salida.
  Se implementa una pila para explorar las rutas posibles, evitando paredes y rutas ya visitadas.
  Archivo: dfs_maze.py
  
#Estructuras de Datos Implementadas
  Ambos programas emplean una pila (Stack) con las siguientes operaciones:
  
  push(item): Añade un elemento a la pila.
  pop(): Remueve y devuelve el último elemento de la pila.
  is_empty(): Comprueba si la pila está vacía.

#Cómo Ejecutar
  Clona el repositorio:
    git clone https://github.com/tu_usuario/lab2-busqueda-no-informada.git
  Dirígete al directorio del repositorio:
    cd lab2-busqueda-no-informada
  Ejecuta los scripts de Python:
  Para el 4-Puzzle: python dfs_4_puzzle.py
  Para el Laberinto: python dfs_maze.py

#Resultados
  4-Puzzle: El programa imprimirá el conjunto de pasos que lleva al estado objetivo.
  Laberinto: El programa mostrará el camino encontrado desde el inicio hasta la salida.
