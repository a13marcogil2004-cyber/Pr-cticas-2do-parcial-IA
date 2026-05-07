def imprimir(tablero):
    for fila in tablero:
        print(fila)

def es_valido(tablero, fila, col, num):

    for x in range(9):
        if tablero[fila][x] == num:
            return False

    for x in range(9):
        if tablero[x][col] == num:
            return False

    inicio_fila = fila - fila % 3
    inicio_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False

    return True

def resolver(tablero):

    for fila in range(9):
        for col in range(9):

            if tablero[fila][col] == 0:

                posibles = []

                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        posibles.append(num)

                if len(posibles) == 0:
                    return False

                if len(posibles) == 1:
                    tablero[fila][col] = posibles[0]
                    return resolver(tablero)

                for num in posibles:
                    tablero[fila][col] = num

                    if resolver(tablero):
                        return True

                    tablero[fila][col] = 0

                return False

    return True

tablero = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

resolver(tablero)

imprimir(tablero)