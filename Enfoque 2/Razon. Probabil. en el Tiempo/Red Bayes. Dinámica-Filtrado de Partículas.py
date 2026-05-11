import random

particulas = []

for _ in range(100):

    posicion = random.randint(0, 10)

    particulas.append(posicion)

observacion = 7

pesos = []

for p in particulas:

    peso = 1 / (1 + abs(observacion - p))

    pesos.append(peso)

suma_pesos = sum(pesos)

pesos = [
    p / suma_pesos
    for p in pesos
]

estimacion = 0

for i in range(len(particulas)):

    estimacion += (
        particulas[i]
        *
        pesos[i]
    )

print("Estimación:")

print(round(estimacion, 2))