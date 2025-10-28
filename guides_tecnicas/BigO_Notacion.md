# 📈 Referencia Rápida de Notación Big O

La Notación Big O describe la **eficiencia de un algoritmo** en términos de tiempo ($T$) y espacio ($S$) a medida que el tamaño de la entrada ($N$) crece.

## Complejidad Temporal (Tiempo de Ejecución)

| Notación | Nombre | Descripción | Ejemplo Típico |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | Constante | El tiempo no cambia con el tamaño de $N$. | Acceder a un diccionario por clave (Python `dict[key]`). |
| **$O(\log n)$** | Logarítmica | El tiempo crece lentamente; el problema se divide a la mitad en cada paso. | Búsqueda Binaria en una lista ordenada. |
| **$O(n)$** | Lineal | El tiempo es directamente proporcional a $N$. | Recorrer una lista completa de $N$ elementos (un bucle). |
| **$O(n \log n)$** | Log-Lineal | Muy eficiente para ordenamiento. | Algoritmos de ordenación avanzados (Merge Sort). |
| **$O(n^2)$** | Cuadrática | El tiempo crece exponencialmente con $N^2$. | Bucles anidados, donde cada elemento se compara con los demás. |

## Reglas Clave de Big O

1.  **Ignorar Constantes:** $O(2N)$ es $O(N)$. $O(100)$ es $O(1)$.
2.  **Ignorar Términos Menores:** $O(N^2 + N)$ se reduce al término dominante: **$O(N^2)$**.
3.  **Complejidad de Múltiples Entradas:** Si tienes dos entradas no relacionadas ($N$ y $M$), la complejidad se multiplica o se suma: $O(N \times M)$ o $O(N + M)$.

## Complejidad Espacial (Uso de Memoria Auxiliar)

* **$O(1)$ (Constante):** El algoritmo usa una cantidad fija de memoria, independientemente del tamaño de la entrada (ej. variables de contador).
* **$O(n)$ (Lineal):** La memoria utilizada crece con el tamaño de la entrada (ej. crear una Tabla Hash o un `Set` para almacenar todos los elementos de una lista de tamaño $N$).