import random

datos = []

for _ in range(1000):

    valor = random.gauss(10, 2)

    datos.append(valor)

media = (
    sum(datos)
    /
    len(datos)
)

varianza = (
    sum(
        (x - media) ** 2
        for x in datos
    )
    /
    len(datos)
)

print("Media:")

print(round(media, 4))

print("\nVarianza:")

print(round(varianza, 4))