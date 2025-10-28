package M03_Algoritmos;

// Practica_DP_Fibonacci.java
// Implementación de Fibonacci usando Programación Dinámica (Memorización - Top-Down)
// Complejidad Temporal: O(n) (se calcula cada F(i) una sola vez)
// La versión recursiva sin DP sería O(2^n)

import java.util.HashMap;
import java.util.Map;

public class Practica_DP_Fibonacci {
    
    // Almacenamiento (cache/mapa) para guardar los resultados ya calculados
    private static Map<Integer, Long> memo = new HashMap<>();

    public static long fibonacciDP(int n) {
        if (n <= 1) {
            return n; // Caso base: F(0)=0, F(1)=1
        }

        // 1. Verificar si el resultado ya está en el mapa
        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        // 2. Calcular el resultado
        long resultado = fibonacciDP(n - 1) + fibonacciDP(n - 2);

        // 3. Almacenar el resultado antes de retornar
        memo.put(n, resultado);
        return resultado;
    }

    public static void main(String[] args) {
        int n = 40; // Probar con un número grande que haría colapsar la recursión simple
        
        System.out.println("Calculando F(" + n + ") con DP...");
        long inicio = System.currentTimeMillis();
        long resultado = fibonacciDP(n);
        long fin = System.currentTimeMillis();
        
        System.out.println("F(" + n + ") = " + resultado);
        System.out.println("Tiempo de ejecución: " + (fin - inicio) + " ms");
    }
}
