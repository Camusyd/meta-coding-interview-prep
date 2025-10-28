# 🧩 Problema de Evaluación: Ganancia Máxima en Ventana Fija (K)

## Descripción del Problema

Dada una lista de números enteros `ganancias` (que representan las ganancias o pérdidas diarias) y un entero `k` (el tamaño de la ventana de inversión), debes encontrar la **suma de ganancias más grande** que se puede obtener en cualquier período continuo de `k` días.

Este problema simula encontrar la ventana de tiempo de `k` días que maximizó tu retorno.

## Restricciones y Casos Límite

* La lista `ganancias` puede contener números positivos (ganancia) y negativos (pérdida).
* `k` siempre será un número entero positivo.
* La longitud de `ganancias` es al menos igual a `k`.
* Si todas las ganancias son negativas, la salida debe ser la suma máxima (menos negativa) dentro de la ventana de tamaño `k`.

## 📝 Ejemplos

| Entrada (`ganancias`) | Entrada (`k`) | Salida Esperada | Explicación |
| :--- | :--- | :--- | :--- |
| `[1, 5, 2, 7, 8, 1]` | 3 | 17 | La suma máxima de 3 días es `[2, 7, 8]` (2 + 7 + 8 = 17). |
| `[4, 2, 1, 7, 8, 1, 2, 8, 1, 0]` | 3 | 16 | Hay dos ventanas con suma 16: `[1, 7, 8]` y `[2, 8, 1]`. |
| `[-4, -2, -1, -7, -8]` | 2 | -3 | La suma máxima es `-2 + (-1) = -3`. |

## 💡 Estrategia Sugerida

La solución ingenua (doble bucle) para este problema sería $O(n \times k)$ o $O(n^2)$. La solución óptima es utilizar el patrón de **Ventana Deslizante** para reducir la complejidad a **$O(n)$**.