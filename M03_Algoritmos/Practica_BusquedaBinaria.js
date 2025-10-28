// Practica_BusquedaBinaria.js
// Implementación clásica de Búsqueda Binaria (Iterativa)
// Complejidad Temporal: O(log n)

function busquedaBinaria(arr, target) {
    let inicio = 0;
    let fin = arr.length - 1;

    // Continúa mientras el espacio de búsqueda sea válido
    while (inicio <= fin) {
        // Calcular el punto medio (mejor forma para evitar overflow en lenguajes como C++)
        let medio = Math.floor(inicio + (fin - inicio) / 2);

        if (arr[medio] === target) {
            return medio; // ¡Encontrado! Devuelve el índice
        } else if (arr[medio] < target) {
            // El objetivo está en la mitad derecha
            inicio = medio + 1;
        } else {
            // El objetivo está en la mitad izquierda
            fin = medio - 1;
        }
    }

    return -1; // Objetivo no encontrado
}

const numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
console.log(`Buscando 23: Indice ${busquedaBinaria(numeros, 23)}`); // 5
console.log(`Buscando 42: Indice ${busquedaBinaria(numeros, 42)}`); // -1