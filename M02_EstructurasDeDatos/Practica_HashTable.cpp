// Practica_HashTable.cpp
// Ejemplo: Contar la frecuencia de caracteres en una cadena usando un Mapa (Tabla Hash)
// Complejidad Temporal: O(n) (lineal), donde n es la longitud de la cadena

#include <iostream>
#include <string>
#include <unordered_map> // std::unordered_map es la Tabla Hash en C++

using namespace std;

void contarFrecuencia(const string& str) {
    // 1. Declarar el Mapa: clave (char) -> valor (int)
    unordered_map<char, int> frecuencia;
    
    // 2. Recorrer la cadena una vez (O(n))
    for (char c : str) {
        // Incrementa el contador. Si 'c' no existe, lo crea e inicializa a 0 antes de incrementar.
        // Acceso y actualización es O(1) promedio.
        frecuencia[c]++; 
    }
    
    // 3. Imprimir el resultado
    cout << "Frecuencia de Caracteres:" << endl;
    for (const auto& par : frecuencia) {
        cout << par.first << ": " << par.second << endl;
    }
}

int main() {
    string texto = "programacion";
    contarFrecuencia(texto);

    // Output esperado:
    // p: 1, r: 2, o: 2, g: 1, a: 2, m: 1, c: 1, i: 1, n: 1
    
    return 0;
}