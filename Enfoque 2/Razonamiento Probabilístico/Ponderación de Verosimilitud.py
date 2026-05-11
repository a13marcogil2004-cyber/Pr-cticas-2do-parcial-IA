import random

muestras = 10000

peso_total = 0

peso_lluvia = 0

for _ in range(muestras):

    lluvia = random.random() < 0.3

    if lluvia:
        peso = 0.8

    else:
        peso = 0.2

    peso_total += peso

    if lluvia:
        peso_lluvia += peso

resultado = (
    peso_lluvia
    /
    peso_total
)

print(
    "P(Lluvia | Tráfico):"
)

print(round(resultado, 4))