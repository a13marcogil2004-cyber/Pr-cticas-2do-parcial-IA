import random
import math

# Calcula distancia euclidiana entre dos ciudades
def distancia(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calcula el costo total de una ruta
def costo(ruta, ciudades):
    total = 0
    for i in range(len(ruta)):
        total += distancia(ciudades[ruta[i]], ciudades[ruta[(i + 1) % len(ruta)]])
    return total

# Crea un individuo (ruta aleatoria)
def crear_individuo(n):
    ruta = list(range(n))
    random.shuffle(ruta)
    return ruta

# Selección por torneo
def seleccion(poblacion, ciudades):
    torneo = random.sample(poblacion, 3)
    return min(torneo, key=lambda r: costo(r, ciudades))

# Cruce tipo Order Crossover (OX simplificado)
def crossover(p1, p2):
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    
    hijo = [-1] * n
    hijo[a:b] = p1[a:b]

    fill = [x for x in p2 if x not in hijo]

    idx = 0
    for i in range(n):
        if hijo[i] == -1:
            hijo[i] = fill[idx]
            idx += 1

    return hijo

# Mutación por intercambio (swap)
def mutacion(ruta):
    i, j = random.sample(range(len(ruta)), 2)
    ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

# Algoritmo genético principal
def algoritmo_genetico(ciudades, poblacion_size=50, generaciones=200, prob_mut=0.2):

    # Inicializar población
    poblacion = [crear_individuo(len(ciudades)) for _ in range(poblacion_size)]

    mejor = min(poblacion, key=lambda r: costo(r, ciudades))

    # Evolución
    for _ in range(generaciones):

        nueva_poblacion = []

        for _ in range(poblacion_size):

            # Selección de padres
            p1 = seleccion(poblacion, ciudades)
            p2 = seleccion(poblacion, ciudades)

            # Cruce
            hijo = crossover(p1, p2)

            # Mutación
            if random.random() < prob_mut:
                hijo = mutacion(hijo)

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        # Actualizar mejor solución
        actual = min(poblacion, key=lambda r: costo(r, ciudades))

        if costo(actual, ciudades) < costo(mejor, ciudades):
            mejor = actual

    return mejor


ciudades = [
    (0, 0),
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3),
    (1, 7)
]

# Ejecutar algoritmo
mejor_ruta = algoritmo_genetico(ciudades)

print("Mejor ruta:", mejor_ruta)
print("Costo:", costo(mejor_ruta, ciudades))