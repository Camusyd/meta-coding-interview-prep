# 🧱 MÓDULO 2: Introducción a las Estructuras de Datos

El dominio de las estructuras de datos (ED) es la mitad de la entrevista de codificación. La clave es saber **por qué** y **cuándo** usar cada una.

## 1. Estructuras de Acceso Directo y Secuencial

### Cadenas (Strings) y Arrays/Listas

| Característica | Complejidad Típica | Enfoque en Entrevistas |
| :--- | :--- | :--- |
| **Acceso por Índice** | $O(1)$ | Es la ED más rápida para leer/escribir si conoces la posición. |
| **Búsqueda por Valor** | $O(n)$ | Requiere recorrer todo el array. |
| **Inserción/Eliminación** | $O(n)$ | En medio del array, requiere mover todos los elementos subsiguientes. |
| **Técnicas Clave** | Punteros Dobles, Ventana Deslizante (Sliding Window), Prefijos/Sufijos. |

### Tablas Hash (Hash Maps, Diccionarios, Sets)

Las Tablas Hash son las ED más usadas para optimización.

* **Propósito:** Almacenar pares (clave, valor) o solo valores (Sets) con **acceso, inserción y eliminación promedio en $O(1)$**.
* **Compensación:** A cambio de velocidad, requieren **espacio extra $O(n)$** para almacenar los datos.
* **Enfoque en Entrevistas:** Úsalas siempre que necesites **buscar o contar frecuencias** y quieras evitar un bucle anidado $O(n^2)$.

## 2. Estructuras Lineales Dinámicas

### Pilas (Stacks) y Colas (Queues)

Estas estructuras se definen por su **orden de acceso** y siempre tienen $O(1)$ para sus operaciones clave.

| Estructura | Regla | Operaciones ($O(1)$) | Uso Típico |
| :--- | :--- | :--- | :--- |
| **Pila (Stack)** | LIFO (Last-In, First-Out) | `Push` (apilar), `Pop` (desapilar) | Evaluar expresiones, rastrear recursión (Backtracking), validación de paréntesis. |
| **Cola (Queue)** | FIFO (First-In, First-Out) | `Enqueue` (encolar), `Dequeue` (desencolar) | Procesamiento de tareas, recorridos en Grafos (BFS - Breadth-First Search). |

### Listas Enlazadas (Linked Lists)

* **Propósito:** Inserción y eliminación **$O(1)$** en los extremos (siempre que el nodo anterior sea conocido).
* **Compensación:** **Acceso por índice es $O(n)$** porque se debe recorrer secuencialmente desde la cabeza.
* **Enfoque en Entrevistas:** Úsalas cuando las inserciones/eliminaciones en el medio de una secuencia son más frecuentes que las búsquedas por índice. Problemas comunes: detección de ciclos, inversión de lista.

## 3. Estructuras Jerárquicas

* **Árboles y Grafos:** Se abordarán con más detalle en **MÓDULO 3** (Algoritmos) porque su utilidad se define por los algoritmos de recorrido que se les apliquen.

## 📘 Debes Dominar

1.  **Comparación de Complejidad:** Saber las complejidades de acceso, inserción y eliminación para Array vs. Hash Map vs. Linked List.
2.  **Uso Estratégico:** Identificar la estructura ideal para convertir un problema $O(n^2)$ en un problema $O(n)$.
3.  **Implementación:** Ser capaz de implementar los nodos básicos de una Pila o una Lista Enlazada.