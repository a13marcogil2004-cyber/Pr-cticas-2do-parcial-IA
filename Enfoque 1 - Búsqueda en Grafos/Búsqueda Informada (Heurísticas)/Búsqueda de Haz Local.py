import random
import math


# DISTANCIA EUCLIDIANA
def distancia(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


# COSTO TOTAL DE UNA RUTA
def costo(ruta, ciudades):
    total = 0
    for i in range(len(ruta)):
        total += distancia(ciudades[ruta[i]], ciudades[ruta[(i + 1) % len(ruta)]])
    return total


# GENERAR VECINO (swap)
def vecino(ruta):
    nueva = ruta.copy()
    i, j = random.sample(range(len(ruta)), 2)
    nueva[i], nueva[j] = nueva[j], nueva[i]
    return nueva


# BÚSQUEDA DE HAZ LOCAL
def local_beam_search(ciudades, k=5, iteraciones=100):

  
    # inicializar k soluciones aleatorias
    poblacion = []
    for _ in range(k):
        ruta = list(range(len(ciudades)))
        random.shuffle(ruta)
        poblacion.append(ruta)

    mejor_global = min(poblacion, key=lambda r: costo(r, ciudades))

    print("Costo inicial mejor:", costo(mejor_global, ciudades))

    for it in range(iteraciones):


        # generar vecinos de toda la población
        vecinos = []

        for ruta in poblacion:
            for _ in range(3):  # vecinos por solución
                vecinos.append(vecino(ruta))


        # seleccionar los k mejores vecinos
        vecinos.sort(key=lambda r: costo(r, ciudades))
        poblacion = vecinos[:k]


        # actualizar mejor global
        mejor_actual = poblacion[0]

        if costo(mejor_actual, ciudades) < costo(mejor_global, ciudades):
            mejor_global = mejor_actual

        if it % 10 == 0:
            print(f"Iter {it}: mejor costo = {costo(mejor_global, ciudades):.2f}")

    return mejor_global


# CIUDADES (ejemplo)
ciudades = [
    (0, 0),
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3),
    (1, 7)
]


# EJECUCIÓN
mejor_ruta = local_beam_search(ciudades, k=5, iteraciones=50)

print("\nMEJOR RUTA ENCONTRADA:")
print(mejor_ruta)
print("COSTO:", costo(mejor_ruta, ciudades))