# Practica_MergeSort.py
# Implementación de Merge Sort (Algoritmo de Ordenamiento)
# Complejidad Temporal: O(n log n)

def merge_sort(arr):
    # Caso Base: Si el array tiene 1 o 0 elementos, ya está ordenado
    if len(arr) <= 1:
        return arr

    # 1. DIVIDIR (Divide)
    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    # Llamadas recursivas para dividir aún más
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # 2. COMBINAR (Conquer)
    return merge(izquierda_ordenada, derecha_ordenada)


def merge(arr_izq, arr_der):
    """Fusiona dos arrays ordenados en uno solo."""
    resultado = []
    i = j = 0 # Punteros para cada array

    # Mientras ambos arrays tengan elementos
    while i < len(arr_izq) and j < len(arr_der):
        if arr_izq[i] < arr_der[j]:
            resultado.append(arr_izq[i])
            i += 1
        else:
            resultado.append(arr_der[j])
            j += 1

    # Agregar cualquier elemento restante
    resultado.extend(arr_izq[i:])
    resultado.extend(arr_der[j:])
    
    return resultado

data = [9, 5, 1, 4, 3, 2]
print("Original:", data)
print("Ordenado:", merge_sort(data)) # Output: [1, 2, 3, 4, 5, 9]