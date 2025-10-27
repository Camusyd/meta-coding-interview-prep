# Ejemplo_BruteForce_vs_Optimal.py
# Problema: Encontrar si existe algún par de números en la lista que sumen K.

def brute_force_sum_k(arr, k):
    """
    Solución ingenua (Brute Force): Compara cada par posible.
    Complejidad Temporal: O(n^2)
    Complejidad Espacial: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                return True
    return False

def optimal_sum_k(arr, k):
    """
    Solución óptima: Usa un conjunto (Set/Tabla Hash) para un acceso O(1) promedio.
    Complejidad Temporal: O(n) (un solo recorrido)
    Complejidad Espacial: O(n) (para almacenar el conjunto)
    """
    seen = set()  # Almacena los números que ya hemos visto
    for num in arr:
        # El complemento necesario para sumar k
        complement = k - num
        
        # Verificar si el complemento ya está en nuestro conjunto (O(1) promedio)
        if complement in seen:
            return True
        
        # Añadir el número actual al conjunto
        seen.add(num)
        
    return False

# --- Pruebas y Comparación ---
data = [3, 5, 2, 7, 8, 1, 9]
target_k = 10

print(f"Datos: {data}, Objetivo K: {target_k}")

# Resultado O(n^2)
print(f"Brute Force (O(n^2)): {brute_force_sum_k(data, target_k)}") 

# Resultado O(n)
print(f"Óptima (O(n)): {optimal_sum_k(data, target_k)}")