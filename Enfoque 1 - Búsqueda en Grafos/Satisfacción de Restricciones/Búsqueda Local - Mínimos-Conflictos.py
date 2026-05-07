import random

def conflictos(tablero, fila, col):

    total = 0

    for i in range(len(tablero)):

        if i != fila:

            if tablero[i] == col:
                total += 1

            if abs(tablero[i] - col) == abs(i - fila):
                total += 1

    return total

def min_conflicts(n, max_iter=1000):

    tablero = [random.randint(0, n - 1) for _ in range(n)]

    for _ in range(max_iter):

        conflictos_totales = []

        for fila in range(n):
            c = conflictos(tablero, fila, tablero[fila])
            conflictos_totales.append(c)

        if sum(conflictos_totales) == 0:
            return tablero

        filas_conflicto = [
            i for i in range(n)
            if conflictos_totales[i] > 0
        ]

        fila = random.choice(filas_conflicto)

        mejor_col = tablero[fila]
        menor_conflicto = conflictos(tablero, fila, mejor_col)

        for col in range(n):

            c = conflictos(tablero, fila, col)

            if c < menor_conflicto:
                menor_conflicto = c
                mejor_col = col

        tablero[fila] = mejor_col

    return None

solucion = min_conflicts(8)

print("Solución:")
print(solucion)