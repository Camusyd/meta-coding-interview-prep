# Pilas y Colas en Python
# Practica_StackQueue.py
from collections import deque

# 1. Implementación de una Pila (Stack - LIFO)
# En Python, las listas normales son eficientes para Pilas (Push/Pop en el final)
pila = []

# PUSH (Agregar al final)
pila.append(10) # O(1)
pila.append(20) # O(1)
pila.append(30) # O(1)

# POP (Remover del final)
print(f"Pila: {pila}")
print(f"POP: {pila.pop()}") # 30
print(f"POP: {pila.pop()}") # 20
print(f"Pila después de Pops: {pila}")


# 2. Implementación de una Cola (Queue - FIFO)
# Usamos 'deque' para garantizar que Enqueue/Dequeue sean O(1) en ambos extremos
cola = deque()

# ENQUEUE (Agregar a la derecha)
cola.append(1) # O(1)
cola.append(2) # O(1)

# DEQUEUE (Remover de la izquierda)
print(f"\nCola: {cola}")
print(f"DEQUEUE: {cola.popleft()}") # 1
print(f"DEQUEUE: {cola.popleft()}") # 2
print(f"Cola después de Dequeues: {cola}")