import random

muestras = 10000

trafico = 0

lluvia_y_trafico = 0

for _ in range(muestras):

    lluvia = random.random() < 0.3

    if lluvia:
        hay_trafico = random.random() < 0.8

    else:
        hay_trafico = random.random() < 0.2

    if hay_trafico:

        trafico += 1

        if lluvia:
            lluvia_y_trafico += 1

resultado = (
    lluvia_y_trafico
    /
    trafico
)

print(
    "P(Lluvia | Tráfico):"
)

print(round(resultado, 4))