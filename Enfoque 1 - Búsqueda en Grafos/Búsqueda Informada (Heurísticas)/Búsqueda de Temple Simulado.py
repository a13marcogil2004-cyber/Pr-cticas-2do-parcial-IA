import random
import math

# -----------------------------
# DISTANCIA EUCLIDIANA
# -----------------------------
def distancia(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# -----------------------------
# COSTO TOTAL DE UNA RUTA
# -----------------------------
def costo(ruta, ciudades):
    total = 0
    for i in range(len(ruta)):
        total += distancia(ciudades[ruta[i]], ciudades[ruta[(i + 1) % len(ruta)]])
    return total

# -----------------------------
# GENERAR VECINO (swap)
# -----------------------------
def vecino(ruta):
    nueva = ruta.copy()
    i, j = random.sample(range(len(ruta)), 2)
    nueva[i], nueva[j] = nueva[j], nueva[i]
    return nueva

# -----------------------------
# TEMPLE SIMULADO
# -----------------------------
def simulated_annealing(ciudades, T=1000, enfriamiento=0.995, iteraciones=1000):

    # solución inicial
    actual = list(range(len(ciudades)))
    random.shuffle(actual)

    mejor = actual.copy()

    costo_actual = costo(actual, ciudades)
    mejor_costo = costo_actual

    print("Costo inicial:", costo_actual)

    for i in range(iteraciones):

        nueva = vecino(actual)

        costo_nueva = costo(nueva, ciudades)

        delta = costo_nueva - costo_actual

        # criterio de aceptación
        if delta < 0 or random.random() < math.exp(-delta / T):
            actual = nueva
            costo_actual = costo_nueva

        # actualizar mejor solución global
        if costo_actual < mejor_costo:
            mejor = actual.copy()
            mejor_costo = costo_actual

        # enfriamiento
        T *= enfriamiento

        if i % 100 == 0:
            print(f"Iter {i}: T={T:.2f}, costo={costo_actual:.2f}")

    return mejor, mejor_costo

# -----------------------------
# CIUDADES (ejemplo)
# -----------------------------
ciudades = [
    (0, 0),
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3),
    (1, 7)
]

# -----------------------------
# EJECUCIÓN
# -----------------------------
mejor_ruta, mejor_costo = simulated_annealing(ciudades)

print("\nMEJOR RUTA:")
print(mejor_ruta)
print("COSTO:", mejor_costo)