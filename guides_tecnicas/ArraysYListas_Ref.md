# 🔄 Arrays/Listas y Ventana Deslizante (Python Focus)

Las listas en Python son la estructura de datos más utilizada. Dominar sus operaciones y los patrones de optimización es clave.

## 1. Operaciones de Listas en Python

| Operación | Complejidad | Notas |
| :--- | :--- | :--- |
| **Acceso por Índice** (`lista[i]`) | $O(1)$ | Rápido y constante. |
| **Añadir al Final** (`lista.append(x)`) | $O(1)$ (Promedio) | Muy rápido; a veces $O(n)$ si necesita reasignar memoria. |
| **Inserción en Medio** (`lista.insert(0, x)`) | $O(n)$ | Requiere desplazar todos los elementos. |
| **Búsqueda** (`x in lista`) | $O(n)$ | Requiere recorrer secuencialmente. |

## 2. Patrón: Ventana Deslizante (Sliding Window)

Este patrón transforma la forma en que se procesan sub-arrays/sub-cadenas para mejorar la eficiencia de $O(n^2)$ a **$O(n)$**.

* **Uso:** En problemas donde buscas una sub-secuencia (con tamaño fijo $K$ o variable) que cumpla una condición (suma máxima, longitud mínima sin repetir, etc.).
* **Componentes Esenciales:**
    1.  **Puntero Derecho (`j`):** Siempre avanza (expande la ventana).
    2.  **Puntero Izquierdo (`i`):** Solo avanza si la condición de la ventana se viola o si la ventana es de tamaño fijo.
    3.  **Métrica de Recálculo:** El cálculo de la métrica (suma, contador, promedio) se hace en **$O(1)$** en cada paso, restando el elemento saliente y sumando el entrante.

## 3. Optimización con Tablas Hash (Dict/Set)

Cuando la Ventana Deslizante tiene un tamaño **variable** (ej. "subcadena más larga *sin* repetición"), se utiliza una Tabla Hash:

* **Tabla Hash (Set/Dict):** Se usa para saber si un elemento ya está dentro de la ventana actual en tiempo $O(1)$.
* **Acción de Expansión:** El puntero derecho (`j`) avanza y el elemento se agrega al Hash.
* **Acción de Contracción:** Si se encuentra una repetición, el puntero izquierdo (`i`) avanza, y el elemento saliente (`i-1`) se elimina o se actualiza en el Hash.