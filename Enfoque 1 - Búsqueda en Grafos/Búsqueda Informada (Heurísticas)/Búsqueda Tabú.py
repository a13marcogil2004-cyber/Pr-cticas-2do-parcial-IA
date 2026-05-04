import random
import math
import copy


# DISTANCIA EUCLIDIANA
def distancia(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


# COSTO TOTAL DE UNA RUTA
def costo_ruta(ruta, ciudades):
    total = 0
    for i in range(len(ruta)):
        total += distancia(ciudades[ruta[i]], ciudades[ruta[(i + 1) % len(ruta)]])
    return total


# GENERAR VECINO (swap 2 ciudades)
def generar_vecino(ruta):
    vecino = ruta.copy()
    i, j = random.sample(range(len(ruta)), 2)
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino


# BÚSQUEDA TABÚ
def busqueda_tabu(ciudades, iteraciones=200, tamaño_tabu=10):

    # solución inicial (permuta aleatoria)
    actual = list(range(len(ciudades)))
    random.shuffle(actual)

    mejor = actual.copy()

    lista_tabu = []

    print("Costo inicial:", costo_ruta(actual, ciudades))

    for it in range(iteraciones):

        vecinos = []

        # generar vecinos
        for _ in range(20):
            vecino = generar_vecino(actual)

            if vecino not in lista_tabu:
                vecinos.append(vecino)

        if not vecinos:
            continue

        # mejor vecino
        mejor_vecino = min(vecinos, key=lambda r: costo_ruta(r, ciudades))

        actual = mejor_vecino

        # actualizar mejor global
        if costo_ruta(actual, ciudades) < costo_ruta(mejor, ciudades):
            mejor = actual.copy()

        # actualizar lista tabú
        lista_tabu.append(actual)

        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

        print(f"Iter {it+1}: costo = {costo_ruta(actual, ciudades):.2f}")

    return mejor


# EJEMPLO DE CIUDADES (x, y)
ciudades = [
    (0, 0),
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3),
    (1, 7)
]


# EJECUCIÓN
mejor_ruta = busqueda_tabu(ciudades)

print("\nMEJOR RUTA:")
print(mejor_ruta)
print("COSTO:", costo_ruta(mejor_ruta, ciudades))
