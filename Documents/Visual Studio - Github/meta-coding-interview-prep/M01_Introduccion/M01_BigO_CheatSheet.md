# 📉 Tabla de Referencia Rápida: Big O Cheat Sheet

Esta tabla resume la complejidad de tiempo y espacio de las operaciones clave para las estructuras de datos fundamentales.

| Estructura de Datos | Acceso (Tiempo) | Búsqueda (Tiempo) | Inserción (Tiempo) | Eliminación (Tiempo) |
| :--- | :--- | :--- | :--- | :--- |
| **Array (Lista)** | $O(1)$ | $O(n)$ | $O(n)$ (si no es al final) | $O(n)$ |
| **Lista Enlazada** | $O(n)$ | $O(n)$ | $O(1)$ (al inicio) | $O(1)$ (si el nodo es conocido) |
| **Tabla Hash (Set/Map/Dict)** | $N/A$ | $O(1)$ (promedio) | $O(1)$ (promedio) | $O(1)$ (promedio) |
| **Pila (Stack)** | $O(n)$ | $O(n)$ | $O(1)$ (Push) | $O(1)$ (Pop) |
| **Cola (Queue)** | $O(n)$ | $O(n)$ | $O(1)$ (Enqueue) | $O(1)$ (Dequeue) |
| **Árbol Binario de Búsqueda** | $O(\log n)$ (promedio) | $O(\log n)$ (promedio) | $O(\log n)$ (promedio) | $O(\log n)$ (promedio) |

**Nota sobre Complejidad Espacial (Auxiliar):**

* La mayoría de las operaciones fundamentales tienen una complejidad espacial de $O(1)$ (no usan memoria extra).
* Operaciones como el uso de conjuntos (`Set`) o diccionarios (`Map`) para optimización introducen una complejidad espacial de **$O(n)$**, donde $n$ es el número de elementos almacenados.