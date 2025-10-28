# ✍️ Guía de Pseudocódigo para Entrevistas

El pseudocódigo es el borrador de tu código. Su objetivo es demostrar tu lógica al entrevistador antes de que te distraigas con la sintaxis.

## 1. Estructura Básica

Utiliza palabras clave claras en mayúsculas y sangría para definir bloques de código (similar a Python, pero más flexible).

| Concepto | Pseudocódigo Sugerido |
| :--- | :--- |
| **Definir Función** | `FUNCIÓN nombre_funcion(argumento1, argumento2):` |
| **Condicional** | `SI condicion ES VERDADERA:` |
| **Bucle (Contador)** | `PARA i DESDE 0 HASTA N-1:` |
| **Bucle (Iteración)** | `PARA cada ELEMENTO en LISTA:` |
| **Asignación** | `VARIABLE = valor` |
| **Retorno** | `RETORNAR resultado` |

## 2. Ejemplo Práctico (Two Sum)

**Problema:** Encontrar si dos números suman un `OBJETIVO` usando un Hash Set.

```text
FUNCIÓN encontrar_suma_par(NUMS, OBJETIVO):
    # Inicialización de la estructura O(n)
    VISTOS = inicializar Conjunto_Vacío 

    PARA cada NUMERO en NUMS:
        COMPLEMENTO = OBJETIVO - NUMERO
        
        # Verificación O(1)
        SI COMPLEMENTO está en VISTOS:
            RETORNAR VERDADERO
        SINO:
            AÑADIR NUMERO a VISTOS
            
    RETORNAR FALSO
```
---

## 3. Consejos de Comunicación

- `Verbaliza las Estructuras:` Menciona la estructura de datos que usarás: "Usaré un Mapa/Diccionario para mapear el elemento a su índice..."

- `Declara Big O:` Después de tu pseudocódigo, di: "Esta solución reduce la complejidad a $O(n)$ en tiempo y $O(n)$ en espacio."