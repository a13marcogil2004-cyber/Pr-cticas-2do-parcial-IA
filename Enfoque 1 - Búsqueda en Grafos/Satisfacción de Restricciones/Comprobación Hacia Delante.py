def es_valido(tablero, fila, col):
    for i in range(fila):
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            return False
    return True

def forward_checking(tablero, fila, n):
    
    if fila == n:
        return tablero.copy()

    dominios_validos = []

    for col in range(n):
        if es_valido(tablero, fila, col):
            dominios_validos.append(col)

    if not dominios_validos:
        return None

    for col in dominios_validos:

        tablero[fila] = col

        resultado = forward_checking(tablero, fila + 1, n)

        if resultado:
            return resultado

        tablero[fila] = -1

    return None

def resolver_n_reinas(n):
    tablero = [-1] * n
    return forward_checking(tablero, 0, n)

solucion = resolver_n_reinas(8)

print("Solución:", solucion)