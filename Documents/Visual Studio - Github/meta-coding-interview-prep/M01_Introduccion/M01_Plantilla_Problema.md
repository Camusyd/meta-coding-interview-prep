# 📋 Plantilla para la Resolución de Problemas de Entrevista

Sigue esta guía paso a paso para abordar cualquier pregunta de codificación.

## 1. Comprender y Aclarar (Preguntas Clave)

Antes de escribir código, demuestra que entiendes el problema.

* **Entrada:** ¿Qué tipo de datos recibo? (Array, String, Enteros...) ¿Puede estar vacía?
* **Salida:** ¿Qué tipo de resultado debo devolver? (Booleano, Lista, Entero...)
* **Restricciones:** ¿Hay números negativos? ¿Hay duplicados? ¿Hay un límite de memoria?

## 2. Ejemplo Simple

Usa el ejemplo proporcionado o crea uno simple para definir la entrada y la salida esperada.

* **ENTRADA:** `[Ejemplo de input]`
* **SALIDA ESPERADA:** `[Resultado esperado]`

## 3. Solución Ingenua (Fuerza Bruta)

Describe la solución más obvia y sencilla, aunque no sea eficiente.

* **Idea:** [Describe brevemente la lógica $O(n^2)$ o ineficiente].
* **Big O (Tiempo):** $O(\ldots)$
* **Big O (Espacio):** $O(\ldots)$

## 4. Optimización (El Salto Lógico)

Aquí es donde demuestras tu habilidad para optimizar el algoritmo.

* **Cuello de Botella:** ¿Qué parte de la solución ingenua está causando el $O(n^2)$? (Usualmente bucles anidados).
* **Estrategia:** ¿Puedo usar una Tabla Hash (Set/Map) para reducir la búsqueda a $O(1)$? ¿Puedo usar un puntero doble? ¿Puedo ordenar la entrada primero?
* **Nueva Big O (Tiempo):** $O(\ldots)$
* **Nueva Big O (Espacio):** $O(\ldots)$

### 5. Pseudocódigo (Problema Two Sum)

**Problema:**  
Dada una lista de números enteros (`nums`) y un objetivo (`target`), devuelve **True** si hay dos números en la lista que sumen el objetivo, usando un enfoque óptimo **O(n)**.

#### Pseudocódigo
```plaintext
// Inicializar la estructura de datos auxiliar
VISTOS = inicializar Conjunto_Vacío

PARA cada NUMERO en la lista NUMS:
    // Calcular el COMPLEMENTO necesario
    COMPLEMENTO = OBJETIVO - NUMERO
    
    // Verificar si el COMPLEMENTO ya está en VISTOS (Acceso O(1))
    SI COMPLEMENTO está en VISTOS:
        RETORNAR VERDADERO
    SINO:
        // Añadir el número actual a VISTOS para futuras verificaciones
        AÑADIR NUMERO a VISTOS
    
RETORNAR FALSO
```
---

### 🐍 6. Implementación y Prueba

### 💻 Código: Implementación en Python

```python
def encontrar_par_suma(nums: list[int], target: int) -> bool:
    """
    Verifica si existe un par de números en nums que sume el target.
    Complejidad Temporal: O(n)
    """
    vistos = set()  # Usamos un Set (Tabla Hash) para la búsqueda rápida
    
    for numero in nums:
        complemento = target - numero
        
        # El corazón del algoritmo O(n): Búsqueda en O(1)
        if complemento in vistos:
            return True
        
        vistos.add(numero)
        
    return False
```

#### Recorrido de Prueba Detallado

**Ejemplo:**  
`nums = [3, 5, 2, 7]`, **Objetivo:** `9`

| Iteración | Número | Complemento (9 - número) | Vistos       | ¿Complemento en vistos? | Acción       | Salida    |
|------------|---------|---------------------------|---------------|--------------------------|--------------|-----------|
| 1          | 3       | 6                         | `{}`          | No                       | Añadir 3     | Continúa  |
| 2          | 5       | 4                         | `{3}`         | No                       | Añadir 5     | Continúa  |
| 3          | 2       | 7                         | `{3, 5}`      | No                       | Añadir 2     | Continúa  |
| 4          | 7       | 2                         | `{3, 5, 2}`   | Sí                       | RETORNAR TRUE | **True**  |

---

### ⚙️ Análisis de Eficiencia

- **Tiempo:** `O(n)` (óptimo), ya que solo se requiere una pasada por la lista.  
- **Espacio:** `O(n)`, debido al espacio adicional utilizado por `vistos` (Set/Tabla Hash).

