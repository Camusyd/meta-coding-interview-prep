# 🗣️ Guía Rápida de Comunicación en Entrevistas

El entrevistador quiere saber cómo piensas, no solo el resultado final. ¡Habla mientras codificas!

## Antes de Empezar a Codificar

1.  **Aclara (5 minutos):** "Antes de empezar, permítame aclarar las restricciones. ¿Podemos asumir que los números son solo positivos? ¿Qué debo devolver si la lista está vacía?"
2.  **Define el Ejemplo (3 minutos):** "Usaré el ejemplo de `Input: [2, 7, 11, 15]` y `Target: 9`. El output esperado sería `[0, 1]` ya que $2 + 7 = 9$."

## Presentando Soluciones y Big O

1.  **Solución Inicial:** "Mi primera idea es la fuerza bruta, usando dos bucles anidados para revisar cada par. Esto sería simple de codificar, pero su complejidad temporal sería **$O(n^2)$**."
2.  **Optimización:** "Para mejorar esto y acercarme a **$O(n)$**, podemos sacrificar espacio. Usaré un **Hash Set (Tabla Hash)** para almacenar los números que ya he visto..."
3.  **Justificación de la Estructura:** "Decido usar una Tabla Hash porque me ofrece un tiempo de acceso y búsqueda de **$O(1)$ promedio**, lo que nos permite recorrer la lista solo una vez."

## Durante la Codificación

* **Verbaliza:** "Ahora voy a inicializar mi bucle. Dentro del bucle, estoy calculando el complemento y luego verificando la condición."
* **Bloqueo:** Si te quedas atascado: "Parece que me he topado con un caso de borde o un problema de índice. Permítame retroceder un paso y revisar mi suposición sobre [menciona la variable o el índice]."

## Finalizando y Probando

1.  **Confirmación:** "Creo que la solución está completa. ¿Le parece bien si la pruebo con mi ejemplo inicial y un caso límite?"
2.  **Prueba de Ejemplo:** "Con la entrada `[1, 5]`, y `Target: 6`. En la primera iteración, veo el 1, almaceno 1. En la segunda, busco $6-5=1$. Como 1 está en mi set, **retorno True**. Funciona."
3.  **Análisis Final:** "Esta solución final tiene una complejidad temporal de **$O(n)$** y una complejidad espacial de **$O(n)$** para almacenar la Tabla Hash. Esto es óptimo para la mayoría de los casos."