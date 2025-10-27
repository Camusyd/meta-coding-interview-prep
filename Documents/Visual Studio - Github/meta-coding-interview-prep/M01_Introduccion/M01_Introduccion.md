# 🧠 MÓDULO 1: Introducción a la Entrevista de Codificación

Este módulo establece las bases para una entrevista técnica exitosa. Cubre desde los fundamentos de la comunicación hasta el análisis de la eficiencia del código (Big O).

## 💡 1. Visión General de la Entrevista

El objetivo de la entrevista de codificación no es solo obtener un código que funcione, sino **demostrar tu proceso de pensamiento** como ingeniero.

### Tipos de Entrevistas Comunes

| Tipo de Entrevista | Descripción | Enfoque Principal |
| :--- | :--- | :--- |
| **Whiteboard / Documento** | Se pide escribir código o pseudocódigo en una pizarra o un documento compartido. | Lógica, sintaxis, y explicación clara del algoritmo. |
| **Online Coding (HackerRank/LeetCode)** | Se escribe y se ejecuta el código en un entorno de IDE online, con pruebas automatizadas. | Precisión, rendimiento y casos límite. |
| **Pair Programming** | Se trabaja junto al entrevistador en una base de código existente, añadiendo funcionalidades o depurando errores. | Colaboración, comprensión de código existente y refactorización. |

## 🗣️ 2. Comunicación Efectiva

La comunicación es tan crítica como la solución misma. El entrevistador necesita entender **cómo** llegaste a la solución.

### Estrategia de Comunicación

1.  **Preguntas Claves:** Aclara el problema antes de empezar. Pregunta sobre **casos límite**, restricciones de datos (tamaño, tipo), y si existe alguna restricción de tiempo/espacio.
2.  **Solución Ingenua (Brute Force):** Describe la primera solución que te venga a la mente, incluso si es ineficiente. Esto demuestra que comprendes el problema.
3.  **Optimización y Big O:** Discute los cuellos de botella de tu solución ingenua y cómo puedes mejorar su eficiencia.
4.  **Pseudocódigo:** Antes de escribir el código final, usa pseudocódigo para trazar la lógica del algoritmo optimizado.
5.  **Prueba:** Recorre la solución paso a paso con un ejemplo simple (o con un caso límite).

### Uso de Pseudocódigo

El pseudocódigo sirve como puente entre tu razonamiento verbal y la implementación real.

* **Definición:** Lenguaje informal y estructurado (una mezcla de lenguaje humano y sintaxis de programación) que describe los pasos de un algoritmo.
* **Regla:** Debe ser lo suficientemente detallado como para traducirse fácilmente a cualquier lenguaje de programación, pero lo suficientemente abstracto para ignorar detalles de sintaxis.

## ⚙️ 3. Fundamentos y Big O Notation

Para escribir código óptimo, debes comprender cómo se mide la eficiencia.

### Introducción a Big O

**Big O Notation (Notación de la Gran O)** es el estándar de la industria para describir la eficiencia de un algoritmo en términos de tiempo de ejecución (tiempo) y espacio ocupado (memoria), a medida que el tamaño de la entrada ($N$) crece.

| Notación | Nombre | Descripción | Ejemplo Típico |
| :--- | :--- | :--- | :--- |
| $O(1)$ | **Constante** | El tiempo de ejecución no cambia, sin importar el tamaño de la entrada. | Acceder a un elemento de un Array por su índice. |
| $O(\log n)$ | **Logarítmica** | El tiempo crece muy lentamente; la entrada se reduce a la mitad en cada paso. | Búsqueda Binaria. |
| $O(n)$ | **Lineal** | El tiempo de ejecución crece directamente proporcional al tamaño de la entrada. | Recorrer una lista de $N$ elementos (un solo bucle). |
| $O(n \log n)$ | **Log-Lineal** | Una combinación eficiente, común en algoritmos de ordenamiento rápido. | Merge Sort, Quick Sort. |
| $O(n^2)$ | **Cuadrática** | El tiempo crece exponencialmente con el cuadrado del tamaño de la entrada. | Recorrer todos los pares en una lista (bucles anidados). |

### Reglas Clave para el Análisis de Complejidad

1.  **Ignorar Constantes:** $O(2N)$ es simplemente $O(N)$.
2.  **Ignorar Términos Menores:** $O(N^2 + N)$ se reduce a $O(N^2)$, ya que el término de mayor orden domina el crecimiento.

### 📘 Debes Dominar

* Saber explicar cómo y por qué tu solución es eficiente.
* Distinguir entre código funcional y código **óptimo**.
* Reconocer patrones básicos de complejidad ($O(1)$, $O(n)$, $O(n^2)$).
* Usar preguntas clarificadoras antes de empezar a escribir código.