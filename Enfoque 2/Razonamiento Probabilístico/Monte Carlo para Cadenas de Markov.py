import random

estado = 0

muestras = []

for _ in range(10000):

    propuesta = estado + random.choice([-1, 1])

    if abs(propuesta) < 5:

        estado = propuesta

    muestras.append(estado)

promedio = (
    sum(muestras)
    /
    len(muestras)
)

print("Promedio estimado:")

print(round(promedio, 4))