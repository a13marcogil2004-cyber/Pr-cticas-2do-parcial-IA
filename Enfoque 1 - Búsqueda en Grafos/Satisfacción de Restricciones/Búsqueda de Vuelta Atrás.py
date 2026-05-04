def backtracking(solucion):
    if es_solucion(solucion):
        return solucion

    for opcion in generar_opciones(solucion):
        if es_valida(opcion, solucion):
            agregar(opcion, solucion)
            resultado = backtracking(solucion)
            if resultado:
                return resultado
            quitar(opcion, solucion)

    return None

def es_valido(tablero, fila, col):
    for i in range(fila):
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            return False
    return True

def backtracking(tablero, fila, n):
    if fila == n:
        return tablero.copy()

    for col in range(n):
        if es_valido(tablero, fila, col):
            tablero[fila] = col

            resultado = backtracking(tablero, fila + 1, n)
            if resultado:
                return resultado

            tablero[fila] = -1

    return None

def resolver_n_reinas(n):
    tablero = [-1] * n
    return backtracking(tablero, 0, n)

solucion = resolver_n_reinas(8)

print(solucion)