def es_valido(tablero, fila, col):
    for i in range(fila):
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            return False
    return True

def backtracking(n, fila, tablero):
    if fila == n:
        return tablero

    for col in range(n):
        if es_valido(tablero, fila, col):
            tablero[fila] = col
            resultado = backtracking(n, fila + 1, tablero)
            if resultado:
                return resultado

    return None

def resolver_n_reinas(n):
    tablero = [-1] * n
    return backtracking(n, 0, tablero)

solucion = resolver_n_reinas(8)

print("Solución:")
print(solucion)