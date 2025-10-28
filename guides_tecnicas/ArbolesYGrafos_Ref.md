# 🌲 Referencia de Alto Nivel: Árboles y Grafos

Aunque no son el foco principal del curso, la terminología es vital para entender problemas de jerarquías de datos y redes (estructuras comunes en *big data*).

## 1. Árboles (Trees)

Un Árbol es una estructura jerárquica:

* **Nodo:** Una entidad que contiene datos y referencias a otros nodos.
* **Raíz (Root):** El nodo superior, sin padres.
* **Hijo / Padre:** Relaciones directas descendentes / ascendentes.
* **Hoja (Leaf):** Un nodo sin hijos.
* **Tipos Comunes:**
    * **Árbol Binario (Binary Tree):** Cada nodo tiene como máximo dos hijos (izquierdo y derecho).
    * **Árbol Binario de Búsqueda (BST):** Un tipo de Árbol Binario donde los valores a la izquierda de un nodo son menores que el nodo, y los valores a la derecha son mayores. Esto permite la búsqueda en **$O(\log n)$**.

## 2. Grafos (Graphs)

Un Grafo es una colección de **Vértices** (nodos) y **Aristas** (conexiones entre ellos). Modelan redes (redes sociales, redes de carreteras, dependencias de software).

* **Vértice / Nodo:** La entidad de datos.
* **Arista / Borde (Edge):** La conexión entre dos vértices.
* **Tipos de Grafos:**
    * **Dirigido:** Las aristas tienen una dirección (A $\to$ B).
    * **No Dirigido:** Las aristas son bidireccionales (A $\leftrightarrow$ B).
    * **Ponderado:** Las aristas tienen un costo o peso (ej. distancia o tiempo).

## 3. Algoritmos de Recorrido

Dos algoritmos fundamentales para explorar nodos en Árboles y Grafos:

| Algoritmo | Siglas | Enfoque | Estructura de Datos Usada |
| :--- | :--- | :--- | :--- |
| **Búsqueda en Amplitud** | **BFS** (Breadth-First Search) | Explora nivel por nivel (horizontalmente). | **Cola (Queue)** |
| **Búsqueda en Profundidad** | **DFS** (Depth-First Search) | Explora tan profundo como sea posible antes de retroceder. | **Pila (Stack)** o Recursión Implícita |