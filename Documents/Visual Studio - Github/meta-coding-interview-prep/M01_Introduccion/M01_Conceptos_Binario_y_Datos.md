# 🔢 Conceptos Fundamentales: Binario y Representación de Datos

Una base sólida en cómo la computadora almacena la información te ayuda a comprender los límites de los tipos de datos y las operaciones a nivel de bit.

## Sistema Binario (Base 2)

* **Bits:** La unidad fundamental de información. Un bit puede tener el valor de **0** o **1** (Apagado o Encendido).
* **Byte:** Un grupo de 8 bits.
* **Representación:** Los números enteros se representan con una serie de potencias de 2.
    * Ejemplo: $1010_2 = (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) = 8 + 0 + 2 + 0 = 10_{10}$

## Representación de Datos

* **Enteros (Integers):**
    * Usualmente se representan usando 32 o 64 bits.
    * **Importancia:** Conocer los límites de un entero de 32 bits ($\approx \pm 2.1$ mil millones) es crucial para evitar **desbordamientos (overflows)** en problemas de suma o multiplicación.
* **Números Flotantes (Floats/Doubles):**
    * Se representan de manera aproximada utilizando notación científica binaria.
    * **Cuidado:** Las comparaciones de igualdad estricta (`==`) con números flotantes suelen ser inseguras debido a la imprecisión.
* **Caracteres (Chars) y Cadenas (Strings):**
    * Los caracteres se almacenan como números enteros usando estándares como **ASCII** o **Unicode (UTF-8)**.
    * Las cadenas son simplemente secuencias (arrays) de caracteres.

## ⚠️ Implicación en Entrevistas

* **Overflows:** Siempre pregunta sobre el **rango** de los números de entrada. Si la suma de dos números puede exceder el límite de un entero de 32 bits, necesitarás usar un tipo de datos de 64 bits (como `long` en Java o `int` en Python si usa precisión arbitraria).
* **Comparaciones de Flotantes:** Evita `if a == b:` para flotantes. Usa `if abs(a - b) < epsilon:` para comparar con una pequeña tolerancia.