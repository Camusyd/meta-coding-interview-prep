# Solucion_ProblemaX.py
# Problema de Evaluación: Ganancia Máxima en Ventana Fija (K)
# Patrón: Ventana Deslizante (Sliding Window)

def calcular_ganancia_maxima(ganancias: list[int], k: int) -> int:
    """
    Calcula la suma máxima que se puede obtener en cualquier subarray continuo de tamaño k.
    
    Complejidad Temporal: O(n) - Un solo recorrido por la lista.
    Complejidad Espacial: O(1) - Solo se usan variables constantes para el seguimiento.
    """
    n = len(ganancias)
    if n < k:
        # Según las restricciones, esto no debería ocurrir, pero es una buena práctica
        raise ValueError("El tamaño de la ventana (k) excede el tamaño de la lista de ganancias.")

    # 1. PRE-CÁLCULO: Inicializar la primera ventana [0...k-1]
    suma_actual = sum(ganancias[0:k])
    max_ganancia = suma_actual
    
    # 2. DESLIZAMIENTO: Mover la ventana un paso a la vez
    # El bucle comienza en k, ya que i=k representa el inicio del nuevo elemento que entra.
    for i in range(k, n):
        
        # Elemento que SALE de la ventana (ganancias[i - k] es el índice k posiciones antes)
        elemento_saliente = ganancias[i - k]
        
        # Elemento que ENTRA en la ventana (ganancias[i] es el nuevo elemento)
        elemento_entrante = ganancias[i]
        
        # 3. RECALCULAR LA SUMA (Operación O(1))
        # Esto evita sumar k elementos en cada iteración, manteniendo la eficiencia O(n)
        suma_actual = suma_actual - elemento_saliente + elemento_entrante
        
        # 4. ACTUALIZAR MÁXIMO
        max_ganancia = max(max_ganancia, suma_actual)
        
    return max_ganancia

# --- Recorrido de Prueba y Análisis ---

ganancias_ejemplo = [1, 5, 2, 7, 8, 1]
k_ejemplo = 3

print(f"Datos: {ganancias_ejemplo}, Ventana (k): {k_ejemplo}")
resultado = calcular_ganancia_maxima(ganancias_ejemplo, k_ejemplo)
print(f"Ganancia Máxima (Resultado Final): {resultado}") # Esperado: 17

# ANÁLISIS DEL RECORRIDO INTERNO (i=3 a i=5)
# i=3: Sale 1 (ganancias[0]), Entra 7 (ganancias[3]). Suma: (1+5+2) - 1 + 7 = 14. Max=14.
# i=4: Sale 5 (ganancias[1]), Entra 8 (ganancias[4]). Suma: 14 - 5 + 8 = 17. Max=17.
# i=5: Sale 2 (ganancias[2]), Entra 1 (ganancias[5]). Suma: 17 - 2 + 1 = 16. Max=17.