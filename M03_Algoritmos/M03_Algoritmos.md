# ⚙️ MÓDULO 3: Algoritmos Clásicos y Patrones

El algoritmo es el conjunto de pasos para resolver un problema. El objetivo en una entrevista es encontrar el algoritmo **óptimo**.

## 1. Patrones Fundamentales de Algoritmos

### Búsqueda y Ordenamiento

| Algoritmo | Propósito | Complejidad Temporal | Notas Clave |
| :--- | :--- | :--- | :--- |
| **Búsqueda Binaria** | Encontrar un elemento en un conjunto **ordenado**. | $O(\log n)$ | Requiere que la entrada esté ordenada. Se basa en reducir el espacio de búsqueda a la mitad en cada paso. |
| **Merge Sort** | Ordenamiento externo de datos. | $O(n \log n)$ | Ejemplo clásico de *Divide y Vencerás*. Es estable y eficiente. |
| **Búsqueda Lineal** | Encontrar un elemento en un conjunto no ordenado. | $O(n)$ | Es la solución base (ingenua). |

### El Patrón "Divide y Vencerás"

* **Idea:** Descomponer un problema grande en subproblemas idénticos más pequeños, resolver los subproblemas, y luego combinar sus soluciones.
* **Ejemplos:** Merge Sort, Quick Sort, Búsqueda Binaria.
* **Clave de Reconocimiento:** El problema puede dividirse recursivamente en dos o más partes independientes.

## 2. Algoritmos de Optimización

### Algoritmos Voraces (Greedy)

* **Idea:** Tomar la **mejor decisión posible en el momento actual (localmente)** sin preocuparse por el impacto futuro de esa decisión.
* **Cuándo Usarlo:** Solo funciona para problemas donde la elección local óptima conduce a una solución global óptima (ej. dar cambio con el menor número de monedas).
* **Riesgo:** Si la mejor elección local no garantiza el óptimo global, se debe usar Programación Dinámica.

### Programación Dinámica (Dynamic Programming - DP)

* **Idea:** Resolver problemas complejos dividiéndolos en subproblemas superpuestos y **almacenando los resultados** de cada subproblema para evitar recalcularlos (memorización o tabulación).
* **Cuándo Usarlo:**
    1.  **Subproblemas Superpuestos:** El mismo subproblema se resuelve varias veces.
    2.  **Estructura Óptima:** La solución óptima se construye a partir de soluciones óptimas de los subproblemas.
* **Técnicas Clave:**
    * **Top-Down (Memorización):** Usar recursión con un *cache* (mapa) para guardar resultados.
    * **Bottom-Up (Tabulación):** Usar iteración y llenar una tabla (array) desde los casos base hasta la solución final.

### Backtracking (Vuelta Atrás)

* **Idea:** Usado para problemas de búsqueda que implican tomar una serie de decisiones. Si una decisión conduce a un callejón sin salida, se "vuelve atrás" a la última decisión y se prueba la siguiente opción.
* **Ejemplos:** Resolver Sudoku, encontrar todos los subconjuntos, generar permutaciones.
* **Estructura:** Típicamente implementado con recursión donde cada llamada explora una decisión y revierte el estado después de la exploración.

## 📘 Debes Dominar

* La **Búsqueda Binaria** es el patrón $O(\log n)$ más importante; úsala siempre que la entrada esté ordenada.
* Reconocer problemas de **Programación Dinámica** basados en si hay subproblemas que se repiten.
* Ser capaz de dibujar el **árbol de recursión** para entender el Backtracking y la DP.