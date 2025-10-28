# Practica_Greedy.py
# Ejemplo: Problema del Cambio de Monedas
# En un sistema de monedas estándar (1, 5, 10, 25), el enfoque Greedy funciona

def greedy_coin_change(monto):
    """
    Calcula el menor número de monedas para devolver el cambio.
    Funciona porque cada moneda es más del doble de la anterior.
    """
    # Renombramos la lista para evitar la advertencia
    denominaciones = [25, 10, 5, 1] 
    conteo = {}
    
    monto_restante = monto
    
    # Aquí 'moneda' se refiere a la denominación actual (25, 10, 5, o 1)
    for moneda in denominaciones: 
        if monto_restante >= moneda:
            # ¿Cuántas veces cabe esta moneda en el monto restante?
            num_monedas = monto_restante // moneda
            conteo[moneda] = num_monedas
            
            # Actualizar el monto restante
            monto_restante %= moneda
            
    return conteo

monto_cambio = 63 # Ejemplo: $0.63
resultado = greedy_coin_change(monto_cambio)

print(f"Cambio para {monto_cambio} centavos:")

# Iteramos sobre el resultado, usando 'valor' y 'cantidad' para evitar redefiniciones
for valor, cantidad in resultado.items():
    if cantidad > 0:
        print(f"- {cantidad} moneda(s) de {valor} centavos")