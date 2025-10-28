// Practica_Arrays.js
// Ejemplo: Invertir un Array/Lista usando Punteros Dobles
// Complejidad Temporal: O(n)

function invertirArray(arr) {
    let izquierda = 0;
    let derecha = arr.length - 1;

    // Mientras el puntero izquierdo no cruce al derecho
    while (izquierda < derecha) {
        // 1. Intercambio de elementos (swap)
        [arr[izquierda], arr[derecha]] = [arr[derecha], arr[izquierda]];

        // 2. Mover punteros hacia el centro
        izquierda++;
        derecha--;
    }
    return arr;
}

const numeros = [1, 2, 3, 4, 5];
console.log("Original:", numeros);
console.log("Invertido:", invertirArray(numeros)); // Output: [5, 4, 3, 2, 1]